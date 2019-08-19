import bpy

# -----------------------------------------------------------------------------
#   NeltulzPrint - prints to console & self.reports at the same time!
# -----------------------------------------------------------------------------

def neltulzPrint(self, context, messageType, logMessage):
    #accepted messageTypes: DEBUG, INFO, OPERATOR, PROPERTY, WARNING, ERROR, ERROR_INVALID_INPUT, ERROR_INVALID_CONTEXT, ERROR_OUT_OF_MEMORY
    print('---[' + messageType + ']---: ' + logMessage)

    def errorPopup(self, context):
        messageLogPrepend = ''
        if messageType == 'ERROR':
            messageLogPrepend = '[NELTULZ - SMART SHARPEN - ERROR]: '
        self.report({'' + messageType + ''}, messageLogPrepend + logMessage)

    #if user is using advanced settings in the panel
    if self.bUseAdvancedSettings:

        #if user has popups disabled in the panel
        if self.bDisableErrorPopups:
            pass
        else:
            errorPopup(self, context)

    else:
        errorPopup(self, context)
        

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

    if self.bUseAdvancedSettings:
        #Smooth shade mesh
        if self.bSmoothShade:
            bpy.ops.object.shade_smooth()
            neltulzPrint(self, context, 'INFO', 'Smooth shaded object')
        else:
            neltulzPrint(self, context, 'ERROR', '"Smooth Shade Object" is unchecked.  This means your entire object is being flat shaded!  Please enable "Smooth Shade Object"!')
            bpy.ops.object.shade_flat()

        #Enable auto smooth
        bpy.context.object.data.use_auto_smooth = self.bAutoSmoothNormals
        
        #Set auto smooth angle 
        if self.bAutoSmoothNormals:

            neltulzPrint(self, context, 'INFO', '"Auto Smooth Normals" Enabled')

            bpy.context.object.data.auto_smooth_angle = self.autoSmoothValue*(3.14159/180)
            
            if self.autoSmoothValue >= 89.9:
                neltulzPrint(self, context, 'INFO', '"Auto Smooth Normals" Angle is ' + str(self.autoSmoothValue) + '.  This is good!')

            elif self.autoSmoothValue >= 45:
                neltulzPrint(self, context, 'WARNING', '"Auto Smooth Normals" Angle is ' + str(self.autoSmoothValue) + '.  This is okay. Recommend changing this value to at least 89.9 for better results')

            elif self.autoSmoothValue >= 30:
                neltulzPrint(self, context, 'ERROR', '"Auto Smooth Normals" Angle is ' + str(self.autoSmoothValue) + '.  This is NOT a good value. Recommend changing this value to at least 89.9 for better results')

            elif self.autoSmoothValue > 1:
                neltulzPrint(self, context, 'ERROR', '"Auto Smooth Normals" Angle is ' + str(self.autoSmoothValue) + '.  This is VERY BAD. Recommend changing this value to at least 89.9 for better results')

            else:
                neltulzPrint(self, context, 'ERROR', '"Auto Smooth Normals" Angle is ' + str(self.autoSmoothValue) + '.  This is HORRIBLE.  You will see a nearly fully sharpened object. Recommend changing this value to at least 89.9 for better results')


        else:
            neltulzPrint(self, context, 'ERROR', '"Auto Smooth Normals" is disabled!  Please enable "Auto Smooth Normals" fom the "Neltulz - Smart Sharpen" Panel to see a result!')

    else:#user did not specify any advanced settings
        
        #smooth shade the object
        bpy.ops.object.shade_smooth()
        neltulzPrint(self, context, 'INFO', 'Smooth shaded object')

        #Enable auto smooth
        bpy.context.object.data.use_auto_smooth = self.bAutoSmoothNormals

        #set angle to 180 degrees
        bpy.context.object.data.auto_smooth_angle = 180*(3.14159/180)
        neltulzPrint(self, context, 'INFO', '"Auto Smooth Normals" Angle is 180.  This is good!')



    
    
