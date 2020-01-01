
import bpy
from . properties import NTZSMSHRP_ignitproperties
from . import misc_layout

from bpy.props import (StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, EnumProperty, PointerProperty)
from bpy.types import (Panel, Operator, AddonPreferences, PropertyGroup, Menu)

class NTZSMSRHP_PT_options(Panel):
    bl_label = "Neltulz - Options"
    bl_idname = "NTZSMSRHP_PT_options"
    bl_category = ""
    bl_space_type = "VIEW_3D"
    bl_region_type = "WINDOW"

    def draw(self, context):
        scene = context.scene
        layout = self.layout
        layout.ui_units_x = 10

        optionsSection = layout.column(align=True)

        misc_layout.options_sectionInner(self, context, scene, optionsSection)

    #END draw()

class NTZSMSRHP_PT_additionaldegreescompact(Panel):
    bl_label = "Neltulz - Additional Degrees (Compact)"
    bl_idname = "NTZSMSRHP_PT_additionaldegreescompact"
    bl_category = ""
    bl_space_type = "VIEW_3D"
    bl_region_type = "WINDOW"

    def draw(self, context):
        scene = context.scene
        layout = self.layout
        layout.ui_units_x = 8

        additionalDegreesSection = layout.column(align=True)

        misc_layout.additionalDegreesCompact_sectionInner(self, context, scene, additionalDegreesSection)

    #END draw()

class NTZSMSHRP_PT_edgedisplayoptions(Panel):
    bl_label = "Test"
    bl_idname = "NTZSMSHRP_PT_edgedisplayoptions"
    bl_category = ""
    bl_space_type = "VIEW_3D"
    bl_region_type = "WINDOW"

    def draw(self, context):
        scene = context.scene

        layout = self.layout
        layout.ui_units_x = 8

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

    bl_label = "Smart Sharpen v1.0.10"
    bl_category = "Neltulz"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    bUseCompactSidebarPanel = BoolProperty(
        name="Use Compact Panel",
        description="Use Compact Panel",
        default = False
    )

    bUseCompactPopupAndPiePanel = BoolProperty(
        name="Use Compact Popup & Pie Panel",
        description="Use Compact Popup & Pie Panel",
        default = True
    )

    def draw(self, context):

        misc_layout.mainSmartSharpenPanel(self, context, self.bUseCompactSidebarPanel, self.bUseCompactPopupAndPiePanel)

    #END draw()