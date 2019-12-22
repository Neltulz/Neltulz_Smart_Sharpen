import bpy

from . import misc_functions

# -----------------------------------------------------------------------------
#    Smart Sharpen Selected
# -----------------------------------------------------------------------------

def execute(self, context, currentObj, currentSel_vertIDs, currentSel_edgeIDs, currentSel_faceIDs, currentDesel_edgeIDs):

    if self.degreesValue <= 0:
        #if current select mode is vertice, use verts when marking sharp, otherwise sharpen normally
        if misc_functions.getCurrentSelectMode(self, context) == 1:
            bpy.ops.mesh.mark_sharp(use_verts=True)
        else:
            bpy.ops.mesh.mark_sharp(use_verts=False)
        
    elif self.degreesValue >= 180:
        #if current select mode is vertice, use verts when marking soft, otherwise soften normally
        if misc_functions.getCurrentSelectMode(self, context) == 1:
            bpy.ops.mesh.mark_sharp(clear=True, use_verts=True)
        else:
            bpy.ops.mesh.mark_sharp(clear=True, use_verts=False)
    else:

        

        #clear sharp
        bpy.ops.mesh.mark_sharp(clear=True, use_verts=False)

        #Deselect All
        bpy.ops.mesh.select_all(action='DESELECT')
        
        #store previousSelectMode (Needed for use later - DO NOT DELETE!)
        previousSelectMode = misc_functions.getCurrentSelectMode(self, context)

        #Switch back to edge selection mode before selecting sharp edges
        if (misc_functions.getCurrentSelectMode(self, context) == 1) or (misc_functions.getCurrentSelectMode(self, context) == 3):
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=True, type='EDGE')
        
        
        




        #Select Sharp Edges matching degreesValue
        sharpnessValue = self.degreesValue*(3.14159/180)
        bpy.ops.mesh.edges_select_sharp(sharpness=sharpnessValue)

        #switch back to object mode and then back to edit mode to force viewport update
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.editmode_toggle()

        #Update mesh data from edit mode
        currentObj.update_from_editmode()




        #store a list of currently selected sharp edge indices
        currentSelectionSharpEdgeIndices = set()
        for e in currentObj.data.edges:
            if e.select:
                currentSelectionSharpEdgeIndices.add(e.index)

        sharpEdgesWithoutDeselectedIndices = currentSelectionSharpEdgeIndices - currentDesel_edgeIDs


        
        #Deselect All
        bpy.ops.mesh.select_all(action='DESELECT')



        #switch to Object Mode
        bpy.ops.object.editmode_toggle()


        #Select all sharp edges, minus the deselected edges
        for edge in sharpEdgesWithoutDeselectedIndices:
            currentObj.data.edges[edge].select=True

        #switch to Edit Mode
        bpy.ops.object.editmode_toggle()





        #Mark Edges are Sharp
        bpy.ops.mesh.mark_sharp(clear=False, use_verts=False)

        #Switch back to previous selection mode before selecting sharp edges
        if (previousSelectMode == 1):
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=True, type='VERT')
        elif (previousSelectMode == 3):
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=True, type='FACE')
        #else:
            #donothing


        #Deselect All
        bpy.ops.mesh.select_all(action='DESELECT')

        #switch to Object Mode
        bpy.ops.object.editmode_toggle()

        if (previousSelectMode == 1):
            #Select all previously selected vertices
            for vert in currentSel_vertIDs:
                currentObj.data.vertices[vert].select=True
        elif (previousSelectMode == 2):
            #Select all previously selected edges
            for edge in currentSel_edgeIDs:
                currentObj.data.edges[edge].select=True
        else:
            #Select all previously selected faces
            for face in currentSel_faceIDs:
                currentObj.data.polygons[face].select=True


        #switch to Edit Mode
        bpy.ops.object.editmode_toggle()
# END smart_sharp_selected()
