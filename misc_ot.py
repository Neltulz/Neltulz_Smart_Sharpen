import bpy
from . properties import NTZSMSHRP_ignitproperties
from . import misc_functions

# -----------------------------------------------------------------------------
#    Reset settings
# -----------------------------------------------------------------------------    

class NTZSMSHRP_OT_resetallsettings(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "ntz_smrt_shrp.reset_settings"
    bl_label = "Neltulz - Smart Sharpen : Reset Settings"
    bl_description = "Reset Settings"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):

        context.scene.neltulzSmartSharpen.smoothShadeObject = "SMOOTH"
        context.scene.neltulzSmartSharpen.bAutoSmoothCheckbox = True
        context.scene.neltulzSmartSharpen.bAutoSmoothSlider = 180

        return {'FINISHED'}
    # END execute()
# END Smart_Sharpen_Operator()