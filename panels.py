
import bpy



from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Operator,
                       AddonPreferences,
                       PropertyGroup,
                       )



bpy.types.Scene.bUseAdvancedSettingsCheckbox = BoolProperty(
    name="Use Advanced Options",
    description="Reveals advanced options.",
    default = False
    )

bpy.types.Scene.bSmoothShadeCheckbox = BoolProperty(
    name="Smooth Shade Object",
    description="Enables smooth shading on object.  Recommended (True) to guarantee smart sharpen result.",
    default = True
    )

bpy.types.Scene.bAutoSmoothCheckbox = BoolProperty(
    name="Auto Smooth Normals",
    description='Enables "Auto Smooth" on object normals.  Recommended (True) to guarantee smart sharpen result.',
    default = True
    )

bpy.types.Scene.bAutoSmoothSlider= FloatProperty(
    name="Auto Smooth Value",
    description='Value for "Auto Smooth Normals"  Recommended (180)',
    default = 180,
    min = 0,
    max = 180
    )

bpy.types.Scene.bDisableErrorPopupsCheckbox = BoolProperty(
    name="Disable Error Popups - I know what I'm doing.",
    description="I know what I'm doing",
    default = False
    )



class OBJECT_PT_NeltulzSmartSharpen(Panel):

    bl_idname = "object.neltulz_smart_sharpen_panel"
    bl_label = "Smart Sharpen v1.0.4"
    bl_category = "Neltulz - Smart Sharpen"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    



    def draw(self, context):

        layout = self.layout
        #scene = bpy.types.Scene
        scene = context.scene

        col = layout.column(align=True)
        
        col.label(text="Degrees (0 - 180)")

        col = layout.column()
        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="0 (Full Sharp)")
        op.degreesValue=0
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox

        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="5")
        op.degreesValue=5
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox

        op = row.operator('object.neltulz_smart_sharpen', text="95")
        op.degreesValue=85
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox
        

        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="15")
        op.degreesValue=15
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox

        op = row.operator('object.neltulz_smart_sharpen', text="105")
        op.degreesValue=105
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox
        

        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="25")
        op.degreesValue=25
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox

        op = row.operator('object.neltulz_smart_sharpen', text="115")
        op.degreesValue=115
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox
        

        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="35")
        op.degreesValue=35
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox

        op = row.operator('object.neltulz_smart_sharpen', text="125")
        op.degreesValue=125
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox
        

        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="45")
        op.degreesValue=45
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox

        op = row.operator('object.neltulz_smart_sharpen', text="135")
        op.degreesValue=135
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox
        

        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="55")
        op.degreesValue=55
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox

        op = row.operator('object.neltulz_smart_sharpen', text="145")
        op.degreesValue=145
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox
        

        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="65")
        op.degreesValue=65
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox

        op = row.operator('object.neltulz_smart_sharpen', text="155")
        op.degreesValue=155
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox
        

        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="75")
        op.degreesValue=75
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox

        op = row.operator('object.neltulz_smart_sharpen', text="165")
        op.degreesValue=165
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox
        

        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="85")
        op.degreesValue=85
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox

        op = row.operator('object.neltulz_smart_sharpen', text="175")
        op.degreesValue=175
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox

        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="180 (Full Soft)")
        op.degreesValue=180
        op.bUseAdvancedSettings=scene.bUseAdvancedSettingsCheckbox
        op.bSmoothShade=scene.bSmoothShadeCheckbox
        op.bAutoSmoothNormals=scene.bAutoSmoothCheckbox
        op.autoSmoothValue=scene.bAutoSmoothSlider
        op.bDisableErrorPopups=scene.bDisableErrorPopupsCheckbox


        # -----------------------------------------------------------------------------
        #   Use Advanced Settings Box
        # -----------------------------------------------------------------------------

        col = layout.column(align=True)
        row = col.row(align=True)
        col.prop(context.scene, "bUseAdvancedSettingsCheckbox", text="Use Advanced Settings" )

        if scene.bUseAdvancedSettingsCheckbox:

            boxAdvancedOptions = layout.box()
            boxAdvancedOptions.label(text="Advanced Settings:")

            col = boxAdvancedOptions.column(align=True)
            
            
            col.prop(context.scene, "bSmoothShadeCheckbox", text="Smooth Shade Object" )
            
            if scene.bSmoothShadeCheckbox:

                box = boxAdvancedOptions.box()
                box.prop(context.scene, "bAutoSmoothCheckbox", text="Auto Smooth Normals" )

                col = box.column()
                row = col.row(align=True)
                row.label(text="Angle")
                row.prop(context.scene, "bAutoSmoothSlider", text='')

                row.enabled = scene.bAutoSmoothCheckbox
            
            col = boxAdvancedOptions.column()
            row = col.row(align=True)
            
            col = boxAdvancedOptions.column()
            col.label(text="Mr. I'm a badass:")
            col.prop(context.scene, "bDisableErrorPopupsCheckbox", text="Disable Error Popups")

        #else:
            #reset advanced settings back to defaults
            #bpy.context.scene.bSmoothShadeCheckbox = True
            #bpy.context.scene.bAutoSmoothCheckbox = True
            #bpy.context.scene.bAutoSmoothSlider = 180
            #bpy.context.scene.bDisableErrorPopupsCheckbox = False
        
