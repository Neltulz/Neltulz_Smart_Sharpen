
import bpy
from . properties import NeltulzSmartSharpen_IgnitProperties
from . misc_layout import createShowHide

from bpy.props import (StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, EnumProperty, PointerProperty)
from bpy.types import (Panel, Operator, AddonPreferences, PropertyGroup, Menu)

class OBJECT_PT_Test(Panel):
    bl_idname = "OBJECT_PT_Test"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Test"

    def draw(self, context):
        scene = context.scene

        layout = self.layout

        layout.label(text="Edge Display")

        buttonRow = layout.row(align=True)
        buttonRow.scale_y = 1.5

        if context.space_data.overlay.show_edge_sharp:
            sharpText = "Sharp (Enabled)"
            sharpIcon = "SHARPCURVE"
        else:
            sharpText = "Sharp (Disabled)"
            sharpIcon = "SPHERECURVE"

        buttonRow.prop(context.space_data.overlay, "show_edge_sharp",        toggle=True, text=sharpText, icon=sharpIcon )
        

        layout.label(text="Others")
        buttonRow = layout.row(align=True)
        
        buttonRow.prop(context.space_data.overlay, "show_edge_crease",       toggle=True, text="Creases" )
        buttonRow.prop(context.space_data.overlay, "show_edge_bevel_weight", toggle=True, text="Bevel" )
        buttonRow.prop(context.space_data.overlay, "show_edge_seams",        toggle=True, text="Seams" )

class OBJECT_PT_NeltulzSmartSharpen(Panel):

    bl_idname = "ntz_smrt_shrp.neltulz_smart_sharpen_panel"
    bl_label = "Smart Sharpen v1.0.8"
    bl_category = "Neltulz"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):

        layout = self.layout
        scene = context.scene

        col = layout.column(align=True)

        #Create buttons for 0 (Full Sharp) and 180 (Full Soft)
        col = layout.column()
        row = col.row(align=True)
        row.scale_y = 1.5

        op = row.operator('ntz_smrt_shrp.neltulz_smart_sharpen', text="0 (Full Sharp)")
        op.degreesValue=0

        op = row.operator('ntz_smrt_shrp.neltulz_smart_sharpen', text="180 (Full Soft)")
        op.degreesValue=180

        popoverRow = row.column(align=True)
        popoverRow.scale_x = 1.5

        if context.space_data.overlay.show_edge_sharp:
            popoverIcon = "SHARPCURVE"
        else:
            popoverIcon = "SPHERECURVE"

        popover = popoverRow.prop_with_popover(
            scene.neltulzSmartSharpen,
            "smoothShadeObject",
            text="",
            icon=popoverIcon,
            icon_only=True,
            panel="OBJECT_PT_Test",
        )
        
        

        degreesList = [3, 5, 10, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175]

        allDegreesButtons = layout.grid_flow(row_major=True, columns=4, align=True)

        for degreeValue in degreesList:

            op = allDegreesButtons.operator('ntz_smrt_shrp.neltulz_smart_sharpen', text=f"{degreeValue}" )
            op.degreesValue=degreeValue

            if scene.neltulzSmartSharpen.smoothShadeObject == "SMOOTH":
                op.smoothShadeObject = True

                op.autoSmoothNormals = scene.neltulzSmartSharpen.bAutoSmoothCheckbox

                op.autoSmoothAngle = scene.neltulzSmartSharpen.bAutoSmoothSlider
                

            elif scene.neltulzSmartSharpen.smoothShadeObject == "NO_SMOOTH":
                op.smoothShadeObject = False

        

        # -----------------------------------------------------------------------------
        #   Use Advanced Settings Box
        # -----------------------------------------------------------------------------

        advancedSettingsWrapper = layout.column(align=True)

        advancedOptionsSection = advancedSettingsWrapper.column(align=True)
        


        #create show/hide toggle for options section
        createShowHide(self, context, scene, "neltulzSmartSharpen", "bShowHideOptions", None, "Options", advancedOptionsSection)

        

        if scene.neltulzSmartSharpen.bShowHideOptions:

            advancedOptionsSection.separator()

            advancedOptionsRow = advancedOptionsSection.row(align=True)

            leftSpacer = advancedOptionsRow.column(align=True)
            leftSpacer.label(text=" ")
            leftSpacer.alignment= "LEFT"
            leftSpacer.ui_units_x = 1

            advancedOptionsCol = advancedOptionsRow.column(align=True)
            advancedOptionsCol.alignment="EXPAND"
            advancedOptionsCol.ui_units_x = 100000

            col = advancedOptionsCol.column(align=True)
            
            col.label(text="Smooth Shade Object:")
            col.prop(scene.neltulzSmartSharpen, "smoothShadeObject", text="" )
            
            if scene.neltulzSmartSharpen.smoothShadeObject == "SMOOTH":

                smoothNormalsBox = advancedOptionsCol.box()
                smoothNormalsBox.prop(scene.neltulzSmartSharpen, "bAutoSmoothCheckbox", text="Auto Smooth Normals" )

                col = smoothNormalsBox.column()
                row = col.row(align=True)
                row.label(text="Angle")
                row.prop(scene.neltulzSmartSharpen, "bAutoSmoothSlider", text='')

                row.enabled = scene.neltulzSmartSharpen.bAutoSmoothCheckbox
            
            col = advancedOptionsCol.column()
            row = col.row(align=True)
            
            col.separator()

            col = advancedOptionsCol.column()
            row = col.row(align=True)
            op = row.operator('ntz_smrt_shrp.reset_settings', text="Reset Settings")

