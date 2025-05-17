# Blender GLB Generator and Viewer

This project allows users to generate 3D models (GLB format) using Blender via a Flask backend, and view them interactively in a React frontend.

## Prerequisites
- [Blender](https://www.blender.org/download/) installed and available in your system PATH
- Python 3.x
- Node.js and npm (for React frontend)

## Backend Setup (Flask)
1. Install Python dependencies:
   ```bash
   pip install flask flask-cors
   ```
2. Ensure `generate_model.py` exists in the backend directory and is configured to generate models based on input JSON.
3. Create a `models` directory in the backend root:
   ```bash
   mkdir models
   ```
4. Run the Flask server:
   ```bash
   python api.py
   ```
   The backend will be available at `http://localhost:5000`.

## Frontend Setup (React)
1. Navigate to the React app directory:
   ```bash
   cd render
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the React development server:
   ```bash
   npm run dev
   ```
   The frontend will be available at `http://localhost:5173`.

## Usage
1. Enter the desired shape (e.g., `sphere`, `cube`) and size in the input fields.
2. Click the "Generate GLB" button.
3. The generated model will be displayed in the viewer once ready.

## Example API Usage
- **POST** `/generate-glb`
  - Body: `{ "shape": "sphere", "size": 2 }`
  - Response: `{ "uuid": "<file_uuid>" }`
- **GET** `/get-glb/<file_uuid>`
  - Downloads the generated GLB file.

## Notes
- Ensure Blender is installed and accessible from the command line.
- The backend must be running for the frontend to generate and fetch models.
