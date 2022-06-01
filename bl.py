import bpy

for scene in bpy.data.scenes:
    scene.render.engine = 'BLENDER_EEVEE'

bpy.context.scene.eevee.taa_render_samples = 2048

bpy.ops.render.render(animation=False, write_still=True)