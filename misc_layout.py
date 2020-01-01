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

def createProp(self, context, scene, bEnabled, labelText, propItem, scale_y, labelScale, propScale, labelAlign, propAlign, propText, bExpandProp, layout):

    propRow = layout.row(align=True)

    if not bEnabled:
        propRow.enabled = False

    propRow.scale_y = scale_y

    propRowLabel = propRow.row(align=True)
    propRowLabel.alignment="EXPAND"
    propRowLabel.ui_units_x = labelScale

    propRowLabel1 = propRowLabel.row(align=True)
    propRowLabel1.alignment=labelAlign
    propRowLabel1.scale_x = 1

    propRowLabel1.label(text=labelText)

    propRowItem = propRow.row(align=True)
    propRowItem.alignment=propAlign

    propRowItem1 = propRowItem.row(align=True)
    propRowItem1.alignment=propAlign
    propRowItem1.ui_units_x = propScale
    propRowItem1.scale_x = 100

    propRowItem1.prop(self, propItem, text=propText, expand=bExpandProp)

def mainSmartSharpenPanel(self, context, bUseCompactSidebarPanel, bUseCompactPopupAndPiePanel):
    layout = self.layout
    layout = layout.column(align=True)
    scene = context.scene

    #determine if panel is inside of a popop/pie menu
    panelInsidePopupOrPie = context.region.type == 'WINDOW'

    if panelInsidePopupOrPie:

        if bUseCompactPopupAndPiePanel:
            layout.ui_units_x = 8
            layout.label(text="Smart Sharpen")

        else:
            layout.ui_units_x = 13
            layout.label(text="Neltulz - Smart Sharpen")

    #Full Sharp and Soft Buttons
    fullSharpAndSoftBtns_section(self, context, scene, panelInsidePopupOrPie, bUseCompactSidebarPanel, bUseCompactPopupAndPiePanel, layout)

    #All Degrees Buttons Section
    allDegreesBtns_section(self, context, scene, panelInsidePopupOrPie, bUseCompactSidebarPanel, bUseCompactPopupAndPiePanel, layout)

    #Options Section
    options_section(self, context, scene, panelInsidePopupOrPie, bUseCompactSidebarPanel, bUseCompactPopupAndPiePanel, layout)

def sep(scaleY, layout):
    #custom separator that allows shorter y distance
    sep = layout.column(align=True)
    sep.label(text="",)
    sep.scale_y = scaleY

def fullSharpAndSoftBtns_section(self, context, scene, panelInsidePopupOrPie, bUseCompactSidebarPanel, bUseCompactPopupAndPiePanel, layout):
    
    #Create buttons for 0 (Full Sharp) and 180 (Full Soft)
    col = layout.column(align=True)
    row = col.row(align=True)

    buttonScaleY = 1.5 #declare
    fullSharpText = "0 (Full Sharp)" #declare
    fullSoftText = "180 (Full Soft)" #declare

    if (panelInsidePopupOrPie and bUseCompactPopupAndPiePanel) or (not panelInsidePopupOrPie and bUseCompactSidebarPanel): #compact panel
        buttonScaleY = 1
        fullSharpText = "0"
        fullSoftText = "180"

    row.scale_y = buttonScaleY

    op = row.operator('ntz_smrt_shrp.neltulz_smart_sharpen', text=fullSharpText)
    op.degreesValue=0

    op = row.operator('ntz_smrt_shrp.neltulz_smart_sharpen', text=fullSoftText)
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
    
    sep(0.25, layout)

def allDegreesBtns_section(self, context, scene, panelInsidePopupOrPie, bUseCompactSidebarPanel, bUseCompactPopupAndPiePanel, layout):
    if (panelInsidePopupOrPie and bUseCompactPopupAndPiePanel) or (not panelInsidePopupOrPie and bUseCompactSidebarPanel): #compact panel
        degreesList = [3, 5, 10, 15, 25, 35, 45, 55, 65, 75]
        colCount = 5
    else:
        degreesList = [3, 5, 10, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175]
        colCount = 4
    
    allDegreesButtons = layout.grid_flow(row_major=True, columns=colCount, align=True)


    for degreeValue in degreesList:

        op = allDegreesButtons.operator('ntz_smrt_shrp.neltulz_smart_sharpen', text=f"{degreeValue}" )
        op.degreesValue=degreeValue

        if scene.neltulzSmartSharpen.smoothShadeObject == "SMOOTH":
            op.smoothShadeObject = True

            op.autoSmoothNormals = scene.neltulzSmartSharpen.bAutoSmoothCheckbox

            op.autoSmoothAngle = scene.neltulzSmartSharpen.bAutoSmoothSlider
            

        elif scene.neltulzSmartSharpen.smoothShadeObject == "NO_SMOOTH":
            op.smoothShadeObject = False

def additionalDegreesCompact_sectionInner(self, context, scene, layout):
    degreesList = [85, 95, 105, 115, 125, 135, 145, 155, 165, 175]

    allDegreesButtons = layout.grid_flow(row_major=True, columns=5, align=True)

    for degreeValue in degreesList:

        op = allDegreesButtons.operator('ntz_smrt_shrp.neltulz_smart_sharpen', text=f"{degreeValue}" )
        op.degreesValue=degreeValue

        if scene.neltulzSmartSharpen.smoothShadeObject == "SMOOTH":
            op.smoothShadeObject = True

            op.autoSmoothNormals = scene.neltulzSmartSharpen.bAutoSmoothCheckbox

            op.autoSmoothAngle = scene.neltulzSmartSharpen.bAutoSmoothSlider
            

        elif scene.neltulzSmartSharpen.smoothShadeObject == "NO_SMOOTH":
            op.smoothShadeObject = False

def options_section(self, context, scene, panelInsidePopupOrPie, bUseCompactSidebarPanel, bUseCompactPopupAndPiePanel, layout):

    optionsSection = layout.column(align=True)

    sep(0.25, optionsSection)

    popoverIcon = "NONE"
    bIconOnly = False
    popoverAlign = "EXPAND"

    if (panelInsidePopupOrPie and bUseCompactPopupAndPiePanel) or (not panelInsidePopupOrPie and bUseCompactSidebarPanel):
        popoverIcon = "SETTINGS"
        bIconOnly = True
        popoverAlign = "RIGHT"


    if panelInsidePopupOrPie or (not panelInsidePopupOrPie and bUseCompactSidebarPanel): #compact panel

        popoverRow = optionsSection.row(align=True)
        popoverRow.alignment = "EXPAND"

        if (panelInsidePopupOrPie and bUseCompactPopupAndPiePanel) or (not panelInsidePopupOrPie and bUseCompactSidebarPanel):

            popoverAdditionalDegreesRow = popoverRow.column(align=True)
            popoverAdditionalDegreesRow.alignment = "EXPAND"
            popover = popoverAdditionalDegreesRow.prop_with_popover(scene.neltulzSmartSharpen, "additionalDegreesEnum", text="", icon="NONE", icon_only=False, panel="NTZSMSRHP_PT_additionaldegreescompact")

            popoverRow.separator()

        popoverOptionsRow = popoverRow.column(align=True)
        popoverOptionsRow.alignment = "RIGHT"
        popover = popoverOptionsRow.prop_with_popover(scene.neltulzSmartSharpen, "optionsPopoverEnum", text="", icon=popoverIcon, icon_only=bIconOnly, panel="NTZSMSRHP_PT_options")
    
    else:
        #create show/hide toggle for options section
        createShowHide(self, context, scene, "neltulzSmartSharpen", "bShowHideOptions", None, "Options", optionsSection)

        if scene.neltulzSmartSharpen.bShowHideOptions:

            optionsSection.separator()
            
            optionsSectionRow = optionsSection.row(align=True)

            spacer = optionsSectionRow.column(align=True)
            spacer.label(text="", icon="BLANK1")
            spacer.alignment="LEFT"

            optionsCol = optionsSectionRow.column(align=True)

            options_sectionInner(self, context, scene, optionsCol)


def options_sectionInner(self, context, scene, layout):
    
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