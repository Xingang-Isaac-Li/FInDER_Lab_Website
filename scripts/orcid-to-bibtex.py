#!/usr/bin/env python3
"""
Example script to fetch publications from ORCID and convert to BibTeX format.

This is a template script that you can customize for your ORCID profile.
Requires: requests, pybtex (install via: pip install requests pybtex)

Usage:
    python orcid-to-bibtex.py YOUR_ORCID_ID > new_publications.bib

Note: You'll need to manually merge the output with references.bib
"""

import sys
import requests
import json
from pybtex.database import Entry, Person
from pybtex.database.output.bibtex import Writer

def fetch_orcid_works(orcid_id):
    """Fetch works from ORCID API."""
    url = f"https://pub.orcid.org/v3.0/{orcid_id}/works"
    headers = {
        "Accept": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching ORCID data: {e}", file=sys.stderr)
        return None

def orcid_to_bibtex(works_data):
    """Convert ORCID works to BibTeX format."""
    if not works_data or 'group' not in works_data:
        return []
    
    entries = []
    for group in works_data['group']:
        # Get the most preferred work summary
        work_summary = group['work-summary'][0]
        
        # Extract title
        title = work_summary.get('title', {}).get('title', {}).get('value', 'Untitled')
        
        # Extract publication date
        pub_date = work_summary.get('publication-date', {})
        year = pub_date.get('year', {}).get('value', '')
        
        # Extract DOI
        ext_ids = work_summary.get('external-ids', {}).get('external-id', [])
        doi = None
        for ext_id in ext_ids:
            if ext_id.get('external-id-type') == 'doi':
                doi = ext_id.get('external-id-value')
                break
        
        # Create a citation key
        citation_key = f"orcid{year}{hash(title) % 10000}"
        
        # Extract authors (if available)
        # Note: ORCID API structure may vary, adjust as needed
        
        # Create BibTeX entry
        entry_type = 'article'  # Default, adjust based on work type
        entry = Entry(entry_type)
        entry.fields['title'] = title
        if year:
            entry.fields['year'] = str(year)
        if doi:
            entry.fields['doi'] = doi
            entry.fields['url'] = f"https://doi.org/{doi}"
        
        entries.append((citation_key, entry))
    
    return entries

def main():
    if len(sys.argv) != 2:
        print("Usage: python orcid-to-bibtex.py ORCID_ID", file=sys.stderr)
        sys.exit(1)
    
    orcid_id = sys.argv[1]
    print(f"# Publications fetched from ORCID: {orcid_id}", file=sys.stderr)
    print("# Review and merge manually with references.bib\n", file=sys.stderr)
    
    works_data = fetch_orcid_works(orcid_id)
    if not works_data:
        sys.exit(1)
    
    entries = orcid_to_bibtex(works_data)
    
    # Output BibTeX
    writer = Writer(sys.stdout)
    for key, entry in entries:
        writer.write_entry(key, entry)

if __name__ == "__main__":
    main()
