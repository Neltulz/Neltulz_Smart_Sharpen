import bpy
from . import misc_functions
from . import smart_sharpen_entire_obj
from . import smart_sharpen_selected
from . import misc_layout

from bpy.props import (StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, EnumProperty, PointerProperty)

# -----------------------------------------------------------------------------
#    Smart Sharpen Operator
# -----------------------------------------------------------------------------    

class NTZSMSHRP_OT_smartsharpen(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "ntz_smrt_shrp.neltulz_smart_sharpen"
    bl_label = "Neltulz - Smart Sharpen"
    bl_description = "Context Aware Smart Sharpen"
    bl_options = {'REGISTER', 'UNDO'}

    degreesValue : FloatProperty (
        name="Degrees Value",
        description="Degrees you would like to smart sharpen edges by",
        default=1,
        min = 0,
        max = 180
    )

    showSmoothShadeObjectOptions : BoolProperty (
        name="Show Smooth Shade Object",
        description="Show Smooth Shade Object",
        default=False,
    )

    smoothShadeObject : BoolProperty (
        name="Smooth Shade Object",
        description="Smooth Shade Object",
        default=True,
    )

    autoSmoothNormals : BoolProperty (
        name="Auto Smooth Normals",
        description="Auto Smooth Normals",
        default=True,
    )

    autoSmoothAngle : FloatProperty (
        name="Auto Smooth Angle",
        description="Auto Smooth Angle",
        default=180,
        min = 0,
        max = 180,
    )

    

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

        
    def draw(self, context):

        layout = self.layout


        misc_layout.createProp(self, context, None, True, "Degrees", "degreesValue", 1, 4, 1, "RIGHT", "EXPAND", "", False, layout)
        
        layout.separator()

        smoothShadeOptions = layout.box()

        misc_layout.createShowHide(self, context, None, self, "showSmoothShadeObjectOptions", "smoothShadeObject", "Smooth Shade Object", smoothShadeOptions)

        if self.showSmoothShadeObjectOptions:
            row = smoothShadeOptions.row(align=True)
            spacer = row.column(align=True)
            spacer.ui_units_x = 1
            spacer.label(text="", icon="BLANK1")
            autoSmoothCol = row.column(align=True)


            misc_layout.createProp(self, context, None, True, None, "autoSmoothNormals", 1, 1, 1, "RIGHT", "EXPAND", None, False, autoSmoothCol)
            autoSmoothCol.separator()
            misc_layout.createProp(self, context, None, True, "Angle", "autoSmoothAngle", 1, 5, 1, "RIGHT", "EXPAND", "", False, autoSmoothCol)


    # END draw()

    def execute(self, context):

        selObjs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
        activeObj = bpy.context.view_layer.objects.active

        #If active object is not in the list of selected objects, then it needs to be added so that it can be smart sharpened.
        if activeObj is not None:
            if activeObj.type == 'MESH':
                if not activeObj in selObjs:
                    selObjs.append(activeObj)

        modeAtBegin = bpy.context.object.mode

        # -----------------------------------------------------------------------------
        #   Check whether user is in "Edit Mode" or "Object Mode"
        #   If "Object mode", things are simple.  If "Edit mode", lots of checks required
        # -----------------------------------------------------------------------------

        #store previousSelectMode (Needed for use later - DO NOT DELETE!)
        previousSelectMode = misc_functions.getCurrentSelectMode(self, context)

        if modeAtBegin == "EDIT":
        
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
            
            for obj in selObjs:

                bpy.ops.object.mode_set(mode='OBJECT') #switch to object mode

                bpy.ops.object.select_all(action='DESELECT')

                obj.select_set(True)
                bpy.context.view_layer.objects.active = obj #set current obj as active object
                
                bpy.ops.object.mode_set(mode='EDIT') #switch to edit mode                        

                #if user has multiple select modes enabled, then fail and prevent the script from doing anything further
                if misc_functions.getCurrentSelectMode(self, context) == 0:
                    self.report({'WARNING'}, 'Please select only one mode (Vertice, Edge, or Face')
                else:

                    #store a list of currently selected vertice indices
                    currentSel_vertIDs = set()
                    for v in obj.data.vertices:
                        if v.select:
                            currentSel_vertIDs.add(v.index)

                    #store a list of currently selected edge indices
                    currentSel_edgeIDs = set()
                    for e in obj.data.edges:
                        if e.select:
                            currentSel_edgeIDs.add(e.index)

                    #store a list of currently selected face indices
                    currentSel_faceIDs = set()
                    for f in obj.data.polygons:
                        if f.select:
                            currentSel_faceIDs.add(f.index)

                    #store a list of currently deselected edge indices 
                    currentDesel_edgeIDs = set()    
                    for e in obj.data.edges:
                        if not e.select:
                            currentDesel_edgeIDs.add(e.index)

                    #print the number of selected vertices, edges, and faces
                    numVerts_Selected = len( [v for v in obj.data.vertices if v.select] )
                    
                    numEdges_Selected = len( [e for e in obj.data.edges if e.select] )
                    
                    numFaces_Selected = len( [f for f in obj.data.polygons if f.select] )

                    smart_sharpen_selected.execute(self, context, obj, currentSel_vertIDs, currentSel_edgeIDs, currentSel_faceIDs, currentDesel_edgeIDs)


                #Smart Sharpening Finished - Now we need to reselect all of the previously selected objects, and return to edit mode

                bpy.ops.object.mode_set(mode='OBJECT') #switch to object mode

                bpy.ops.object.select_all(action='DESELECT')

                for obj in selObjs:
                    obj.select_set(True)

                bpy.ops.object.mode_set(mode='EDIT') #switch to edit mode

                
            
            
        elif modeAtBegin == "OBJECT":

            #detect if something is selected
            if bpy.context.selected_objects:


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
                self.report({'WARNING'}, 'Please select an object before running the script')

        else:
            self.report({'WARNING'}, 'Unable to detect "object" or "edit" mode.  Canceling')


        return {'FINISHED'}
    # END execute()
# END Smart_Sharpen_Operator()