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

    elif self.degreesValue >= 180:
        #do nothing, all sharp edges were already cleared prior to this!
        pass

    else:
        #Deselect All
        bpy.ops.mesh.select_all(action='DESELECT')

        #Select Sharp Edges matching degreesValue
        sharpnessValue = self.degreesValue*(3.14159/180)
        bpy.ops.mesh.edges_select_sharp( sharpness=sharpnessValue )

        #mark sharp
        bpy.ops.mesh.mark_sharp()
# END smart_sharp_entire_obj()