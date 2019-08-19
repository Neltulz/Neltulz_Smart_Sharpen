bl_info = {
    "name" : "Neltulz - Smart Sharpen",
    "author" : "Neil V. Moore",
    "description" : "Context Aware Smart Sharpen",
    "blender" : (2, 80, 0),
    "version" : (1, 0, 4),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

# -----------------------------------------------------------------------------
#   Import Classes and/or functions     
# -----------------------------------------------------------------------------  

import bpy

from . main_ot import OBJECT_OT_NeltulzSmartSharpen
from . panels import OBJECT_PT_NeltulzSmartSharpen
from . import keymaps

PendingDeprecationWarning


# -----------------------------------------------------------------------------
#    Store classes in List so that they can be easily registered/unregistered    
# -----------------------------------------------------------------------------  

classes = (
    OBJECT_OT_NeltulzSmartSharpen,
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

    #add keymaps from keymaps.py
    keymaps.neltulz_smart_sharpen_register_keymaps(addon_keymaps)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    #remove keymaps from keymaps.py
    keymaps.neltulz_smart_sharpen_unregister_keymaps(addon_keymaps)


#if __name__ == "__main__":
    #register()

    # test call
    #bpy.ops.object.neltulz_smart_sharpen_main_ot()