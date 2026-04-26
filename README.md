# EcoAI Website

An AI-powered waste classification website.

## Local Development

Due to browser security (CORS), you cannot open `classify.html` directly. You must use a local server.

1. **Using Python (Quickest)**:
   ```bash
   python3 -m http.server 8000
   ```
   Then open [http://localhost:8000](http://localhost:8000)

2. **Using Node/NPM**:
   ```bash
   npm install
   npm start
   ```
   Then open [http://localhost:3000](http://localhost:3000)

## Deployment to Vercel

1. Push this folder to a GitHub repository.
2. Go to [Vercel](https://vercel.com) and "Import Project".
3. Vercel will detect the static files and deploy them automatically.

## How it Works
The classifier uses **TensorFlow.js** and a **Teachable Machine** model located in the `model/` folder to identify waste categories (Recyclable, Organic, Non-Recyclable, Hazard).
