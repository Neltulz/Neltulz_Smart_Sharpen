import bpy        

# -----------------------------------------------------------------------------
#   Determine which mode is currently Selected (Vert, Edge, Face, etc)
#   Returned: (0=Multiple modes, 1=Vertice Mode, 2=Edge Mode, 3=Face Mode)
# -----------------------------------------------------------------------------

def getCurrentSelectMode(self, context):
    #Create empty list
    tempList = []

    #check current mesh select mode
    for bool in bpy.context.tool_settings.mesh_select_mode:
        tempList.append(bool)
    
    #convert list into a tuple
    tempTuple = tuple(tempList)

    currentSelectMode = int()

    
    if tempTuple == (True, False, False):       
        currentSelectMode = 1
    elif tempTuple == (False, True, False):
        currentSelectMode = 2
    elif tempTuple == (False, False, True):
        currentSelectMode = 3
    #else:
        #fail (defaults currentSelectMode to 0)

    return currentSelectMode
# END getCurrentSelectMode(self, context)

# -----------------------------------------------------------------------------
#   Automatically smooth shade, and auto smooth normals
# -----------------------------------------------------------------------------

def smoothShadeAndAutoSmoothNormals(self, context):
    
    scene = context.scene

    selObjs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']

    #Enable auto smooth
    for currentObject in selObjs:

        #Smooth shade mesh
        if self.smoothShadeObject:
            bpy.ops.object.shade_smooth()
        else:
            self.report({'WARNING'}, 'Smooth Shade Object" is unchecked.  This means your entire object is being flat shaded!  Please enable "Smooth Shade Object"')
            bpy.ops.object.shade_flat()

        
        currentObject.data.use_auto_smooth = self.autoSmoothNormals
    
        #Set auto smooth angle 
        if self.autoSmoothNormals:

            currentObject.data.auto_smooth_angle = self.autoSmoothAngle*(3.14159/180)

        else:
            self.report({'WARNING'}, '"Auto Smooth Normals" is disabled!  Please enable "Auto Smooth Normals" fom the "Neltulz - Smart Sharpen" Panel to see a result!' )

    '''
    else:#user did not specify any advanced settings
        
        #smooth shade the object
        bpy.ops.object.shade_smooth()

        #Enable auto smooth
        for currentObject in selObjs:
            currentObject.data.use_auto_smooth = self.autoSmoothNormals

            #set angle to 180 degrees
            currentObject.data.auto_smooth_angle = 180*(3.14159/180)
    '''



    
    
