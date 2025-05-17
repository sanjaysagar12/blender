import bpy
import sys
import json

# Read JSON input (e.g., passed from command line)
args = json.loads(sys.argv[-1])

shape = args.get("shape", "cube")
size = float(args.get("size", 1))
export_path = args.get("export_path", "./tmp/model.glb")

# Reset Blender scene
bpy.ops.wm.read_factory_settings(use_empty=True)

# Create shape
if shape == "cube":
    bpy.ops.mesh.primitive_cube_add(size=size, location=(0, 0, 0))
elif shape == "sphere":
    bpy.ops.mesh.primitive_uv_sphere_add(radius=size, location=(0, 0, 0))
else:
    raise Exception("Unsupported shape")

# Export
bpy.ops.export_scene.gltf(filepath=export_path, export_format='GLB')
