import bpy
from . properties import NeltulzSmartSharpen_IgnitProperties
from . import misc_functions

# -----------------------------------------------------------------------------
#    Reset settings
# -----------------------------------------------------------------------------    

class OBJECT_OT_NeltulzSmartSharpen_ResetSettings(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.neltulz_smart_sharpen_reset_settings"
    bl_label = "Neltulz - Smart Sharpen - Reset Settings"
    bl_description = "Reset Settings"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        
        if not context.scene.neltulzSmartSharpen.bUseAdvancedSettingsCheckbox:
            # Prevent infinite loop when unchecking "Use Advanced Settings" checkbox
            context.scene.neltulzSmartSharpen.bPreventAdvancedSettingsUpdate = True

        context.scene.neltulzSmartSharpen.bUseAdvancedSettingsCheckbox = False
        context.scene.neltulzSmartSharpen.bSmoothShadeCheckbox = True
        context.scene.neltulzSmartSharpen.bAutoSmoothCheckbox = True
        context.scene.neltulzSmartSharpen.bAutoSmoothSlider = 180
        context.scene.neltulzSmartSharpen.bDisableErrorPopupsCheckbox = True

        # Done resetting things, allow "Use Advanced Settings" to update the next time it is clicked
        context.scene.neltulzSmartSharpen.bPreventAdvancedSettingsUpdate = False

        return {'FINISHED'}
    # END execute()
# END Smart_Sharpen_Operator()