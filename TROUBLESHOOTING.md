# Troubleshooting Guide

## 404 Error on GitHub Pages

If you're seeing a 404 error even though GitHub says your site is deployed:

### Step 1: Check GitHub Actions Logs

1. Go to your repository on GitHub
2. Click the **Actions** tab
3. Check if the latest workflow run completed successfully
4. If there are errors, check the logs to see what went wrong

### Step 2: Verify Base URL Configuration

For GitHub Pages, your site is hosted at:
```
https://YOUR_USERNAME.github.io/REPOSITORY_NAME/
```

The `base-url` in `_quarto.yml` must match your repository name (with a leading slash).

**Update `_quarto.yml`:**
```yaml
website:
  base-url: /YOUR_REPOSITORY_NAME
```

For example, if your repository is `FInDER_Lab_Website`, it should be:
```yaml
website:
  base-url: /FInDER_Lab_Website
```

### Step 3: Rebuild and Redeploy

After updating the base URL:

1. Commit the changes:
   ```bash
   git add _quarto.yml
   git commit -m "Fix base URL for GitHub Pages"
   git push
   ```

2. Wait for the GitHub Actions workflow to complete (2-5 minutes)

3. Try accessing your site again

### Step 4: Clear Browser Cache

Sometimes your browser caches the 404 page. Try:
- Hard refresh (Ctrl+F5 or Cmd+Shift+R)
- Incognito/Private browsing mode
- Different browser

### Step 5: Check File Structure

Verify that the built site contains an `index.html` file:
1. Go to Actions tab
2. Click on the latest successful workflow run
3. Check the "Upload artifact" step to see what files were uploaded

The `_site` directory should contain:
- `index.html`
- Other HTML files for your pages
- CSS, JS, and other assets

## Common Issues

### Bibliography Not Rendering

- Check GitHub Actions logs for R package installation errors
- Verify BibTeX syntax in `references.bib`
- Ensure R packages (`bibtex`, `RefManageR`) are available (they should be in the GitHub Actions environment)

### Site Not Updating After Push

- Wait 2-5 minutes for deployment
- Check Actions tab to ensure workflow ran
- Verify you pushed to the `main` branch
- Clear browser cache

### Build Failures

Common causes:
- Syntax errors in `.qmd` files
- Missing files referenced in configuration
- BibTeX formatting errors
- Missing dependencies

Check the Actions logs for specific error messages.

## Getting Help

If issues persist:
1. Check the GitHub Actions logs carefully
2. Review Quarto documentation: https://quarto.org/docs/websites/
3. Check GitHub Pages documentation: https://docs.github.com/en/pages
