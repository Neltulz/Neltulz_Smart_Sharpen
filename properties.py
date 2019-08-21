import bpy
from . import misc_functions

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Operator,
                       AddonPreferences,
                       PropertyGroup,
                       )


def resetSettings(self, context):
    if not self.bUseAdvancedSettingsCheckbox:
        if not self.bPreventAdvancedSettingsUpdate:

            bpy.ops.object.neltulz_smart_sharpen_reset_settings()




class NeltulzSmartSharpen_IgnitProperties(bpy.types.PropertyGroup):

    bUseAdvancedSettingsCheckbox : BoolProperty (
        name="Use Advanced Options",
        description="Reveals advanced options.",
        default = False,
        update=resetSettings
    )

    bPreventAdvancedSettingsUpdate : BoolProperty(
        name="Prevent advanced settings update",
        description="Prevents the advanced settings from updating and causing an infinite loop",
        default = False
    )

    bSmoothShadeCheckbox : BoolProperty(
        name="Smooth Shade Object",
        description="Enables smooth shading on object.  Recommended (True) to guarantee smart sharpen result.",
        default = True
    )

    bAutoSmoothCheckbox : BoolProperty(
        name="Auto Smooth Normals",
        description='Enables "Auto Smooth" on object normals.  Recommended (True) to guarantee smart sharpen result.',
        default = True
    )

    bAutoSmoothSlider : FloatProperty(
        name="Auto Smooth Value",
        description='Value for "Auto Smooth Normals"  Recommended (180)',
        default = 180,
        min = 0,
        max = 180
    )

    bDisableErrorPopupsCheckbox : BoolProperty(
        name="Disable Error Popups - I know what I'm doing.",
        description="I know what I'm doing",
        default = False
    )