import bpy

# -----------------------------------------------------------------------------
#    Keymaps (For Register)
# -----------------------------------------------------------------------------    

def neltulz_smart_sharpen_register_keymaps(addon_keymaps):

    #store window_manager as var for easier reference
    wm = bpy.context.window_manager

    #------------------------------Object Mode----------------------------------------------------------------------------

    #create new keymap
    km = wm.keyconfigs.addon.keymaps.new(name = "Object Mode", space_type="EMPTY")

    #create shortcuts for keymap
    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "ZERO", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 75
    
    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "NINE", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 65
  
    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "EIGHT", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 55
 
    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "SEVEN", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 45
  
    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "SIX", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 35

    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "FIVE", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 25

    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "FOUR", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 15

    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "THREE", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 5

    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "TWO", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 180
  
    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "ONE", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 0

    #add list of keymaps
    addon_keymaps.append(km)

    #------------------------------Mesh Mode----------------------------------------------------------------------------

    #create new keymap
    km = wm.keyconfigs.addon.keymaps.new(name = "Mesh", space_type="EMPTY")

    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "ZERO", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 75
  
    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "NINE", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 65

    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "EIGHT", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 55

    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "SEVEN", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 45

    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "SIX", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 35

    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "FIVE", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 25

    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "FOUR", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 15

    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "THREE", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 5

    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "TWO", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 180

    kmi = km.keymap_items.new("ntz_smrt_shrp.neltulz_smart_sharpen", type = "ONE", ctrl=True, shift=True, value = "PRESS")
    kmi.properties.degreesValue = 0

    #add list of keymaps
    addon_keymaps.append(km)


def neltulz_smart_sharpen_unregister_keymaps(addon_keymaps):
    # handle the keymap
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    # clear the list
    addon_keymaps.clear()