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




class NTZSMSHRP_ignitproperties(bpy.types.PropertyGroup):

    bShowHideOptions : BoolProperty (
        name="Show/Hide Options",
        description="Reveals options.",
        default = False,
    )

    optionsPopoverEnum_List = [
        ("OPTIONS", "Options", "", "", 0),
    ]

    optionsPopoverEnum : EnumProperty (
        items       = optionsPopoverEnum_List,
        name        = "Options Popover Enum",
        description = "Options Popover Enum",
        default     = "OPTIONS"
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

    sharpEdgeDisplay_PopoverEnum_List = [
        ("SHARP_ENABLED",  "",  "", "SHARPCURVE", 0),
        ("SHARP_DISABLED", "", "", "SPHERECURVE", 1),
    ]

    sharpEdgeDisplay_PopoverEnum : EnumProperty (
        items       = sharpEdgeDisplay_PopoverEnum_List,
        name        = "Sharp Edge Popover Enum",
        description = "Sharp Edge Popover Enum",
        default     = "SHARP_ENABLED"
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