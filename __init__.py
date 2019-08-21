bl_info = {
    "name" : "Neltulz - Smart Sharpen",
    "author" : "Neil V. Moore",
    "description" : "Context Aware Smart Sharpen",
    "blender" : (2, 80, 0),
    "version" : (1, 0, 5),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

# -----------------------------------------------------------------------------
#   Import Classes and/or functions     
# -----------------------------------------------------------------------------  

import bpy

from . properties import NeltulzSmartSharpen_IgnitProperties
from . main_ot import OBJECT_OT_NeltulzSmartSharpen
from . misc_ot import OBJECT_OT_NeltulzSmartSharpen_ResetSettings
from . addon_preferences import OBJECT_OT_NeltulzSubD_Preferences
from . panels import OBJECT_PT_NeltulzSmartSharpen
from . import keymaps

PendingDeprecationWarning


# -----------------------------------------------------------------------------
#    Store classes in List so that they can be easily registered/unregistered    
# -----------------------------------------------------------------------------  

classes = (
    NeltulzSmartSharpen_IgnitProperties,
    OBJECT_OT_NeltulzSmartSharpen_ResetSettings,
    OBJECT_OT_NeltulzSmartSharpen,
    OBJECT_OT_NeltulzSubD_Preferences,
    OBJECT_PT_NeltulzSmartSharpen,
)

# -----------------------------------------------------------------------------
#    Register classes from the classes list
# -----------------------------------------------------------------------------    

addon_keymaps = []

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    # update panel name
    addon_preferences.update_panel(None, bpy.context)

    #add keymaps from keymaps.py
    keymaps.neltulz_smart_sharpen_register_keymaps(addon_keymaps)

    #add property group to the scene
    bpy.types.Scene.neltulzSmartSharpen = bpy.props.PointerProperty(type=NeltulzSmartSharpen_IgnitProperties)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    #remove keymaps from keymaps.py
    keymaps.neltulz_smart_sharpen_unregister_keymaps(addon_keymaps)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.neltulz_smart_sharpen()