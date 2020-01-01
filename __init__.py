bl_info = {
    "name" : "Neltulz - Smart Sharpen",
    "author" : "Neil V. Moore",
    "description" : "Context Aware Smart Sharpen",
    "blender" : (2, 80, 0),
    "version" : (1, 0, 10),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

# -----------------------------------------------------------------------------
#   Import Classes and/or functions     
# -----------------------------------------------------------------------------  

import bpy

from . properties           import NTZSMSHRP_ignitproperties
from . main_ot              import NTZSMSHRP_OT_smartsharpen
from . misc_ot              import NTZSMSHRP_OT_resetallsettings
from . addon_preferences    import NTZSMSHRP_OT_addonprefs
from . panels               import NTZSMSHRP_PT_edgedisplayoptions
from . panels               import NTZSMSRHP_PT_options
from . panels               import NTZSMSRHP_PT_additionaldegreescompact
from . panels               import NTZSMSHRP_PT_sidebarpanel

from . import keymaps

PendingDeprecationWarning


# -----------------------------------------------------------------------------
#    Store classes in List so that they can be easily registered/unregistered    
# -----------------------------------------------------------------------------  

classes = (
    NTZSMSHRP_ignitproperties,
    NTZSMSHRP_OT_resetallsettings,
    NTZSMSHRP_OT_smartsharpen,
    NTZSMSHRP_OT_addonprefs,
    NTZSMSHRP_PT_edgedisplayoptions,
    NTZSMSRHP_PT_options,
    NTZSMSRHP_PT_additionaldegreescompact,
    NTZSMSHRP_PT_sidebarpanel,
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
    prefs = bpy.context.preferences.addons[__name__].preferences
    addon_preferences.update_panel(prefs, bpy.context)

    #add keymaps from keymaps.py
    keymaps.neltulz_smart_sharpen_register_keymaps(addon_keymaps)

    #add property group to the scene
    bpy.types.Scene.neltulzSmartSharpen = bpy.props.PointerProperty(type=NTZSMSHRP_ignitproperties)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

    #remove keymaps from keymaps.py
    keymaps.neltulz_smart_sharpen_unregister_keymaps(addon_keymaps)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.ntz_smrt_shrp.neltulz_smart_sharpen()