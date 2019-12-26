
import bpy
from . properties import NTZSMSHRP_ignitproperties
from . import misc_layout

from bpy.props import (StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, EnumProperty, PointerProperty)
from bpy.types import (Panel, Operator, AddonPreferences, PropertyGroup, Menu)

class NTZSMSRHP_PT_options(Panel):
    bl_idname = "NTZSMSRHP_PT_options"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Options"

    def draw(self, context):
        scene = context.scene
        layout = self.layout

        optionsSection = layout.column(align=True)

        misc_layout.createPanelOptionsSection(self, context, scene, optionsSection)

    #END draw()

class NTZSMSHRP_PT_edgedisplayoptions(Panel):
    bl_idname = "NTZSMSHRP_PT_edgedisplayoptions"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Test"

    def draw(self, context):
        scene = context.scene

        layout = self.layout

        layout.label(text="Edge Display")

        buttonRow = layout.row(align=True)
        buttonRow.scale_y = 1.5

        buttonRow.prop(context.space_data.overlay, "show_edge_sharp",        toggle=True, text="Sharp", icon="SHARPCURVE" )
        

        layout.label(text="Others")
        buttonRow = layout.row(align=True)
        
        buttonRow.prop(context.space_data.overlay, "show_edge_crease",       toggle=True, text="Creases" )
        buttonRow.prop(context.space_data.overlay, "show_edge_bevel_weight", toggle=True, text="Bevel" )
        buttonRow.prop(context.space_data.overlay, "show_edge_seams",        toggle=True, text="Seams" )

class NTZSMSHRP_PT_sidebarpanel(Panel):

    bl_label = "Smart Sharpen v1.0.9"
    bl_category = "Neltulz"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):

        layout = self.layout
        scene = context.scene

        #determine if panel is inside of a popop/pie menu
        panelInsidePopupOrPie = context.region.type == 'WINDOW'

        if panelInsidePopupOrPie:
            layout.ui_units_x = 13
            layout.label(text="Neltulz - Smart Sharpen v1.0.9")

        col = layout.column(align=True)

        #Create buttons for 0 (Full Sharp) and 180 (Full Soft)
        col = layout.column(align=True)
        row = col.row(align=True)
        row.scale_y = 1.5

        op = row.operator('ntz_smrt_shrp.neltulz_smart_sharpen', text="0 (Full Sharp)")
        op.degreesValue=0

        op = row.operator('ntz_smrt_shrp.neltulz_smart_sharpen', text="180 (Full Soft)")
        op.degreesValue=180

        popoverRow = row.column(align=True)
        popoverRow.scale_x = 1.5

        popover = popoverRow.prop_with_popover(
            scene.neltulzSmartSharpen,
            "sharpEdgeDisplay_PopoverEnum",
            text="",
            icon="SHARPCURVE",
            icon_only=True,
            panel="NTZSMSHRP_PT_edgedisplayoptions",
        )
        
        if panelInsidePopupOrPie:
            sep = layout.column(align=True)
            sep.label(text=" ")
            sep.scale_y = 0.1

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


        optionsSection = layout.column(align=True)
                
        if not panelInsidePopupOrPie:

            #create show/hide toggle for options section
            misc_layout.createShowHide(self, context, scene, "neltulzSmartSharpen", "bShowHideOptions", None, "Options", optionsSection)

            if scene.neltulzSmartSharpen.bShowHideOptions:

                optionsSection.separator()
                
                optionsSectionRow = optionsSection.row(align=True)

                spacer = optionsSectionRow.column(align=True)
                spacer.label(text="", icon="BLANK1")
                spacer.alignment="LEFT"

                optionsCol = optionsSectionRow.column(align=True)

                misc_layout.createPanelOptionsSection(self, context, scene, optionsCol)

        else:
            
            optionsSection.separator()

            popover = optionsSection.prop_with_popover(
                scene.neltulzSmartSharpen,
                "optionsPopoverEnum",
                text="",
                icon="NONE",
                icon_only=False,
                panel="NTZSMSRHP_PT_options",
            )