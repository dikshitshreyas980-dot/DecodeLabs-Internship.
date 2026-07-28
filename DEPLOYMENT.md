# Deployment Guide

This project is configured to be easily deployed to **Netlify** (Frontend) and **Render** (Backend).

## 1. GitHub Setup
1. Initialize git: `git init`
2. Add files: `git add .`
3. Commit: `git commit -m "Initial commit"`
4. Push to your GitHub repository.

## 2. Backend Deployment (Render)
1. Log into Render (render.com).
2. Create a new **Web Service**.
3. Connect your GitHub repository.
4. Render will automatically detect the `render.yaml` configuration in the root directory.
5. Alternatively, configure manually:
   - Build Command: `pip install -r backend/requirements.txt`
   - Start Command: `cd backend && gunicorn app:create_app()`
6. Copy the deployed backend URL (e.g., `https://decodebot-backend.onrender.com`).

## 3. Frontend Deployment (Netlify)
1. Log into Netlify (netlify.com).
2. Click **Add new site** -> **Import an existing project**.
3. Connect your GitHub repository.
4. Netlify will detect the `netlify.toml` file.
5. **IMPORTANT:** Go to Environment Variables and add:
   - Key: `VITE_API_URL`
   - Value: `[Your Render Backend URL]/api`
6. Deploy site.
