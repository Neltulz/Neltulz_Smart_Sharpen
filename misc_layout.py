import bpy

#Show hide section with arrow, optional checkbox, and text
def createShowHide(self, context, scene, properties, showHideBool, optionalCheckboxBool, text, layout):

    if scene is not None:
        data = eval( f"scene.{properties}" )
        boolThing = eval( f"scene.{properties}.{showHideBool}" )
    else:
        data = self
        boolThing = eval( f"self.{showHideBool}")

    if boolThing:
        showHideIcon = "TRIA_DOWN"
    else:
        showHideIcon = "TRIA_RIGHT"

    row = layout.row(align=True)

    downArrow = row.column(align=True)
    downArrow.alignment = "LEFT"
    downArrow.prop(data, showHideBool, text="", icon=showHideIcon, emboss=False )

    if optionalCheckboxBool is not None:
        checkbox = row.column(align=True)
        checkbox.alignment = "LEFT"
        checkbox.prop(data, optionalCheckboxBool, text="" )

    textRow = row.column(align=True)
    textRow.alignment = "LEFT"
    textRow.prop(data, showHideBool, text=text, emboss=False )

    emptySpace = row.column(align=True)
    emptySpace.alignment = "EXPAND"
    emptySpace.prop(data, showHideBool, text=" ", emboss=False)

def createProp(self, context, scene, labelText, propItem, layout, scale_y):

    propRow = layout.grid_flow(columns=2, even_columns=True, even_rows=True, align=True)
    propRow.scale_y = scale_y

    propRowLabel = propRow.column(align=True)
    propRowLabel.alignment="RIGHT"
    propRowLabel.scale_x = 50
    propRowLabel.label(text=labelText)

    propRowItem = propRow.column(align=True)
    propRowItem.alignment="EXPAND"
    propRowItem.scale_x = 1
    propRowItem.prop(self, propItem, text="", expand=True)

def createPanelOptionsSection(self, context, scene, layout):
    
    
    layout.label(text="Smooth Shade Object:")
    layout.prop(scene.neltulzSmartSharpen, "smoothShadeObject", text="" )
    
    if scene.neltulzSmartSharpen.smoothShadeObject == "SMOOTH":

        smoothNormalsBox = layout.box()
        smoothNormalsBox.prop(scene.neltulzSmartSharpen, "bAutoSmoothCheckbox", text="Auto Smooth Normals" )

        col = smoothNormalsBox.column()
        row = col.row(align=True)
        row.label(text="Angle")
        row.prop(scene.neltulzSmartSharpen, "bAutoSmoothSlider", text='')

        row.enabled = scene.neltulzSmartSharpen.bAutoSmoothCheckbox
    
    col = layout.column(align=True)
    row = col.row(align=True)
    
    col.separator()

    col = layout.column()
    row = col.row(align=True)
    op = row.operator('ntz_smrt_shrp.reset_settings', text="Reset Settings")