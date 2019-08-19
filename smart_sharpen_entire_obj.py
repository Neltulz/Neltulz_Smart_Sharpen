import bpy

from . import misc_functions

# -----------------------------------------------------------------------------
#    Smart Sharpen Entire Object   
# ----------------------------------------------------------------------------- 

def execute(self, context):


    #Select All
    bpy.ops.mesh.select_all(action='SELECT')

    #clear sharp
    bpy.ops.mesh.mark_sharp(clear=True)



    if self.degreesValue <= 0:
        #mark sharp
        bpy.ops.mesh.mark_sharp()

        misc_functions.neltulzPrint(self, context, 'INFO', 'Entire object was sharpened')

    elif self.degreesValue >= 180:
        #do nothing, all sharp edges were already cleared prior to this!

        misc_functions.neltulzPrint(self, context, 'INFO', 'Entire object was softened')

    else:
        #Deselect All
        bpy.ops.mesh.select_all(action='DESELECT')

        #Select Sharp Edges matching degreesValue
        sharpnessValue = self.degreesValue*(3.14159/180)
        bpy.ops.mesh.edges_select_sharp( sharpness=sharpnessValue )


        misc_functions.neltulzPrint(self, context, 'INFO', 'Selected sharp edges by ' + str(self.degreesValue) + 'deg (' + str(sharpnessValue) + ') and sharpened')

        #mark sharp
        bpy.ops.mesh.mark_sharp()
# END smart_sharp_entire_obj()