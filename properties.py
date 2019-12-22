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

            bpy.ops.ntz_smrt_shrp.reset_settings()




class NeltulzSmartSharpen_IgnitProperties(bpy.types.PropertyGroup):

    bShowHideOptions : BoolProperty (
        name="Show/Hide Options",
        description="Reveals options.",
        default = False,
    )

    bPreventAdvancedSettingsUpdate : BoolProperty(
        name="Prevent advanced settings update",
        description="Prevents the advanced settings from updating and causing an infinite loop",
        default = False
    )

    smoothShadeObject_List = [
        ("UNSET",      "Unset (Use last known)",  "", 0),
        ("SMOOTH",     "Yes",    "", 1),
        ("NO_SMOOTH",  "No",     "", 2),
    ]

    smoothShadeObject : EnumProperty (
        items       = smoothShadeObject_List,
        name        = "Smooth Shade Object",
        description = "Whether to smooth shade object or not",
        default     = "SMOOTH"
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