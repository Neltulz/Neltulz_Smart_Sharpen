
import bpy
from . properties import NeltulzSmartSharpen_IgnitProperties


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






class OBJECT_PT_NeltulzSmartSharpen(Panel):

    bl_idname = "object.neltulz_smart_sharpen_panel"
    bl_label = "Smart Sharpen v1.0.5"
    bl_category = "Smart Sharpen"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    



    def draw(self, context):

        layout = self.layout
        scene = context.scene

        col = layout.column(align=True)
        
        col.label(text="Degrees (0 - 180)")

        col = layout.column()
        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="0 (Full Sharp)")
        op.degreesValue=0
        
        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="5")
        op.degreesValue=5
        
        op = row.operator('object.neltulz_smart_sharpen', text="95")
        op.degreesValue=85
        
        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="15")
        op.degreesValue=15
        
        op = row.operator('object.neltulz_smart_sharpen', text="105")
        op.degreesValue=105
        
        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="25")
        op.degreesValue=25
        
        op = row.operator('object.neltulz_smart_sharpen', text="115")
        op.degreesValue=115
        
        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="35")
        op.degreesValue=35
        
        op = row.operator('object.neltulz_smart_sharpen', text="125")
        op.degreesValue=125
        
        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="45")
        op.degreesValue=45
        
        op = row.operator('object.neltulz_smart_sharpen', text="135")
        op.degreesValue=135
        
        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="55")
        op.degreesValue=55
        
        op = row.operator('object.neltulz_smart_sharpen', text="145")
        op.degreesValue=145
        
        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="65")
        op.degreesValue=65
        
        op = row.operator('object.neltulz_smart_sharpen', text="155")
        op.degreesValue=155
        
        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="75")
        op.degreesValue=75
        
        op = row.operator('object.neltulz_smart_sharpen', text="165")
        op.degreesValue=165
        
        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="85")
        op.degreesValue=85
        
        op = row.operator('object.neltulz_smart_sharpen', text="175")
        op.degreesValue=175
        
        row = col.row(align=True)
        op = row.operator('object.neltulz_smart_sharpen', text="180 (Full Soft)")
        op.degreesValue=180
        

        # -----------------------------------------------------------------------------
        #   Use Advanced Settings Box
        # -----------------------------------------------------------------------------

        col = layout.column(align=True)
        row = col.row(align=True)
        col.prop(scene.neltulzSmartSharpen, "bUseAdvancedSettingsCheckbox", text="Use Advanced Settings" )

        if scene.neltulzSmartSharpen.bUseAdvancedSettingsCheckbox:

            boxAdvancedOptions = layout.box()
            boxAdvancedOptions.label(text="Advanced Settings:")

            col = boxAdvancedOptions.column(align=True)
            
            
            col.prop(scene.neltulzSmartSharpen, "bSmoothShadeCheckbox", text="Smooth Shade Object" )
            
            if scene.neltulzSmartSharpen.bSmoothShadeCheckbox:

                box = boxAdvancedOptions.box()
                box.prop(scene.neltulzSmartSharpen, "bAutoSmoothCheckbox", text="Auto Smooth Normals" )

                col = box.column()
                row = col.row(align=True)
                row.label(text="Angle")
                row.prop(scene.neltulzSmartSharpen, "bAutoSmoothSlider", text='')

                row.enabled = scene.neltulzSmartSharpen.bAutoSmoothCheckbox
            
            col = boxAdvancedOptions.column()
            row = col.row(align=True)
            
            col = boxAdvancedOptions.column()
            col.label(text="Mr. I'm a badass:")
            col.prop(scene.neltulzSmartSharpen, "bDisableErrorPopupsCheckbox", text="Disable Error Popups")

            col = boxAdvancedOptions.column()
            row = col.row(align=True)
            op = row.operator('object.neltulz_smart_sharpen_reset_settings', text="Reset Settings")