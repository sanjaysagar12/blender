import bpy
import sys
import json

# Read JSON input (e.g., passed from command line)
args = json.loads(sys.argv[-1])

shape = args.get("shape", "cube")
size = float(args.get("size", 1))
speed = float(args.get("speed", 1.0))
duration = int(60 / speed)
export_path = args.get("export_path", "./tmp/model.glb")

# Reset Blender scene
bpy.ops.wm.read_factory_settings(use_empty=True)

# Create shape
if shape == "cube":
    bpy.ops.mesh.primitive_cube_add(size=size, location=(0, 0, 0))
    obj = bpy.context.active_object
elif shape == "sphere":
    bpy.ops.mesh.primitive_uv_sphere_add(radius=size, location=(0, 0, 0))
    obj = bpy.context.active_object
else:
    raise Exception("Unsupported shape")

# Add simple rotation animation
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = duration
obj.rotation_euler = (0, 0, 0)
obj.keyframe_insert(data_path="rotation_euler", frame=1)
obj.rotation_euler = (0, 0, 6.28319)  # 360 degrees in radians
obj.keyframe_insert(data_path="rotation_euler", frame=duration)

# Export
bpy.ops.export_scene.gltf(filepath=export_path, export_format='GLB')
