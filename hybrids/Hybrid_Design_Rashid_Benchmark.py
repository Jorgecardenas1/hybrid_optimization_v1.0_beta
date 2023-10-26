# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 18:57:58 2020

@author: Daniel Montofré and Oscar Restrepo
@edited: Jorge Cárdenas

Hybrid type:
Even number of branches
"""
# This program is aimed to provide an optimizer for electromagnetic design of 
# mm-wave devices using the calculation engine fromm HFSS


############################################################################### 

import Simulation.funciones as fn
from Simulation.global_ import *

#from Simulation.parametros import *
#from Settings.global_ import *
import ScriptEnv
############################################################################### 

ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.NewProject(str(nombre_proyecto))
oProject.InsertDesign("HFSS", str(nombre_diseno), "DrivenModal", "")


###############################################################################

#ADD THE VARIABLE TO BE USED IN THE SETUP OF THE SIMULATION

#fn.agregaVariable(oProject,"frec","90GHz")
#fn.agregaVariable(oProject,"band_width","50GHz")
fn.agregaArreglo(oProject,"variables", "[0, 0.3, 0.3, 0.3, 0.3, 0.3, 1, 1.6, 2.5, 0.3,1.5,0.72]mm")  

# variables= [g0,g1,g2,g3,g4,p1,p2,p3,p4,s]

###############################################################################

# HERE THE DESIGN PARAMETERS OF THE WAVEGUIDE ARE DEFINED


#fn.agregaVariable(oProject,"a","2.8mm")
#fn.agregaVariable(oProject,"b","1.4mm")#1.27
fn.agregaVariable(oProject,"L","6.482mm")
###############################################################################

# INITIALIZE THE 3D DESIGN MODELER
oDesign = oProject.SetActiveDesign(nombre_diseno)
oEditor = oDesign.SetActiveEditor("3D Modeler")


#CREATES THE TOP WAVEGUIDE (PORTS 1 & 3)
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-variables[10]/2",
		"YPosition:="		, "variables[9]/2",
		"ZPosition:="		, "-L/2",
		"XSize:="		, "variables[10]",
		"YSize:="		, "variables[11]",
		"ZSize:="		, "L"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"air\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

#CREATES THE DOWN WAVEGUIDE (PORTS 2 & 4)
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-variables[10]/2",
		"YPosition:="		, "-variables[9]/2",
		"ZPosition:="		, "-L/2",
		"XSize:="		, "variables[10]",
		"YSize:="		, "-variables[11]",
		"ZSize:="		, "L"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"air\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


#CREATES THE CENTRAL SLOT
# oEditor.CreateBox(
# 	[
# 		"NAME:BoxParameters",
# 		"XPosition:="		, "-a/2",
# 		"YPosition:="		, "-variables[9]/2",
# 		"ZPosition:="		, "-variables[0]/2",
# 		"XSize:="		, "a",
# 		"YSize:="		, "variables[9]",
# 		"ZSize:="		, "variables[0]"
# 	], 
# 	[
# 		"NAME:Attributes",
# 		"Name:="		, "Box3",
# 		"Flags:="		, "",
# 		"Color:="		, "(143 175 143)",
# 		"Transparency:="	, 0,
# 		"PartCoordinateSystem:=", "Global",
# 		"UDMId:="		, "",
# 		"MaterialValue:="	, "\"air\"",
# 		"SurfaceMaterialValue:=", "\"\"",
# 		"SolveInside:="		, True,
# 		"IsMaterialEditable:="	, True,
# 		"UseMaterialAppearance:=", False,
# 		"IsLightweight:="	, False
# 	])


#CREATES THE P1 SLOT
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-variables[10]/2",
		"YPosition:="		, "-variables[9]/2",
		"ZPosition:="		, "variables[5]-variables[1]/2",
		"XSize:="		, "variables[10]",
		"YSize:="		, "variables[9]",
		"ZSize:="		, "variables[1]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box4",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"air\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


#CREATES THE -P1 SLOT
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-variables[10]/2",
		"YPosition:="		, "-variables[9]/2",
		"ZPosition:="		, "-variables[5]+variables[1]/2",
		"XSize:="		, "variables[10]",
		"YSize:="		, "variables[9]",
		"ZSize:="		, "-variables[1]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box5",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"air\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])



#CREATES THE P2 SLOT
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-variables[10]/2",
		"YPosition:="		, "-variables[9]/2",
		"ZPosition:="		, "variables[6]-variables[2]/2",
		"XSize:="		, "variables[10]",
		"YSize:="		, "variables[9]",
		"ZSize:="		, "variables[2]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box6",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"air\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


#CREATES THE -P2 SLOT
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-variables[10]/2",
		"YPosition:="		, "-variables[9]/2",
		"ZPosition:="		, "-variables[6]+variables[2]/2",
		"XSize:="		, "variables[10]",
		"YSize:="		, "variables[9]",
		"ZSize:="		, "-variables[2]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box7",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"air\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


#CREATES THE P3 SLOT
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-variables[10]/2",
		"YPosition:="		, "-variables[9]/2",
		"ZPosition:="		, "variables[7]-variables[3]/2",
		"XSize:="		, "variables[10]",
		"YSize:="		, "variables[9]",
		"ZSize:="		, "variables[3]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box8",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"air\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


#CREATES THE -P3 SLOT
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-variables[10]/2",
		"YPosition:="		, "-variables[9]/2",
		"ZPosition:="		, "-variables[7]+variables[3]/2",
		"XSize:="		, "variables[10]",
		"YSize:="		, "variables[9]",
		"ZSize:="		, "-variables[3]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box9",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"air\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

#CREATES THE P4 SLOT
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-variables[10]/2",
		"YPosition:="		, "-variables[9]/2",
		"ZPosition:="		, "variables[8]-variables[4]/2",
		"XSize:="		, "variables[10]",
		"YSize:="		, "variables[9]",
		"ZSize:="		, "variables[4]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box10",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"air\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


#CREATES THE -4 SLOT
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-variables[10]/2",
		"YPosition:="		, "-variables[9]/2",
		"ZPosition:="		, "-variables[8]+variables[4]/2",
		"XSize:="		, "variables[10]",
		"YSize:="		, "variables[9]",
		"ZSize:="		, "-variables[4]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box11",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"air\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


#THIS LINE TAKES ALL THE BOXES AND MERGE THEM INTO THE FINAL STRUCTURE
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Box1,Box2,Box4,Box5,Box6,Box7,Box8,Box9,Box10,Box11"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])

#THIS LINE ONLY CHANGES THE NAME OF THE STRUCTURE RECENTLY CREATED
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Box1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "RF_Hybrid"
				]
			]
		]
	])

###############################################################################

# THIS PART OF THE SCRIPT SETS THE BOUNDARY CONDITIONS, IN THIS CASE, THE WAVEPORTS
# IN ORDER TO KNOW THE NUMBER OF THE FACES TO BE ASSGINED AS WAVEPORTS, THE MOST 
# CONVENIENT IS TO LOOK INTO THE GRAPHICAL INTERFACE OF HFSS BY SELECTING THE TARGET FACE
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignWavePort(
	[
		"NAME:1",
		"Faces:="		, [8],
		"NumModes:="		, 1,
		"RenormalizeAllTerminals:=", True,
		"UseLineModeAlignment:=", False,
		"DoDeembed:="		, False,
		[
			"NAME:Modes",
			[
				"NAME:Mode1",
				"ModeNum:="		, 1,
				"UseIntLine:="		, False,
				"CharImp:="		, "Zpi"
			]
		],
		"ShowReporterFilter:="	, False,
		"ReporterFilter:="	, [True],
		"UseAnalyticAlignment:=", False
	])
oModule.AssignWavePort(
	[
		"NAME:4",
		"Faces:="		, [36],
		"NumModes:="		, 1,
		"RenormalizeAllTerminals:=", True,
		"UseLineModeAlignment:=", False,
		"DoDeembed:="		, False,
		[
			"NAME:Modes",
			[
				"NAME:Mode1",
				"ModeNum:="		, 1,
				"UseIntLine:="		, False,
				"CharImp:="		, "Zpi"
			]
		],
		"ShowReporterFilter:="	, False,
		"ReporterFilter:="	, [True],
		"UseAnalyticAlignment:=", False
	])
oModule.AssignWavePort(
	[
		"NAME:2",
		"Faces:="		, [7],
		"NumModes:="		, 1,
		"RenormalizeAllTerminals:=", True,
		"UseLineModeAlignment:=", False,
		"DoDeembed:="		, False,
		[
			"NAME:Modes",
			[
				"NAME:Mode1",
				"ModeNum:="		, 1,
				"UseIntLine:="		, False,
				"CharImp:="		, "Zpi"
			]
		],
		"ShowReporterFilter:="	, False,
		"ReporterFilter:="	, [True],
		"UseAnalyticAlignment:=", False
	])
oModule.AssignWavePort(
	[
		"NAME:3",
		"Faces:="		, [35],
		"NumModes:="		, 1,
		"RenormalizeAllTerminals:=", True,
		"UseLineModeAlignment:=", False,
		"DoDeembed:="		, False,
		[
			"NAME:Modes",
			[
				"NAME:Mode1",
				"ModeNum:="		, 1,
				"UseIntLine:="		, False,
				"CharImp:="		, "Zpi"
			]
		],
		"ShowReporterFilter:="	, False,
		"ReporterFilter:="	, [True],
		"UseAnalyticAlignment:=", False
	])

# oModule = oDesign.GetModule("BoundarySetup")
# oModule.AssignWavePort(
# 	[
# 		"NAME:1",
# 		"Faces:="		, [8],
# 		"NumModes:="		, 1,
# 		"RenormalizeAllTerminals:=", True,
# 		"UseLineModeAlignment:=", False,
# 		"DoDeembed:="		, False,
# 		[
# 			"NAME:Modes",
# 			[
# 				"NAME:Mode1",
# 				"ModeNum:="		, 1,
# 				"UseIntLine:="		, False,
# 				"CharImp:="		, "Zpi"
# 			]
# 		],
# 		"ShowReporterFilter:="	, False,
# 		"ReporterFilter:="	, [True],
# 		"UseAnalyticAlignment:=", False
# 	])
# oModule.AssignWavePort(
# 	[
# 		"NAME:4",
# 		"Faces:="		, [36],
# 		"NumModes:="		, 1,
# 		"RenormalizeAllTerminals:=", True,
# 		"UseLineModeAlignment:=", False,
# 		"DoDeembed:="		, False,
# 		[
# 			"NAME:Modes",
# 			[
# 				"NAME:Mode1",
# 				"ModeNum:="		, 1,
# 				"UseIntLine:="		, False,
# 				"CharImp:="		, "Zpi"
# 			]
# 		],
# 		"ShowReporterFilter:="	, False,
# 		"ReporterFilter:="	, [True],
# 		"UseAnalyticAlignment:=", False
# 	])
# oModule.AssignWavePort(
# 	[
# 		"NAME:2",
# 		"Faces:="		, [7],
# 		"NumModes:="		, 1,
# 		"RenormalizeAllTerminals:=", True,
# 		"UseLineModeAlignment:=", False,
# 		"DoDeembed:="		, False,
# 		[
# 			"NAME:Modes",
# 			[
# 				"NAME:Mode1",
# 				"ModeNum:="		, 1,
# 				"UseIntLine:="		, False,
# 				"CharImp:="		, "Zpi"
# 			]
# 		],
# 		"ShowReporterFilter:="	, False,
# 		"ReporterFilter:="	, [True],
# 		"UseAnalyticAlignment:=", False
# 	])
# oModule.AssignWavePort(
# 	[
# 		"NAME:3",
# 		"Faces:="		, [35],
# 		"NumModes:="		, 1,
# 		"RenormalizeAllTerminals:=", True,
# 		"UseLineModeAlignment:=", False,
# 		"DoDeembed:="		, False,
# 		[
# 			"NAME:Modes",
# 			[
# 				"NAME:Mode1",
# 				"ModeNum:="		, 1,
# 				"UseIntLine:="		, False,
# 				"CharImp:="		, "Zpi"
# 			]
# 		],
# 		"ShowReporterFilter:="	, False,
# 		"ReporterFilter:="	, [True],
# 		"UseAnalyticAlignment:=", False
# 	])

##############################################################################

# ANALYSIS SETUP
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("HfssDriven", 
	[
		"NAME:Setup1",
		"AdaptMultipleFreqs:="	, False,
		"Frequency:="		, "186GHz",
		"MaxDeltaS:="		, 0.02,
		"PortsOnly:="		, False,
		"UseMatrixConv:="	, False,
		"MaximumPasses:="	, 6,
		"MinimumPasses:="	, 1,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"IsEnabled:="		, True,
		"BasisOrder:="		, 1,
		"DoLambdaRefine:="	, True,
		"DoMaterialLambda:="	, True,
		"SetLambdaTarget:="	, False,
		"Target:="		, 0.3333,
		"UseMaxTetIncrease:="	, False,
		"PortAccuracy:="	, 2,
		"UseABCOnPort:="	, False,
		"SetPortMinMaxTri:="	, False,
		"UseDomains:="		, False,
		"UseIterativeSolver:="	, False,
		"SaveRadFieldsOnly:="	, False,
		"SaveAnyFields:="	, True,
		"IESolverType:="	, "Auto",
		"LambdaTargetForIESolver:=", 0.15,
		"UseDefaultLambdaTgtForIESolver:=", True
	])

# SET THE FREQUENCY SWEEP
oModule.InsertFrequencySweep("Setup1", 
	[
		"NAME:Sweep",
		"IsEnabled:="		, True,
		"RangeType:="		, "LinearCount",
		"RangeStart:="		, "163GHz",
		"RangeEnd:="		, "210GHz",
		"RangeCount:="		, 151,
		"Type:="		, "Discrete",
		"SaveFields:="		, False,
		"SaveRadFields:="	, False,
		"ExtrapToDC:="		, False
	])
##############################################################################


# =============================================================================
#  SAVE THE PROJECT AND CLOSE THE PROGRAM

oProject.SaveAs("C:\\Users\\Astrolab\\Documents\\Ansoft\\" +"Band2+3_Hybrid_Rashid_Benchmark"+'.aedt', True)
#oProject.SaveAs("C:\\Users\\Astrolab\\Documents\\Ansoft\\" + '"'+nombre_proyecto+'"'+ ", True)
# oDesktop.CloseProject("Blade_PSO")
# =============================================================================
