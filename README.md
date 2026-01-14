# FInDER Lab Website

A research lab website built with Quarto, hosted on GitHub Pages, and automated with GitHub Actions.

## Features

- **Quarto-based**: Modern, reproducible website using Quarto
- **GitHub Pages**: Free hosting via GitHub Pages
- **Automated Deployment**: GitHub Actions automatically builds and deploys on every push
- **Bibliography Support**: BibTeX bibliography integration for publications
- **Markdown-based Content**: People and projects as Markdown files
- **Responsive Design**: Mobile-friendly layout

## Setup Instructions

### 1. Prerequisites

- A GitHub account
- Git installed on your computer
- (Optional) Quarto installed locally for previewing

### 2. Repository Setup

1. Push this repository to GitHub (if not already there)
2. Go to your repository Settings → Pages
3. Under "Source", select "GitHub Actions"
4. The GitHub Actions workflow will automatically build and deploy your site

### 3. Customization

#### Update Basic Information

- Edit `_quarto.yml` to change the site title, navigation, and theme
- Update `index.qmd`, `about.qmd`, and `contact.qmd` with your lab information
- Replace placeholder email addresses and contact information
- Update social media links in `_quarto.yml`

#### Add People

You can add people in two ways:

1. **Directly edit `people.qmd`**: Simple, works for a small number of people
2. **Create individual Markdown files**: 
   - Create a file in the `people/` directory (e.g., `people/jane-doe.md`)
   - Use `people/_template.md` as a template
   - Reference the file in `people.qmd` or create a custom rendering system

#### Add Projects

Similar to people:

1. **Directly edit `projects.qmd`**: Simple approach
2. **Create individual Markdown files**:
   - Create files in the `projects/` directory
   - Use `projects/_template.md` as a template
   - Reference or include them in `projects.qmd`

#### Add Publications

Publications are managed via BibTeX:

1. Edit `references.bib` and add your publications in BibTeX format
2. Cite them in `publications.qmd` using `[@citation-key]`
3. The bibliography will automatically render when you build the site

Example BibTeX entry:
```bibtex
@article{smith2024,
  title = {Your Publication Title},
  author = {Smith, John and Doe, Jane},
  journal = {Journal Name},
  year = {2024},
  volume = {1},
  pages = {1--10},
  doi = {10.1000/xyz123}
}
```

#### ORCID Integration (Optional)

To automatically sync publications from ORCID:

1. Get your ORCID ID from https://orcid.org
2. Use the ORCID Public API to fetch publications
3. Create a script to convert ORCID data to BibTeX format
4. Add a GitHub Actions workflow step to run the script and update `references.bib`

Example approach:
- Use Python with `pybtex` or `bibtexparser` libraries
- Use R with `rorcid` package
- Create a script that fetches from ORCID API and converts to BibTeX
- Run the script in GitHub Actions before building

### 4. Local Development (Optional)

To preview the site locally:

1. Install Quarto: https://quarto.org/docs/get-started/
2. Install R (required for bibliography rendering): https://www.r-project.org/
3. Install R packages:
   ```r
   install.packages(c("RefManageR", "bibtex"))
   ```
4. Render the site:
   ```bash
   quarto render
   ```
5. Preview:
   ```bash
   quarto preview
   ```

### 5. Custom Styling

Edit `styles.css` to customize the appearance of your site.

## File Structure

```
.
├── _quarto.yml          # Quarto configuration
├── index.qmd            # Home page
├── about.qmd            # About page
├── people.qmd           # People page
├── projects.qmd         # Projects page
├── publications.qmd     # Publications page
├── contact.qmd          # Contact page
├── references.bib       # Bibliography (BibTeX)
├── styles.css           # Custom CSS
├── README.md            # This file
├── .github/
│   └── workflows/
│       └── publish.yml  # GitHub Actions workflow
├── people/              # Individual people pages (optional)
│   ├── _template.md
│   └── jane-doe.md
└── projects/            # Individual project pages (optional)
    ├── _template.md
    └── example-project-1.md
```

## Deployment

The site is automatically deployed via GitHub Actions whenever you push to the `main` branch:

1. The workflow checks out your repository
2. Sets up Quarto
3. Renders the Quarto website
4. Deploys to GitHub Pages

Your site will be available at: `https://[your-username].github.io/[repository-name]/`

## Troubleshooting

### Bibliography Not Rendering

- Ensure R is available in the GitHub Actions environment (it should be by default)
- Check that `RefManageR` and `bibtex` R packages are available
- Verify your BibTeX syntax is correct
- Check GitHub Actions logs for errors

### Site Not Updating

- Check GitHub Actions workflow status
- Ensure GitHub Pages is enabled and set to use GitHub Actions as source
- Check for build errors in the Actions tab

### Local Preview Issues

- Make sure Quarto and R are installed
- Install required R packages
- Check that all file paths are correct

## License

[Add your license here, or remove this section]

## Acknowledgments

Built with [Quarto](https://quarto.org/), hosted on [GitHub Pages](https://pages.github.com/).
