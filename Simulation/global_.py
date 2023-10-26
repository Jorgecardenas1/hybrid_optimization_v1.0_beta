# -*- coding: utf-8 -*-


import uuid
from datetime import datetime
import os

global local_system 
local_system = ""

global current_path
current_path=""

"""Esto debe ser de esta forma pues HFSS tiene problemas para insertar imports 
incluso si alguna referencia circular tienen numpy, puede presentar problemas"""

global direccion_archivos
direccion_archivos=os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

global nombre_proyecto
nombre_proyecto = "Band2+3_Hybrid_testV3"

global nombre_diseno 
nombre_diseno = "Optimized Hybrid"

global nombre_variables
nombre_variables = "variables"

global nombre_particle 
nombre_particle = "particle"

global unidades
unidades = "mm"

global branches
branches = 0

global direccion_Ansoft
direccion_Ansoft=r"C:\\Users\\Astrolab\\Documents\\Ansoft\\" 


global file_folder 
file_folder = "files"

global figures_folder
figures_folder = "figures"

global n_variables 
n_variables = 0

global iteraciones 
iteraciones = 0

global n_particulas 
n_particulas = 0

global A_dimension_index
A_dimension_index = 0

global branch_number
branch_number=0

global nominales 
nominales = []

global  var_min 
var_min = []

global var_max 
var_max = []

def setSimID():
    global simulationID
    simulationID=str(uuid.uuid4())

global HFSS_RUN_STRINGS
HFSS_RUN_STRINGS=["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                    "-features=beta -ng -runscriptandexit", "simulacion.py"]

"""Other variables"""
global start_time
start_time = datetime.now()