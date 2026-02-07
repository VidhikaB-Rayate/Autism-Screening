# How to Deploy Your Autism Screening App

To access your website from anywhere, we will deploy it to **Render.com**. It's a free and reliable cloud platform.

## Prerequisites
1.  **GitHub Account**: [Sign up here](https://github.com/) if you don't have one.
2.  **Render Account**: [Sign up here](https://render.com/) (log in with your GitHub account).
3.  **Git Installed**: Ensure you have Git installed on your computer.

---

## Step 1: Upload Your Code to GitHub

We need to put your code online so Render can access it.

1.  Open your project folder (`e:\Degree_txt_books\SEM-6\project`) in a terminal (Command Prompt or PowerShell).
2.  Run these commands one by one:
    ```powershell
    # Initialize a new git repository
    git init
    
    # Add all files to the repository
    git add .
    
    # Commit the changes
    git commit -m "Initial commit for deployment"
    ```
3.  **Create a New Repository on GitHub**:
    *   Go to [GitHub.com](https://github.com/new).
    *   Name it `autism-screening-app`.
    *   Keep it **Public** (easier) or Private.
    *   Click **Create repository**.
4.  **Link and Push**:
    *   Copy the commands under "...or push an existing repository from the command line" shown on GitHub. They will look like this (replace `YOUR_USERNAME`):
    ```powershell
    git remote add origin https://github.com/YOUR_USERNAME/autism-screening-app.git
    git branch -M main
    git push -u origin main
    ```

---

## Step 2: Deploy to Render

1.  Go to your [Render Dashboard](https://dashboard.render.com/).
2.  Click **New +** -> **Web Service**.
3.  Select **Build and deploy from a Git repository**.
4.  Connect your GitHub account if asked, then select your `autism-screening-app` repository.
5.  **Configure the Service**:
    *   **Name**: `autism-screening` (or anything you like).
    *   **Region**: Closest to you (e.g., Singapore or Frankfurt).
    *   **Branch**: `main`.
    *   **Runtime**: `Python 3`.
    *   **Build Command**: `pip install -r backend/requirements.txt`
    *   **Start Command**: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
    *   **Instance Type**: `Free`.
6.  Click **Create Web Service**.

## Step 3: Wait & Access

Render will now download your code and install the dependencies. This might take 2-5 minutes.
*   Watch the logs. Once it says "Your service is live", click the link at the top (e.g., `https://autism-screening.onrender.com`).
*   **Share this link!** Anyone can now access your app.

---

## Troubleshooting

*   **Build Failed?** Check the logs. Did `pip install` fail?
    *   *Solution*: Ensure `backend/requirements.txt` is committed and exists.
*   **"Internal Server Error"?**
    *   *Solution*: Check the "Logs" tab in Render for Python errors.
