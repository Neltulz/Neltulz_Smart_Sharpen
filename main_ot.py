import bpy
from . import misc_functions
from . import smart_sharpen_entire_obj
from . import smart_sharpen_selected

# -----------------------------------------------------------------------------
#    Smart Sharpen Operator
# -----------------------------------------------------------------------------    

class OBJECT_OT_NeltulzSmartSharpen(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.neltulz_smart_sharpen"
    bl_label = "Neltulz - Smart Sharpen"
    bl_description = "Context Aware Smart Sharpen"

    degreesValue: bpy.props.FloatProperty \
    (
        name="Degrees Value =",
        description="Degrees you would like to smart sharpen edges by",
        default=1,
        min = 0,
        max = 180
    )

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):

        print('---[INFO]---: --------------------------------------------------------------------------------')
        print('---[INFO]---: Neltulz - Smart Sharpen - Started')

        # -----------------------------------------------------------------------------
        #   Check whether user is in "Edit Mode" or "Object Mode"
        #   If "Object mode", things are simple.  If "Edit mode", lots of checks required
        # -----------------------------------------------------------------------------

        #store previousSelectMode (Needed for use later - DO NOT DELETE!)
        previousSelectMode = misc_functions.getCurrentSelectMode(self, context)

        if bpy.context.object.mode == "EDIT":
            
            print('---[INFO]---: "Edit mode" Detected')

            # -----------------------------------------------------------------------------
            #   Smooth Mesh & Set smoothing angle to 180 degrees. This ensures that auto
            #   smooth doesn't override marked sharp edges.
            # -----------------------------------------------------------------------------

            bpy.ops.object.mode_set(mode='OBJECT') #switch to object mode

            #Smooth mesh
            misc_functions.smoothShadeAndAutoSmoothNormals(self, context)

            bpy.ops.object.mode_set(mode='EDIT') #switch to edit mode

            # -----------------------------------------------------------------------------
            #    User is in Edit mode, some things must be checked before determining
            #    The next course of action.
            # -----------------------------------------------------------------------------

            sel_objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']

            
            for currentObj in sel_objs:

                bpy.ops.object.mode_set(mode='OBJECT') #switch to object mode

                bpy.ops.object.select_all(action='DESELECT')

                currentObj.select_set(True)
                bpy.context.view_layer.objects.active = currentObj
                
                bpy.ops.object.mode_set(mode='EDIT') #switch to edit mode

                #update current Object from edit mode
                currentObj.update_from_editmode()
                
                        

                #if user has multiple select modes enabled, then fail and prevent the script from doing anything further
                if misc_functions.getCurrentSelectMode(self, context) == 0:
                    print('---[ERROR]---: Multiple Select mode is unsupported.  Please select only one mode (Vertice, Edge, or Face')

                else:
                    
                    #print which selection mode is detected
                    if misc_functions.getCurrentSelectMode(self, context) == 1:
                        print('---[INFO]---: Vertice Select Mode" Detected')
                    elif misc_functions.getCurrentSelectMode(self, context) == 2:
                        print('---[INFO]---: Edge Select Mode" Detected')
                    else:
                        print('---[INFO]---: Face Select Mode" Detected')

                    #store a list of currently selected vertice indices
                    currentSel_vertIDs = set()
                    for v in currentObj.data.vertices:
                        if v.select:
                            currentSel_vertIDs.add(v.index)

                    #store a list of currently selected edge indices
                    currentSel_edgeIDs = set()
                    for e in currentObj.data.edges:
                        if e.select:
                            currentSel_edgeIDs.add(e.index)

                    #store a list of currently selected face indices
                    currentSel_faceIDs = set()
                    for f in currentObj.data.polygons:
                        if f.select:
                            currentSel_faceIDs.add(f.index)

                    #store a list of currently deselected edge indices 
                    currentDesel_edgeIDs = set()    
                    for e in currentObj.data.edges:
                        if not e.select:
                            currentDesel_edgeIDs.add(e.index)

                    #print the number of selected vertices, edges, and faces
                    numVerts_Selected = len( [v for v in currentObj.data.vertices if v.select] )
                    print('---[INFO]---: Detected ' + str(numVerts_Selected) + ' vertices selected')
                    
                    numEdges_Selected = len( [e for e in currentObj.data.edges if e.select] )
                    print('---[INFO]---: Detected ' + str(numEdges_Selected) + ' edges selected')
                    
                    numFaces_Selected = len( [f for f in currentObj.data.polygons if f.select] )
                    print('---[INFO]---: Detected ' + str(numFaces_Selected) + ' faces selected')

                    smart_sharpen_selected.execute(self, context, currentObj, currentSel_vertIDs, currentSel_edgeIDs, currentSel_faceIDs, currentDesel_edgeIDs)


                #Smart Sharpening Finished - Now we need to reselect all of the previously selected objects, and return to edit mode

                bpy.ops.object.mode_set(mode='OBJECT') #switch to object mode

                bpy.ops.object.select_all(action='DESELECT')

                for currentObj in sel_objs:
                    currentObj.select_set(True)

                bpy.ops.object.mode_set(mode='EDIT') #switch to edit mode

                
            
            
        elif bpy.context.object.mode == "OBJECT":

            #detect if something is selected
            if bpy.context.selected_objects:

                print('---[INFO]---: Object mode" Detected')

                #Smooth mesh
                misc_functions.smoothShadeAndAutoSmoothNormals(self, context)
                                
                #switch to Edit Mode
                bpy.ops.object.editmode_toggle()

                #switch to edge mode
                bpy.ops.mesh.select_mode(use_extend=False, use_expand=True, type='EDGE')
                
                smart_sharpen_entire_obj.execute(self, context)

                #Switch back to previous selection mode before selecting sharp edges
                if (previousSelectMode == 1):
                    bpy.ops.mesh.select_mode(use_extend=False, use_expand=True, type='VERT')
                elif (previousSelectMode == 3):
                    bpy.ops.mesh.select_mode(use_extend=False, use_expand=True, type='FACE')
                else:
                    pass

                #Deselect All
                bpy.ops.mesh.select_all(action='DESELECT')

                #switch back to object mode
                bpy.ops.object.editmode_toggle()

            else:
                print('---[ERROR]---: Please select an object before running the script!')

        else:
            print('---[ERROR]---: Unable to detect "object" or "edit" mode.  Canceling.')

        print('---[INFO]---:  ')
        print('---[INFO]---: Neltulz - Smart Sharpen - Finished')
        print('---[INFO]---: --------------------------------------------------------------------------------')

        return {'FINISHED'}
    # END execute()
# END Smart_Sharpen_Operator()