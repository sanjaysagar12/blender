from flask import Flask, request, send_file
from flask_cors import CORS
import subprocess
import json
import uuid
import os
import shutil

app = Flask(__name__)
CORS(app)

@app.route('/generate-glb', methods=['POST'])
def generate_glb():
    if shutil.which("blender") is None:
        return {"error": "Blender executable not found. Please ensure Blender is installed and in your PATH."}, 500

    data = request.json
    shape = data.get('shape', 'cube')
    size = data.get('size', 1)

    file_uuid = uuid.uuid4().hex
    output_file = f"./models/{file_uuid}.glb"
    blender_script = os.path.abspath("generate_model.py")

    args = json.dumps({
        "shape": shape,
        "size": size,
        "export_path": output_file
    })
    command = [
        "blender", "--background", "--python", blender_script, "--", args
    ]
    subprocess.run(command, check=True)

    return {"uuid": file_uuid}

@app.route('/get-glb/<file_uuid>', methods=['GET'])
def get_glb(file_uuid):
    file_path = f"./models/{file_uuid}.glb"
    if not os.path.exists(file_path):
        return {"error": "File not found"}, 404
    return send_file(file_path, as_attachment=True, download_name="model.glb")

if __name__ == '__main__':
    app.run(debug=True)
