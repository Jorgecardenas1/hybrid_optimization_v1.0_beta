
# -*- coding: utf-8 -*-


import Simulation.global_ as global_
import logging
import subprocess
import os
import numpy as np
import matplotlib.pyplot as plt
import uuid
# modulo que contiene strings de mensajes
import Settings.messages as msg
import shutil


"""Simulation Object to control simulation properties"""
class Simulation:
    date = ""
    elapsed_time = 0
    id=0
    
    def __init__(self, date):
        self.id_ = 0
        self.date = date
        

    def set_simulation_params(self):

        if global_.branches == 5:
            pass

        if global_.branches == 7:
            global_.n_variables = 12
            global_.iteraciones = 15
            global_.n_particulas = 4

            global_.nominales = [0.4, 0.6, 0.6, 0.6, 0.6, 0.3, 1.2, 2.3, 3, 0.64,2.8,1.3]

            global_.var_min = [0.1,0.15,0.15,0.15,0.15,0.1,1.0,2.0,2.9,0.75,2.6,1.35]
            global_.var_max = [1.0,0.8,0.8,0.8,0.8,0.8,1.8,2.8,3.5,1.0,3.1,1.54] 


        if global_.branches == 8:
            global_.n_variables = 10
            global_.iteraciones = 30
            global_.n_particulas = 7

            
            global_.nominales = [0, 0.6, 0.6, 0.6, 0.6, 1, 2, 3, 4, 0.64]

            global_.var_min = [0,0.1,0.1,0.1,0.1,0.1,1.0,2.1,3,0.5]
            global_.var_max = [0,1.5,1.5,1.5,1.5,1.5,3.0,5,6,0.8] 
        


        if global_.branches == 80:
            global_.n_variables = 12
            global_.iteraciones = 20
            global_.n_particulas = 4
            global_.A_dimension_index = 10
            global_.branch_number = 8


            """Standard set of variables and vectors"""
            global_.nominales = [0,0.325,0.325,0.325,0.325,0.26,0.8,1.5,2.5, 0.75,2.6,1.35 ]
            global_.var_min =   [0,0.28,0.28,0.28,0.26,0.43,0.96,1.95,2.8,0.8,2.7,1.3]
            global_.var_max =   [0,0.3,0.3,0.3,0.28,0.45,0.99,1.98,3.0,0.85,2.72,1.35]


        if global_.branches=='Band 2+3 8 br - flex':

            global_.n_variables = 12
            global_.iteraciones = 20
            global_.n_particulas = 4
            global_.A_dimension_index = 10
            global_.branch_number = 8

            global_.nominales = [0,0.25,0.25,0.25,0.25, 0.8,0.8,0.8,0.8,0.85,2.55,1.3]
            global_.var_min =[0,0.255,0.255,0.255,0.26,  0.85,0.85,0.85,0.85,0.85,2.48,1.25]
            global_.var_max = [0,0.288,0.288,0.288,0.35, 0.9,0.9,0.9,0.9,0.9,2.55,1.35]
            #Vec


  
        if global_.branches == "Band 3 - 8Br":
            global_.n_variables = 12
            global_.iteraciones = 15
            global_.n_particulas = 3


            #this set enables creation of 8 branches
            global_.nominales = [0,0.325,0.325,0.325,0.325,0.26,0.8,1.5,2.6, 0.75,2.6,1.35 ]
            global_.var_min = [0,0.1,0.1,0.1,0.1,0.1,0.75,1.6,2.3,0.6,2.5,1.25]
            global_.var_max =[0,0.4,0.4,0.4,0.4,0.7,1.5,2.2,4.0,0.7,2.7,1.35]
        
        if global_.branches=="Band 3 - flat 8Br Flex":
            global_.n_variables = 12
            global_.iteraciones = 20
            global_.n_particulas = 5
            global_.A_dimension_index = 10
            global_.branch_number = 8

            """ 14 parámetros"""

            global_.nominales = [0.0,0.211,0.297,0.264,0.224, 0.4, 1.2, 2.3, 3, 0.866, 2.7, 1.3]
            global_.var_min =[0,0.27,0.27,0.27,0.27,  0.4,0.4,0.4,0.4,0.4,2.62,1.31]
            global_.var_max = [0,0.33,0.33,0.33,0.33, 0.6,0.6,0.6,0.6,0.6,2.72,1.351]
            #Vec

        if global_.branches=="Band 3 - 8Br Flex":

            global_.n_variables = 14
            global_.iteraciones = 20
            global_.n_particulas = 7
            global_.A_dimension_index = 10
            global_.branch_number = 8

            """ 14 parámetros"""

            global_.nominales = [0.0,0.211,0.297,0.264,0.224, 0.4, 1.2, 2.3, 3, 0.866, 2.7, 1.3, 0.05376809036840973, 0.09640358945074504]
            global_.var_min =[0,0.28,0.28,0.28,0.28,  0.5,0.5,0.5,0.5,0.5,2.54,1.27, 0.18, 0.18]
            global_.var_max = [0,0.33,0.4,0.4,0.4, 0.7,0.7,0.7,0.7,0.7,2.54,1.27, 0.3, 0.35]
            #Vec     
        
        if global_.branches == "Band 3 - 12Br Flex":
            global_.n_variables = 18
            global_.iteraciones = 18
            global_.n_particulas = 7
            global_.A_dimension_index = 14
            global_.branch_number = 12

            global_.nominales = [0,0.25,0.25,0.25,0.25, 0.8,0.8,0.8,0.8,0.85,2.55,1.3, 0.22, 0.27]
            global_.var_min =[0,0.18,0.21,0.15,0.17,0.21,0.21,  0.37,0.41,0.4,0.38,0.34,0.41,0.69,2.58,1.29, 0.23, 0.23]
            global_.var_max = [0,0.19,0.22,0.16,0.18,0.22,0.22,    0.38,0.42,0.41,0.38,0.35,0.42,0.69,2.58,1.29, 0.26, 0.26]



        if global_.branches == 'rashid band 5': 
            """this simulation runs a normal hybrid, without extrusions, but int rashid band"""
            global_.n_variables = 12
            global_.iteraciones = 15
            global_.n_particulas = 5
  
            #vector original Rashid
            #[0, 0.118, 0.118, 0.118, 0.183, 0.256, 0.768, 1.28, 1.861, 0.383, 1.26, 0.63, 0.08, 0.394]
          
            
            scale=2.1
            global_.nominales = [0, 0.287, 0.251, 0.242, 0.129, 0.3, 1.3, 2.3, 3.2, 0.866, 2.8, 1.4]
            global_.nominales = np.divide( global_.nominales , scale).tolist()
            
            global_.var_min = [0,0.05,0.05,0.05,0.05,0.2,0.8,1.0,2.0,0.75,2.6,1.35]
            global_.var_min = np.divide( global_.var_min , scale).tolist()

            global_.var_max =[0,0.8,0.8,0.8,0.8,1.1,2.2,3.2,5.0,1.0,3.1,1.54]
            global_.var_max = np.divide( global_.var_max , scale).tolist()
        

        if global_.branches == 'rashid band 5 - extrusion': 
            """Here we use the original rashid geometry in terms of our vector notation
            to optimize by changing max and min values"""
            global_.n_variables = 14
            global_.iteraciones = 20
            global_.n_particulas = 3
        
            global_.nominales = [0, 0.118, 0.118, 0.118, 0.183, 0.256, 0.768, 1.28, 1.8245, 0.383, 1.3, 0.63, 0.08, 0.394]
            global_.var_min = [0, 0.05, 0.05, 0.05, 0.05, 0.15, 0.6, 1.0, 1.5, 0.37, 1.29, 0.6, 0, 0.01]
            global_.var_max =[0, 0.4, 0.4, 0.4, 0.4, 0.55, 1.8, 2.0, 2.8, 0.39, 1.33, 0.65, 0.2, 0.5]
        
        if global_.branches == 'rashid band 5 benchmark H1H2': 
            """Here we use the original rashid geometry even with branches H1 H2 and distance between them L"""
            global_.n_variables = 9
            global_.iteraciones = 20
            global_.n_particulas = 4

            """ [0, H1, H2, L, distance main gudes, A, B, a,b]"""      
            global_.nominales = [0, 0.137, 0.189, 0.256, 0.383, 1.3, 0.63, 0.08, 0.394]
            global_.var_min = [0, 0.1, 0.08, 0.25, 0.3, 1.29, 0.6, 0.08, 0.08]
            global_.var_max =[0, 0.2, 0.2, 0.5, 0.39, 1.33, 0.7, 0.150, 0.150]

        if global_.branches == 'rashid band 5 - extrusion_free':
            global_.n_variables = 14
            global_.iteraciones = 10
            global_.n_particulas = 5
        
            global_.nominales = [0, 0.118, 0.118, 0.118, 0.183, 0.256, 0.768, 1.28, 1.8245, 0.383, 1.3, 0.63, 0.08, 0.394]
            global_.var_min = [0, 0.05, 0.05, 0.05, 0.05, 0.15, 0.6, 1.0, 1.5, 0.37, 1.29, 0.6, 0.01, 0.1]
            global_.var_max =[0, 0.4, 0.4, 0.4, 0.4, 0.55, 1.8, 2.0, 2.8, 0.39, 1.33, 0.65, 0.2, 0.4]
        
        if global_.branches == 'winged band 2+3': 
           
            global_.n_variables = 14
            global_.iteraciones = 10
            global_.n_particulas = 3
             #[0, 0.118, 0.118, 0.118, 0.183, 0.256, 0.768, 1.28, 1.861, 0.383, 1.26, 0.63, 0.08, 0.394]
            lambda_4=0.81910
            lambda_8=0.40955

      
            global_.nominales = [0,0.325,0.325,0.325,0.325,0.26,0.8,1.5,2.5, 0.75,2.6,1.35,0.16,0.8 ]
            global_.var_min = [0,0.05,0.05,0.05,0.05,0.1,1.0,2.0,3.0,0.7,2.7,1.35,0.01,0.1]
            global_.var_max =[0,0.8,0.8,0.8,0.8,0.9,1.9,3.0,4.5,0.82,3.1,1.54,0.18,1.0]
        
        if global_.branches == 'winged band 2+3 free param':
            global_.n_variables = 14
            global_.iteraciones = 10
            global_.n_particulas = 3

            #vector original Rashid
            #[0, 0.118, 0.118, 0.118, 0.183, 0.256, 0.768, 1.28, 1.861, 0.383, 1.26, 0.63, 0.08, 0.394]
            lambda_4=0.81910

            global_.nominales = [0,0.325,0.325,0.325,0.325,0.26,0.8,1.5,2.5, 0.75,2.6,1.35,0.16,0.8 ]
            global_.var_min = [0,0.05,0.05,0.05,0.05,0.1,0.7,1.6,2.3,0.7,2.69,1.26,0.01,0.1]
            global_.var_max =[0,0.5,0.5,0.5,0.5,0.6,1.5,2.2,4.0,0.82,2.79,1.4,0.18,1.0]

        if global_.branches == '3-winged band 2+3 free param':
            global_.n_variables = 17
            global_.iteraciones = 10
            global_.n_particulas = 5
            global_.A_dimension_index = 10
            global_.branch_number = 8

            """Este vector es más refinado de la simulacion"""
            global_.nominales = [0.0, 0.24078870035015237, 0.2088882350947257, 0.3046551481567814, 0.29486602951401014, 0.1712432435747554, 0.9756184669112243, 2.4602390184511043, 3.0843548224288435, 0.7927759344357268, 2.6940146259272035, 1.1693606133580408, 0.05376809036840973, 0.5686867375243781, 2.459677504820723, 0.09640358945074504, 0.8134903271759962]
            global_.var_min = [0,0.18,0.18,0.18,0.19,   0.28,0.9,2.0,3.9,0.7,2.62,1.31,0.2,0.2,0.9,0.18,0.8]
            global_.var_max = [0,0.21,0.25,0.25,0.28,0.31,1.3,2.3,4.2,0.8,2.62,1.31,2.5,0.35,3,0.35,1.5]    



        if global_.branches == '3-winged band 2+3 fixed param':
            
            
            global_.n_variables = 14
            global_.iteraciones = 20
            global_.n_particulas = 5
            global_.A_dimension_index = 10
            global_.branch_number = 8

            """ 14 parámetros"""
            global_.nominales = [0, 0.264, 0.260, 0.264, 0.274, 0.245, 1.229, 2.260, 3.491, 0.741, 2.611, 1.30, 0.05376809036840973, 0.09640358945074504]
            global_.var_min =[0,0.2,0.2,0.2,0.2,  0.3,1.0,2.0,3.0,0.7,2.54,1.25, 0.17, 0.18]
            global_.var_max = [0,0.31,0.31,0.31,0.37, 0.8,1.7,2.8,4.5,0.9,2.6,1.3, 0.19, 0.20]
            #Vector escalado rashid que funcionó [0, 0.287, 0.32, 0.77, 0.848, 2.52, 1.26, 0.21, 0.273]
            
        if global_.branches == '3-winged band 2+3 flex distribution':
            
            
            global_.n_variables = 14
            global_.iteraciones = 20
            global_.n_particulas = 6
            global_.A_dimension_index = 10
            global_.branch_number = 8

            """ 14 parámetros"""

            global_.nominales = [0, 0.264, 0.260, 0.264, 0.274, 0.245, 1.229, 2.260, 3.491, 0.741, 2.611, 1.30, 0.22, 0.27]
            global_.var_min =[0,0.15,0.15,0.15,0.15,  0.2,0.2,0.2,0.2,0.74,2.54,1.2, 0.25, 0.25]
            global_.var_max = [0,0.5,0.5,0.5,0.5, 0.8,0.8,0.8,0.8,0.76,2.69,1.34, 0.35, 0.35]

 
        if global_.branches =='10-br 3-winged band 2+3 flex distribution':

            global_.n_variables = 16
            global_.iteraciones = 10
            global_.n_particulas = 10
            global_.A_dimension_index = 12
            global_.branch_number = 10

            # global_.nominales = [0,0.3,0.3,0.3,0.3,0.3, 0.8,0.8,0.8,0.8,0.8,0.85,2.55,1.3, 0.22, 0.27]
            # global_.var_min =[0,0.21,0.21,0.21,0.21,0.21,      0.75,0.75,0.75,0.75,0.75,0.8,2.5,1.25, 0.2, 0.2]
            # global_.var_max =[0,0.23,0.23,0.23,0.23,0.3,       0.85,0.85,0.85,0.85,0.85,0.9,2.58,1.3, 0.35, 0.35]
            [0.0, 0.178, 0.195, 0.217, 0.166, 0.206, 0.57, 0.66, 0.847, 0.561, 0.403, 0.869, 2.613, 1.3065, 0.191, 0.293]
            global_.nominales = [0,0.25,0.25,0.25,0.25, 0.8,0.8,0.8,0.8,0.85,2.55,1.3, 0.22, 0.27]
            global_.var_min =[0,0.16,0.15,0.15,0.15,0.15,  0.5,0.5,0.5,0.5,0.4,0.8,2.5,1.2, 0.185, 0.25]
            global_.var_max = [0,0.21,0.21,0.21,0.21,0.21, 0.9,0.9,0.9,0.9,0.9,0.9,2.63,1.35, 0.22, 0.3]
            #Vector escalado rashid que funcionó [0, 0.287, 0.32, 0.77, 0.848, 2.52, 1.26, 0.21, 0.273]
          

        if global_.branches =='12-br 3-winged band 2+3 flex distribution':

            global_.n_variables = 18
            global_.iteraciones =10
            global_.n_particulas = 4
            global_.A_dimension_index = 14
            global_.branch_number = 12


            global_.nominales = [0,0.25,0.25,0.25,0.25, 0.8,0.8,0.8,0.8,0.85,2.55,1.3, 0.22, 0.27]
            global_.var_min =[0,0.15,0.15,0.15,0.15,0.15,0.2,  0.62,0.62,0.62,0.62,0.62,0.62,0.71,2.6,1.3, 0.18, 0.18]
            global_.var_max = [0,0.20,0.2,0.2,0.2,0.2,0.28,    0.75,0.75,0.75,0.75,0.75,0.75,0.72,2.62,1.31, 0.22, 0.22]


        if global_.branches == '12-br 3-winged band 2+3 fixed param reduced vector':
            
            
            global_.n_variables = 18
            global_.iteraciones = 15
            global_.n_particulas = 3
            global_.A_dimension_index = 14
            global_.branch_number = 12

            """ 14 parámetros"""

            global_.nominales = [0.0,0.311,0.297,0.364,0.224,0.364,0.224, 0.4, 1.2, 2.3, 3,4,5, 0.766, 2.7, 1.3, 0.0537, 0.09640]
            global_.var_min =[0,0.19,0.19,0.19,0.19,0.19,0.19,  0.2,0.6, 1.0, 1.8, 2.9, 3.5,0.72,2.6,1.3, 0.001, 0.001]
            global_.var_max = [0,0.3,0.3,0.3,0.3,0.3,0.3,     0.4, 0.8, 1.6, 2.3, 3.3, 4.0,0.76,2.7,1.35, 0.01, 0.01]


        if global_.branches=='3-winged band 2+3 Rashid Parameters Vector':
            global_.n_variables = 9
            global_.iteraciones = 20
            global_.n_particulas = 7
            global_.A_dimension_index = 5

            global_.branch_number = 8

            """ [0, H1, H2, L, distance main gudes, A, B, a,b]"""  

            global_.nominales =  [0.0, 0.2877, 0.287, 0.53760, 0.753, 2.6, 1.3232, 0.168, 0.8274]
            global_.var_min =  [0.0, 0.24, 0.25, 0.7 , 0.8, 2.48, 1.24, 0.18, 0.22]
            global_.var_max = [0.0, 0.29, 0.33, 0.89, 0.9, 2.55, 1.25, 0.25, 0.3]


       #Vector escalado rashid que funcionó [0, 0.287, 0.32, 0.77, 0.848, 2.52, 1.26, 0.21, 0.273]
     
        #    scale=2.1
        #    global_.nominales = np.multiply( global_.nominales , scale).tolist()
            
        #    global_.var_min = np.multiply( global_.var_min , scale).tolist()

        #    global_.var_max = np.multiply( global_.var_max , scale).tolist()
        
        if global_.branches=='3-winged 10 br band 2+3 Rashid Parameters Vector':
            global_.n_variables = 9
            global_.iteraciones = 15
            global_.n_particulas = 7
            global_.A_dimension_index = 5
            global_.branch_number=10
            """ [0, H1, H2, L, distance main gudes, A, B, a,b]"""  

            global_.nominales =  [0.0, 0.2877, 0.287, 0.53760, 0.753, 2.6, 1.3232, 0.168, 0.8274]
            global_.var_min =  [0.0, 0.185, 0.185, 0.2, 0.7, 2.65, 1.35, 0.01, 0.01]
            global_.var_max = [0.0, 0.25, 0.25, 0.8, 0.77, 2.75, 1.325, 0.29, 0.29]


            #Next lines are to test band 2 
            #global_.nominales =  [0.0, 0.2877, 0.287, 0.53760, 0.753, 2.6, 1.3232, 0.168, 0.8274]
            #global_.var_min =  [0.0, 0.1, 0.1, 0.15, 0.7, 2.6, 1.3, 0.08, 0.08]
            #global_.var_max = [0.0, 0.4, 0.4, 1.5, 0.8, 2.9, 1.46, 0.2, 0.2]

        if global_.branches=='3-winged 12 br band 2+3 Rashid Parameters Vector':
            global_.n_variables = 9
            global_.iteraciones = 18
            global_.n_particulas = 8
            global_.A_dimension_index = 5
            global_.branch_number = 12
            """ [0, H1, H2, L, distance main gudes, A, B, a,b]"""  

            global_.nominales =  [0.0, 0.2877, 0.287, 0.53760, 0.753, 2.6, 1.27, 0.168, 0.8274]
            global_.var_min =  [0.0, 0.17, 0.23, 0.78 , 0.79, 2.62, 1.31, 0.2, 0.25]
            global_.var_max = [0.0, 0.19, 0.25, 0.80, 0.81, 2.62, 1.31, 0.21, 0.35]
            #El vector escalado desde rashid
            # [0, 0.287, 0.32, 0.77, 0.848, 2.52, 1.26, 0.21, 0.273]



        if global_.branches=='3-winged 14 br band 2+3 Rashid Parameters Vector':
            global_.n_variables = 9
            global_.iteraciones = 10
            global_.n_particulas = 6
            global_.A_dimension_index = 5
            global_.branch_number = 12

            """ [0, H1, H2, L, distance main gudes, A, B, a,b]"""  

            global_.nominales =  [0.0, 0.2877, 0.287, 0.53760, 0.753, 2.6, 1.27, 0.168, 0.8274]
            global_.var_min =  [0.0, 0.14, 0.15, 0.6 , 0.71, 2.52, 1.25, 0.17, 0.18]
            global_.var_max = [0.0, 0.2, 0.28, 0.75, 0.73, 2.62, 1.31, 0.19, 0.23]
  
        if global_.branches == 9:
            global_.n_variables = 10
            global_.iteraciones = 5
            global_.n_particulas = 5

            
            global_.nominales = [0.3, 0.3, 0.3, 0.3, 0.3, 1.5, 2.5, 3, 4, 0.64]
            global_.var_min = [0.2,0.1,0.1,0.1,0.1,0.6,0.8,1.5,2.5,0.1]
            global_.var_max = [1.1,1.1,1.1,1.1,1.1,1.8,3.0,3.9,4.5,0.8]  

        if global_.branches == 100:
            global_.n_variables = 14
            global_.iteraciones = 10
            global_.n_particulas = 3
            global_.A_dimension_index = 12


            #[0, 0.41, 0.33, 0.3, 0, 0.505, 1.57, 2.845, 0, 0.92]
            #[0.0, 0.343, 0.29, 0.142, 0.359, 0.3, 1.3, 2.3, 3.2, 0.8, 2.7, 1.4]
            #incorporating previous knowledge of max and min
            global_.nominales = [0, 0.287, 0.251, 0.242, 0.129,0.1, 0.3, 1.3, 2.0, 2.5,3, 0.9, 2.8, 1.4]
            global_.var_min = [0,0.1,0.1,0.1,0.1,0.1,0.2,1.0,2.0,3.0,3.5, 0.75,2.6,1.3] 
            global_.var_max = [0,0.4,0.4,0.4,0.4,0.4,0.9,1.8,2.8,3.5,4.5, 0.8,2.75,1.54]
        
        logging.info(msg.PARAMS_SET)
    
    def get_simulation_params(self):
        params = {
            "simulation_type":global_.branches,
            "num_branches":str(global_.branch_number),
            "n_variables":global_.n_variables,
            "iterations":global_.iteraciones,
            "n_particles":global_.n_particulas,
            "nominal":global_.nominales,
            "var_min":global_.var_min,
            "var_max":global_.var_max
        }
        return params

    

#=============================================================================
# THIS customized FUNCTION CALLS 'funciones.py' FILE AND GENERATES THE DATA
# TO BE USED BY THE OPTIMIZER.

def create_sim_file(particle, i, j):
    
    particle = particle.round(4)  
    if global_.A_dimension_index>6 and global_.A_dimension_index<12:

        L = sum(particle[:8])+4*3.33
    elif global_.A_dimension_index>12:
        L = sum(particle[:13])+4*3.33
    else:
        L = sum(particle[:2])* (global_.branch_number+1)+4*3.33

    tag = "_"+str(i)+"_"+str(j)     #esta linea genera el string _i_j
    var = "[" + ", ".join([str(x) for x in particle]) + "]" #Generar string del array de datos de la particula
    var_L = str(L)
    os.chdir( os.path.normpath(global_.direccion_archivos))
    
    f = open("simulacion.py", "w")   #abre un archivo para escribir

    direccion_dibujo = '"' + global_.direccion_Ansoft + global_.nombre_proyecto \
                + '.aedt"'
    f.write("import Simulation.funciones as fn\n")


    f.write("\n")
    f.write("import ScriptEnv\n")
    f.write("oDesktop.RestoreWindow()\n")
    f.write("oDesktop.OpenProject(" + direccion_dibujo + ")\n")
    f.write("oProject = oDesktop.SetActiveProject(" + '"'+global_.nombre_proyecto+'"' 
            + ")\n")

    f.write('fn.modificaArreglo(oProject,"' + global_.nombre_variables + ' ","' + var 
            + global_.unidades + '")\n')
    
    f.write('fn.modificaArreglo(oProject,"L","' + var_L 
            + global_.unidades + '")\n')

    f.write('oDesign = oProject.SetActiveDesign("' +global_.nombre_diseno + '")\n')
    f.write("oDesign.AnalyzeAll()")
    f.write("\n")
#    f.write("fn.creaGain(oProject,0,'" + tag + "')\n")
#    f.write("fn.creaGain(oProject,90,'" + tag + "')\n")

    f.write('oModule = oDesign.GetModule("OutputVariable")\n')
    f.write('oModule.CreateOutputVariable("AmpImbalance", "abs(dB(s(2,1)/s(3,1)))", "Setup1 : Sweep", "Modal Solution Data", [])\n')
    f.write('oModule.CreateOutputVariable("PhaseImb", "abs(arg(S(2,1)/S(3,1)))", "Setup1 : Sweep", "Modal Solution Data", [])\n')


    f.write("fn.creaS11(oProject,'" + tag + "','"+ global_.simulationID +"')\n")
    f.write("fn.creaS21(oProject,'" + tag + "','"+ global_.simulationID +"')\n")
    f.write("fn.creaS31(oProject,'" + tag + "','"+ global_.simulationID +"')\n")
    f.write("fn.creaS41(oProject,'" + tag + "','"+ global_.simulationID +"')\n")
    f.write("fn.creaAmpImb(oProject,'" + tag + "','"+ global_.simulationID +"')\n")
    f.write("fn.creaPhaseImb(oProject,'" + tag + "','"+ global_.simulationID +"')\n")

    f.close()

    
## Launches HFSS simulation file
def run_simulation_hfss(hfss_run_strings):

    subprocess.run(hfss_run_strings)

    logging.info(msg.SIM_PARTICLE_FINISHED)

## read the simulation results
def read_simulation_results(i,j):
    
    files_location = os.path.join( os.path.normpath(global_.direccion_archivos),r"output",global_.simulationID,r"files")

    os.chdir(files_location)
    direccion_graficas_s11= global_.direccion_archivos+ "\\output\\"+global_.simulationID+"\\figures\\S11"+"_" + str(i)+"_"+str(j)
    
    try:
        s11 = np.genfromtxt("datosS11_"+str(i)+"_"+str(j)+
                     ".csv", skip_header = 1, delimiter = ',')
    
        direccion_graficas_s11= global_.direccion_archivos+ "\\output\\"+global_.simulationID+"\\figures\\S11"+"_" + str(i)+"_"+str(j)
   
    except:
        filename="datosS11_"+str(i-1)+"_"+str(j)+".csv"
        new_filename="datosS11_"+str(i)+"_"+str(j)+".csv"
        copy_rename(filename,new_filename)
        
        s11 = np.genfromtxt("datosS11_"+str(i)+"_"+str(j)+
                     ".csv", skip_header = 1, delimiter = ',')
        direccion_graficas_s11= global_.direccion_archivos+ "\\output\\"+global_.simulationID+"\\figures\\S11"+"_" + str(i)+"_"+str(j)

    try:

    
        s21 = np.genfromtxt("datosS21_"+str(i)+"_"+str(j)+
                     ".csv", skip_header = 1, delimiter = ',')
    
        direccion_graficas_s21= global_.direccion_archivos+ "\\output\\"+global_.simulationID+"\\figures\\S21"+"_" + str(i)+"_"+str(j)
    except:

        filename="datosS21_"+str(i-1)+"_"+str(j)+".csv"
        new_filename="datosS21_"+str(i)+"_"+str(j)+".csv"
        copy_rename(filename,new_filename)

        s21 = np.genfromtxt("datosS21_"+str(i)+"_"+str(j)+
                     ".csv", skip_header = 1, delimiter = ',')
        
        direccion_graficas_s21= global_.direccion_archivos+ "\\output\\"+global_.simulationID+"\\figures\\S21"+"_" + str(i)+"_"+str(j)

    try:

    
        s31 = np.genfromtxt("datosS31_"+str(i)+"_"+str(j)+
                     ".csv", skip_header = 1, delimiter = ',')
    
        direccion_graficas_s31= global_.direccion_archivos+ "\\output\\"+global_.simulationID+"\\figures\\S31"+"_" + str(i)+"_"+str(j)
    
    except:
        
        filename="datosS31_"+str(i-1)+"_"+str(j)+".csv"
        new_filename="datosS31_"+str(i)+"_"+str(j)+".csv"
        copy_rename(filename,new_filename)

        s31 = np.genfromtxt("datosS31_"+str(i)+"_"+str(j)+
                     ".csv", skip_header = 1, delimiter = ',')
        direccion_graficas_s31= global_.direccion_archivos+ "\\output\\"+global_.simulationID+"\\figures\\S31"+"_" + str(i)+"_"+str(j)

    try:
       

        s41 = np.genfromtxt("datosS41_"+str(i)+"_"+str(j)+
                     ".csv", skip_header = 1, delimiter = ',')
    except:
        filename="datosS41_"+str(i-1)+"_"+str(j)+".csv"
        new_filename="datosS41_"+str(i)+"_"+str(j)+".csv"
        copy_rename(filename,new_filename)

        s41 = np.genfromtxt("datosS41_"+str(i)+"_"+str(j)+
                     ".csv", skip_header = 1, delimiter = ',')
    #derivative_data = np.genfromtxt("Derivative_"+str(i)+"_"+str(j)+".csv", skip_header = 1, delimiter = ',')
    #Plot S11 and S21

    try:
        amp_imb = np.genfromtxt("amp_imb_"+str(i)+"_"+str(j)+
                     ".csv", skip_header = 1, delimiter = ',')
    
        direccion_graficas_amp= global_.direccion_archivos+ "\\output\\"+global_.simulationID+"\\figures\\amp_imb"+"_" + str(i)+"_"+str(j)
   
    except:
        filename="amp_imb_"+str(i-1)+"_"+str(j)+".csv"
        new_filename="amp_imb_"+str(i)+"_"+str(j)+".csv"
        copy_rename(filename,new_filename)
        
        amp_imb = np.genfromtxt("amp_imb_"+str(i)+"_"+str(j)+
                     ".csv", skip_header = 1, delimiter = ',')
        direccion_graficas_amp= global_.direccion_archivos+ "\\output\\"+global_.simulationID+"\\figures\\amp_imb"+"_" + str(i)+"_"+str(j)

    try:
        pha_imb = np.genfromtxt("pha_imb_"+str(i)+"_"+str(j)+
                     ".csv", skip_header = 1, delimiter = ',')
    
        direccion_graficas_pha= global_.direccion_archivos+ "\\output\\"+global_.simulationID+"\\figures\\pha_imb"+"_" + str(i)+"_"+str(j)
   
    except:
        filename="pha_imb_"+str(i-1)+"_"+str(j)+".csv"
        new_filename="pha_imb_"+str(i)+"_"+str(j)+".csv"
        copy_rename(filename,new_filename)
        
        pha_imb = np.genfromtxt("pha_imb_"+str(i)+"_"+str(j)+
                     ".csv", skip_header = 1, delimiter = ',')
        direccion_graficas_pha= global_.direccion_archivos+ "\\output\\"+global_.simulationID+"\\figures\\pha_imb"+"_" + str(i)+"_"+str(j)


    dydx1_31 = np.gradient(s31[:,1],s31[:,0])
    dydx2_31 = np.gradient(dydx1_31,s31[:,0])

    dydx1_21 = np.gradient(s21[:,1],s21[:,0])
    dydx2_21 = np.gradient(dydx1_21,s31[:,0])
    #print("second derivative max"+str(rating))
    
    data_to_plot=[dydx2_31, s31[:,0], dydx2_21, s31[:,0]]

    create_plot(s11,s41,'Frequency (GHz)',r'S11,S41 (dB)',direccion_graficas_s11,[],-20)
   
    #Plot S31 and S41
    create_plot(s31,s21,'Frequency (GHz)',r'S31,S21 (dB)',direccion_graficas_s31,data_to_plot,-3)

    create_plot_imb(amp_imb,'Frequency (GHz)',r'Amplitude Imbalance (dB)',direccion_graficas_amp,1)
    #create_plot_imb(pha_imb,'Frequency (GHz)',r'Phase Imbalance (Grad)',direccion_graficas_pha,90)


    os.chdir(global_.direccion_archivos)

    return s11,s21,s31,s41, amp_imb


def create_plot(data_1, data_2,label_x, label_y, save_path,derivative_data,boundary):
     #Plot S11 and S21
    figure=plt.figure(figsize=(8,6))
    plt.plot(data_1[:,0],data_1[:,1])
    plt.plot(data_2[:,0],data_2[:,1])
    plt.axhline(y=boundary, color='r', linestyle='-')
    plt.axhline(y=boundary+0.5,color='r', alpha=0.7, linestyle='-')
    plt.axhline(y=boundary-0.5, color='r', alpha=0.7, linestyle='-')

    #if derivative_data!=[]:
       # plt.plot(derivative_data[1],derivative_data[0],alpha=0.5)
       # plt.plot(derivative_data[3],derivative_data[2],alpha=0.5)
    
    plt.plot()
    plt.ylabel(label_y,fontsize=15)
    plt.xlabel(label_x,fontsize=15)
    plt.tick_params(axis='both', which='major', labelsize=15)
    plt.grid(True)
    plt.grid(color = '0.5', linestyle = '--', linewidth = 1.5)
    plt.show
    plt.savefig(save_path)
    plt.close(figure)

def create_plot_imb(data_1,label_x, label_y, save_path,boundary):
     #Plot S11 and S21
    figure=plt.figure(figsize=(8,6))
    plt.plot(data_1[:,0],data_1[:,1])
    plt.axhline(y=boundary, color='r', linestyle='-')

    plt.plot()
    plt.ylabel(label_y,fontsize=15)
    plt.xlabel(label_x,fontsize=15)
    plt.tick_params(axis='both', which='major', labelsize=15)
    plt.grid(True)
    plt.grid(color = '0.5', linestyle = '--', linewidth = 1.5)
    plt.show
    plt.savefig(save_path)
    plt.close(figure)



def copy_rename(old_file_name, new_file_name):

        files_location = os.path.join( os.path.normpath(global_.direccion_archivos),r"output",global_.simulationID,r"files")

        print(old_file_name)
        print(new_file_name)
        os.chdir(files_location)
        shutil.copy(old_file_name,new_file_name)    
