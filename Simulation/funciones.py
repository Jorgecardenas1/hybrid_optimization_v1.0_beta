# -*- coding: utf-8 -*-
"""
Created on 30/07/2020

@author: Daniel Montofré and Oscar Restrepo
"""

from .global_ import *

#from .parametros import *
#import Simulation.parametros as parametros

def agregaVariable(proj,nombre,valor):
        oDesign = proj.SetActiveDesign(nombre_diseno)
        oDesign.ChangeProperty(
    	[
    		"NAME:AllTabs",
    		[
    			"NAME:LocalVariableTab",
    			[
    				"NAME:PropServers", 
    				"LocalVariables"
    			],
    			[
    				"NAME:NewProps",
    				[
    					"NAME:" + nombre,
    					"PropType:="		, "VariableProp",
    					"UserDef:="		, True,
    					"Value:="		, valor
    				]
    			]
    		]
    	])
    

def modificaVariable(proj,nombre,valor):
    oDesign = proj.SetActiveDesign(nombre_diseno)
    oDesign.ChangeProperty(
    	[
    		"NAME:AllTabs",
    		[
    			"NAME:LocalVariableTab",
    			[
    				"NAME:PropServers", 
    				"LocalVariables"
    			],
    			[
    				"NAME:ChangedProps",
    				[
    					"NAME:"+ nombre ,
    					"Value:="		, valor
    				]
    			]
    		]
    	])

    
def agregaArreglo(proj,nombre,valor):
    oDesign = proj.SetActiveDesign(nombre_diseno)
    oDesign.ChangeProperty(
    	[
    		"NAME:AllTabs",
    		[
    			"NAME:LocalVariableTab",
    			[
    				"NAME:PropServers", 
    				"LocalVariables"
    			],
    			[
    				"NAME:NewProps",
    				[
    					"NAME:" + nombre,
    					"PropType:="		, "VariableProp",
    					"UserDef:="		, True,
    					"Value:="		, valor
    				]
    			]
    		]
    	])

# modifica un arreglo del proyecto proj
# nombre y valor son strings
    
def modificaArreglo(proj,nombre,valor):
    oDesign = proj.SetActiveDesign(nombre_diseno)
    oDesign.ChangeProperty(
    	[
    		"NAME:AllTabs",
    		[
    			"NAME:LocalVariableTab",
    			[
    				"NAME:PropServers", 
    				"LocalVariables"
    			],
    			[
    				"NAME:ChangedProps",
    				[
    					"NAME:"+ nombre,
    					"Value:="		, valor
    				]
    			]
    		]
    	])

    
#UNDERNEATH THE COMMANDS TO GENERATE THE S PARAMETERS ARE PRESENTED.
    
#Creating the S11 data
def creaS11(proj,nombre,simID):
    oDesign = proj.SetActiveDesign(nombre_diseno)
    oModule = oDesign.GetModule("ReportSetup")
    oModule.CreateReport("S11", "Modal Solution Data", "Rectangular Plot", "Setup1 : Sweep", 
    	[
    		"Domain:="		, "Sweep"
    	], 
    	[
    		"Freq:="		, ["All"],
    	], 
    	[
    		"X Component:="		, "Freq",
    		"Y Component:="		, ["dB(S(1,1))"]
    	], [])

    oModule.ExportToFile("S11", direccion_archivos+"/output/"+str(simID)+"/files/"+r"datosS11"+str(nombre)+".csv")



#Creating the S21 data
def creaS21(proj,nombre,simID):
    oDesign = proj.SetActiveDesign(nombre_diseno)
    oModule = oDesign.GetModule("ReportSetup")
    oModule.CreateReport("S21", "Modal Solution Data", "Rectangular Plot", "Setup1 : Sweep", 
    	[
    		"Domain:="		, "Sweep"
    	], 
    	[
    		"Freq:="		, ["All"],
    	], 
    	[
    		"X Component:="		, "Freq",
    		"Y Component:="		, ["dB(S(2,1))"]
    	], [])
    oModule.ExportToFile("S21",direccion_archivos+"/output/"+str(simID)+"/files/"+r"datosS21"+str(nombre)+".csv")



#Creating the S31 data
def creaS31(proj,nombre,simID):
    oDesign = proj.SetActiveDesign(nombre_diseno)
    oModule = oDesign.GetModule("ReportSetup")
    oModule.CreateReport("S31", "Modal Solution Data", "Rectangular Plot", "Setup1 : Sweep", 
    	[
    		"Domain:="		, "Sweep"
    	], 
    	[
    		"Freq:="		, ["All"],
    	], 
    	[
    		"X Component:="		, "Freq",
    		"Y Component:="		, ["dB(S(3,1))"]
    	], [])
    oModule.ExportToFile("S31", direccion_archivos+"/output/"+str(simID)+"/files/"+r"datosS31"+str(nombre)+".csv")



#Creating the S41 data
def creaS41(proj,nombre,simID):
    oDesign = proj.SetActiveDesign(nombre_diseno)
    oModule = oDesign.GetModule("ReportSetup")
    oModule.CreateReport("S41", "Modal Solution Data", "Rectangular Plot", "Setup1 : Sweep", 
    	[
    		"Domain:="		, "Sweep"
    	], 
    	[
    		"Freq:="		, ["All"],
    	], 
    	[
    		"X Component:="		, "Freq",
    		"Y Component:="		, ["dB(S(4,1))"]
    	], [])
    oModule.ExportToFile("S41", direccion_archivos+"/output/"+str(simID)+"/files/"+r"datosS41"+str(nombre)+".csv")


def creaAmpImb(proj,nombre,simID):
	
	oDesign = proj.SetActiveDesign(nombre_diseno)
	oModule = oDesign.GetModule("ReportSetup")
	oModule.CreateReport("Amplitud Imbalance", "Modal Solution Data", "Rectangular Plot", "Setup1 : Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"],
		"a:="			, ["Nominal"],
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["AmpImbalance"]
	], [])
	
	oModule.ExportToFile("Amplitud Imbalance", direccion_archivos+"/output/"+str(simID)+"/files/"+r"amp_imb"+str(nombre)+".csv")


def creaPhaseImb(proj,nombre,simID):
	
	oDesign = proj.SetActiveDesign(nombre_diseno)
	oModule = oDesign.GetModule("ReportSetup")
	oModule.CreateReport("Phase Imbalance", "Modal Solution Data", "Rectangular Plot", "Setup1 : Sweep", 
	[
		"Domain:="		, "Sweep"
	], 
	[
		"Freq:="		, ["All"],
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["PhaseImb"]
	], [])

	oModule.ExportToFile("Phase Imbalance", direccion_archivos+"/output/"+str(simID)+"/files/"+r"pha_imb"+str(nombre)+".csv")
