# -*- coding: utf-8 -*-
"""
Created on 27/07/2020

@author: Daniel Montofré and Oscar Restrepo
@edites: Jorge Cárdenas
"""
import subprocess
from Simulation.global_ import *
import inquirer


questions = [
    inquirer.List('size',
                message="Number of branches?",
                choices=['5', '7','8', '9','Band 2+3 8 br - normal vector',"Band 2+3 8 br - flex","Band 3 - 8Br","Band 3 - flat 8Br Flex","Band 3 - 8Br Flex","Band 3 - 12Br Flex",'100','rashid band 5','rashid band 5 benchmark H1H2','rashid band 5 - extrusion','rashid band 5 - extrusion_free',\
                    'winged band 2+3','winged band 2+3 free param','3-winged band 2+3 free param'\
                        ,'3-winged band 2+3 fixed param','3-winged band 2+3 fixed param reduced vector','3-winged band 2+3 flex distribution','10-br 3-winged band 2+3 flex distribution','12-br 3-winged band 2+3 flex distribution','12-br 3-winged band 2+3 fixed param reduced vector',
                        '3-winged band 2+3 Rashid Parameters Vector','3-winged band 2+3 10 Branch Rashid Parameters','3-winged band 2+3 12 Branch Rashid Parameters','3-winged band 2+3 14 Branch Rashid Parameters'],
            ),
    ]
answers = inquirer.prompt(questions)
if answers["size"]!="Band 2+3 8 br - flex" and answers["size"]!="Band 3 - 8Br" and answers["size"]!="Band 3 - flat 8Br Flex" and answers["size"]!="Band 3 - 8Br Flex" and answers["size"]!="Band 3 - 12Br Flex" \
     and answers["size"]!= 'rashid band 5' and answers["size"]!= 'winged band 2+3' \
    and answers["size"] != 'rashid band 5 - extrusion' and answers['size'] !='rashid band 5 - extrusion_free'\
        and answers['size']!='rashid band 5 benchmark H1H2' and answers['size']!='10-br 3-winged band 2+3 flex distribution'\
            and answers["size"]!='12-br 3-winged band 2+3 flex distribution'\
        and answers["size"]!='winged band 2+3 free param' and answers["size"]!='3-winged band 2+3 free param' \
            and answers['size']!='3-winged band 2+3 flex distribution'\
            and answers["size"]!='3-winged band 2+3 fixed param' and answers["size"]!='3-winged band 2+3 fixed param reduced vector'\
                and answers["size"]!='12-br 3-winged band 2+3 fixed param reduced vector'\
                and answers["size"]!='3-winged band 2+3 Rashid Parameters Vector' and answers["size"]!='3-winged band 2+3 10 Branch Rashid Parameters'\
                    and answers["size"]!='3-winged band 2+3 14 Branch Rashid Parameters' and answers["size"]!='3-winged band 2+3 12 Branch Rashid Parameters':

    branches =int(answers["size"])
elif answers["size"]=='Band 2+3 8 br - normal vector':
    branches = 'Band 2+3 8 br - normal vector'
elif answers["size"]=="Band 2+3 8 br - flex":
    branches = "Band 2+3 8 br - flex"
elif answers["size"]=="Band 3 - 8Br":
    branches="Band 3 - 8Br"
elif answers["size"]=="Band 3 - flat 8Br Flex":
    branches="Band 3 - flat 8Br Flex"
elif answers["size"]=="Band 3 - 8Br Flex":
    branches="Band 3 - 8Br Flex"
elif answers["size"]=="Band 3 - 12Br Flex":
    branches="Band 3 - 12Br Flex"
elif answers["size"]=='rashid band 5':
    branches = 'rashid band 5'
elif answers["size"]=='rashid band 5 - extrusion':
    branches = 'rashid band 5 - extrusion'
elif answers["size"]=='rashid band 5 benchmark H1H2':
    branches = 'rashid band 5 benchmark H1H2'
elif answers["size"]=='rashid band 5 - extrusion_free':
    branches ='rashid band 5 - extrusion_free'
elif answers["size"]== 'winged band 2+3':
    branches = 'winged band 2+3'
elif answers["size"]== 'winged band 2+3 free param':
    branches = 'winged band 2+3 free param'
elif answers["size"]=='3-winged band 2+3 free param':
    branches = '3-winged band 2+3 free param'
elif answers["size"]=='3-winged band 2+3 fixed param':
    branches ='3-winged band 2+3 fixed param'
elif answers["size"]=='3-winged band 2+3 flex distribution':
    branches='3-winged band 2+3 flex distribution'
elif answers["size"]=='10-br 3-winged band 2+3 flex distribution':
    branches='10-br 3-winged band 2+3 flex distribution'
elif answers["size"]=='12-br 3-winged band 2+3 flex distribution':
    branches='12-br 3-winged band 2+3 flex distribution'
elif answers["size"]=='3-winged band 2+3 fixed param reduced vector':
    branches='3-winged band 2+3 fixed param reduced vector'
elif answers["size"]=='12-br 3-winged band 2+3 fixed param reduced vector':
    branches="12-br 3-winged band 2+3 fixed param reduced vector"
elif answers["size"]=='3-winged band 2+3 Rashid Parameters Vector':
    branches = '3-winged band 2+3 Rashid Parameters Vector'
elif answers["size"]=='3-winged band 2+3 10 Branch Rashid Parameters':
    branches = '3-winged band 2+3 10 Branch Rashid Parameters'
elif answers["size"]=='3-winged band 2+3 12 Branch Rashid Parameters':
    branches='3-winged band 2+3 12 Branch Rashid Parameters'
elif answers["size"]=='3-winged band 2+3 14 Branch Rashid Parameters':
    branches = '3-winged band 2+3 14 Branch Rashid Parameters'
else:
    pass
    

if branches == 7:
    nombre_proyecto = "Band2+3_Hybrid_testV2"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_v1.py"])
if branches == 8:
    nombre_proyecto = "Band2+3_Hybrid_testV4"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_v2.py"])
if branches == 'Band 2+3 8 br - normal vector':
    nombre_proyecto = "Band2+3_Hybrid_testV4_avar"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_V2_a_Var.py"])
if branches == "Band 2+3 8 br - flex":
    nombre_proyecto = "Band2+3_Hybrid_8br_fixedparam_flex"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_23_fixedparam_flex.py"])

if branches == "Band 3 - flat 8Br Flex":
    nombre_proyecto = "Band3_Hybrid_8br_flex"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_3_8br_flex.py"])

if branches == "Band 3 - 8Br":
    nombre_proyecto = "Band3_Hybrid_testV4_avar"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_Band3_8Br.py"])

if branches=="Band 3 - 8Br Flex":
    nombre_proyecto = "Band3_Hybrid_8br_fixedparam_flex"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_3_fixedparam_flex.py"])
if branches=="Band 3 - 12Br Flex":
    nombre_proyecto = "Band3_Hybrid_12br_3_extruded_fixedparam_flex"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_3_12Br_extruded_fixedparam_flex.py"])


if branches == 9:
    nombre_proyecto = "Band2+3_Hybrid_testV3"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design.py"])
if branches == 100:
    nombre_proyecto = "Band2+3_Hybrid_testV4_10Br"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_V2_a_Var_10Br.py"])
if branches == 'rashid band 5':
    nombre_proyecto = "Band2+3_Hybrid_Rashid_Benchmark"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_Rashid_Benchmark.py"])

if branches == 'rashid band 5 - extrusion':
    nombre_proyecto = "Band2+3_Hybrid_Rashid_extruded"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_5_extruded.py"])
if branches == 'rashid band 5 benchmark H1H2':

    nombre_proyecto = "Band5_Hybrid_8br_3_extruded_BenchmarkRashid"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_5_3_extruded_fixedparam_bechmark.py"])

if branches == 'rashid band 5 - extrusion_free':
    nombre_proyecto = "Band2+3_Hybrid_Rashid_extruded_free"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_5_free_param_extruded.py"])
if branches == 'winged band 2+3':
    nombre_proyecto = "Band2+3_Hybrid_Winged"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_23_extruded.py"])

if branches == 'winged band 2+3 free param':
    nombre_proyecto = "Band2+3_Hybrid_Winged_freeparam"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_23_extruded_freeparam.py"])
if branches == '3-winged band 2+3 free param':

    nombre_proyecto = "Band2+3_Hybrid_3_Winged_freeparam"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_23_3_extruded_freeparam.py"])
if branches =='3-winged band 2+3 fixed param':
    nombre_proyecto = "Band2+3_Hybrid_3_Winged_fixedparam"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_23_3_extruded_fixedparam.py"])

if branches =='3-winged band 2+3 flex distribution':
    nombre_proyecto = "Band2+3_Hybrid_8br_3_extruded_fixedparam_flex"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_23_3_extruded_fixedparam_flex.py"])

"""Ojo.. aqui se está usando el mismo archivo de hfss para evaluar 
dos escenarios: parametros de extrusiones fijos pero reduciendo el tamaño del vector nominal"""
if branches =='3-winged band 2+3 fixed param reduced vector':
    nombre_proyecto = "Band2+3_Hybrid_3_Winged_fixedparam"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_23_3_extruded_fixedparam_reducedVector.py"])    

if branches =='12-br 3-winged band 2+3 fixed param reduced vector':
    nombre_proyecto = "Band2+3_Hybrid_12br_3_extruded_fixedparam"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_23_12branch_3_extruded_fixedparam_reducedVector.py"])    

if branches =='10-br 3-winged band 2+3 flex distribution':
    nombre_proyecto = "Band2+3_Hybrid_10br_3_extruded_fixedparam_flex"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_23_3_10Br_extruded_fixedparam_flex.py"])    

if branches =='12-br 3-winged band 2+3 flex distribution':
    nombre_proyecto = "Band2+3_Hybrid_12br_3_extruded_fixedparam_flex"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_23_3_12Br_extruded_fixedparam_flex.py"])    


if branches =='3-winged band 2+3 Rashid Parameters Vector':
    nombre_proyecto ="Band2+3_Hybrid_8br_3_extruded_BenchmarkRashid"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_2+3_extruded_rashid_parameters.py"])    

if branches =='3-winged band 2+3 10 Branch Rashid Parameters':
    nombre_proyecto ="Band2+3_Hybrid_10br_3_extruded_BenchmarkRashid"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_2+3_10Br_extruded_rashid_parameters.py"])    
if branches =='3-winged band 2+3 12 Branch Rashid Parameters':
    nombre_proyecto ="Band2+3_Hybrid_12br_3_extruded_BenchmarkRashid"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_2+3_12Br_extruded_rashid_parameters.py"])    

if branches =='3-winged band 2+3 14 Branch Rashid Parameters':
    nombre_proyecto ="Band2+3_Hybrid_14br_3_extruded_BenchmarkRashid"
    nombre_diseno = "Optimized Hybrid"
    subprocess.run(["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                "-RunScript","hybrids/Hybrid_Design_band_2+3_14Br_extruded_rashid_parameters.py"])    


