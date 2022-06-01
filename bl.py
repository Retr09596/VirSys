import bpy

eve  = bpy.context.scene.eevee
# eve.use_overscan            = True # means comment, that line won't work unless you get rid of the first #
# eve.soft_shadows            = True
eve.use_ssr                 = True
eve.use_ssr_halfres         = True
eve.use_gtao                = True
eve.taa_render_samples      = 16
eve.gtao_distance           = 1.0