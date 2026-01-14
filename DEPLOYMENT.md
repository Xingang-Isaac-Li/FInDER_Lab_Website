# Deployment Guide: Publishing Your Lab Website to GitHub Pages

This guide walks you through pushing your website to GitHub and making it live online.

## Prerequisites

1. **Git** - If not installed, download from https://git-scm.com/downloads
2. **GitHub Account** - Create one at https://github.com if you don't have one

## Step-by-Step Instructions

### Step 1: Install Git (if needed)

1. Download Git from https://git-scm.com/downloads
2. Run the installer (use default settings)
3. Restart your terminal/command prompt after installation
4. Verify installation by running: `git --version`

### Step 2: Initialize Git Repository

Open a terminal/command prompt in your project directory and run:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Lab website setup"
```

### Step 3: Create GitHub Repository

1. Go to https://github.com and sign in
2. Click the **"+"** icon in the top right → **"New repository"**
3. Fill in:
   - **Repository name**: `FInDER_Lab_Website` (or your preferred name)
   - **Description**: "Research lab website built with Quarto"
   - **Visibility**: Choose **Public** (required for free GitHub Pages) or **Private** (requires GitHub Pro)
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
4. Click **"Create repository"**

### Step 4: Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands. Use these (replace `YOUR_USERNAME` with your GitHub username):

```bash
# Add remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/FInDER_Lab_Website.git

# Rename branch to 'main' if needed (GitHub uses 'main' by default)
git branch -M main

# Push to GitHub
git push -u origin main
```

You'll be prompted for your GitHub username and password. For password, use a **Personal Access Token** (see below).

### Step 5: Create GitHub Personal Access Token (for authentication)

Since GitHub no longer accepts passwords, you need a Personal Access Token:

1. Go to https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Give it a name (e.g., "Lab Website Deployment")
4. Select scopes: check **"repo"** (this gives full control)
5. Click **"Generate token"**
6. **Copy the token immediately** (you won't see it again!)
7. Use this token as your password when pushing to GitHub

### Step 6: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top menu)
3. Click **Pages** (left sidebar)
4. Under **"Source"**, select **"GitHub Actions"** (not "Deploy from a branch")
5. The page will save automatically

### Step 7: Trigger the GitHub Actions Workflow

1. Go to the **Actions** tab in your repository
2. You should see the workflow running (it may take a few minutes)
3. Once complete, go back to **Settings → Pages**
4. Your site URL will be displayed: `https://YOUR_USERNAME.github.io/FInDER_Lab_Website/`

## Making Future Updates

After the initial setup, updating your site is simple:

```bash
# Make changes to your files
# Then:

git add .
git commit -m "Update website content"
git push
```

GitHub Actions will automatically rebuild and redeploy your site within a few minutes.

## Troubleshooting

### Git not found
- Make sure Git is installed and in your PATH
- Restart your terminal after installation
- On Windows, try using Git Bash instead of PowerShell

### Authentication errors
- Make sure you're using a Personal Access Token, not your password
- Tokens expire - generate a new one if needed
- Consider using GitHub Desktop (GUI tool) as an alternative

### Workflow fails
- Check the **Actions** tab for error messages
- Common issues:
  - Syntax errors in `.qmd` files
  - Missing files referenced in configuration
  - BibTeX formatting errors in `references.bib`

### Site not updating
- Wait a few minutes (deployment takes 2-5 minutes)
- Check Actions tab to see if workflow completed
- Clear browser cache
- Verify GitHub Pages source is set to "GitHub Actions"

## Alternative: Using GitHub Desktop

If you prefer a graphical interface:

1. Download GitHub Desktop from https://desktop.github.com
2. Sign in with your GitHub account
3. Click **File → Add Local Repository**
4. Select your project folder
5. Click **Publish repository** to push to GitHub
6. Follow Step 6-7 above to enable GitHub Pages

## Your Site URL

Once deployed, your site will be available at:
```
https://YOUR_USERNAME.github.io/FInDER_Lab_Website/
```

Replace `YOUR_USERNAME` with your actual GitHub username and `FInDER_Lab_Website` with your repository name.
