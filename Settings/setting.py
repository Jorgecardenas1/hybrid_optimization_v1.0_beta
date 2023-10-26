
# -*- coding: utf-8 -*-

from sys import platform
import logging
from Simulation import global_ 
import os
from datetime import datetime


def check_os():

    if platform == "linux" or platform == "linux2":
        # linux
        return platform
    elif platform == "darwin":
        # OS X
        return platform

    elif platform == "win32":
        # Windows...
        return platform

def check_current_path():
    return os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

def set_direccion_ansoft():
    global_.direccion_Ansoft = r"C:\\Users\\Astrolab\\Documents\\Ansoft\\"          


def set_folders():

    global_.HFSS_RUN_STRINGS=["C:\Program Files\\AnsysEM\\AnsysEM19.0\\Win64\\ansysedt.exe",
                    "-RunScriptAndExit", os.path.join( os.path.normpath(global_.direccion_archivos),r"simulacion.py")]
    files_dir = os.path.join( os.path.normpath(global_.direccion_archivos),r"output",global_.simulationID,global_.file_folder)
    figs_dir = os.path.join( os.path.normpath(global_.direccion_archivos),r"output",global_.simulationID,global_.figures_folder)#crear carpeta para files_dir imagenes oscar
    
    try:
        os.makedirs(files_dir)
    except OSError:
        logging.warning('%s folder not created', global_.file_folder)
        #print ("La creacion de la direccion %s fallo o ya existia" % files_dir)
    else:
        logging.warning('%s folder created', global_.file_folder)
        #print ("Se creo exitosamente la direccion %s " % files_dir)
        
    os.chdir(global_.direccion_archivos)

    #acá coloco el mismo mensaje de inicio del programa para carpeta "figuras"

    try:

        os.makedirs(figs_dir)    
    except OSError:
        logging.warning('%s folder not created', global_.figures_folder)
        #print ("La creacion de la direccion %s fallo o ya existia" % figs_dir)
    else:
        logging.warning('%s folder created',global_.figures_folder)
        #print ("Se creo exitosamente la direccion %s " % figs_dir)
        
    os.chdir(global_.direccion_archivos)

def start_timing():
    global_.start_time = datetime.now()

def get_elapsed_time():
    diff=datetime.now()-global_.start_time
    return str(diff.total_seconds())

