# -*- coding: utf-8 -*-

"""
pso.py
Functions related to implementation of PSO algorithm.


"""



from numpy.core.records import array
import Simulation.global_ as global_
from PSO import fitness_func as fit

import os

import numpy as np
import importlib

import matplotlib.pyplot as plt
from scipy import stats
from scipy import integrate
from sklearn.metrics import mean_squared_error

from numpy.random import seed
from numpy.random import randn


#seed control
#seed(1)



class Particle:
    """
    Particle class enabling the creation of multiple and dynamic number of particles.
    """
    id_ = 0
    values_array = []

    def __init__(self, id ):
        self.id_=id

        

    def random_array(self, array_size):
        self.values_array = np.array(np.random.random_sample(array_size))

    def fill_zeros_array(self, array_size):
       self.values_array = np.zeros(array_size)
    
    def reset_xParticles_id_counter(self):
        self.id_ = 0


class Swarm:
    
    phiv=0.9

    particles=[] # array with all particles part of the swar
    x_particles=[] # array with all particles part of the swar
    best_index=0 #best integer describing the index corresponding the best particle in 
                #particles array
    vmax = []
    velocidades = []
    gbest = 0  #global  best
    pbest =[]
    pg = []
    variables_number=0

    def __init__(self, particles_number, variables_number, var_max, var_min):
        #swarm variables
        self.particles_number = particles_number
        self.variables_number = variables_number

        #Set variations
        
        self.var_max = np.array(var_max)
        self.var_min = np.array(var_min)
        self.particles = []
        self.velocidades = np.zeros([global_.n_particulas,global_.n_variables])
        self.pbest = np.zeros(global_.n_particulas)
        self.pg = np.zeros(global_.n_variables)

    """Create particles swarm"""
    def create(self):
        
        self.particles = [Particle(i) for i in range(self.particles_number )]
        self.x_particles = [Particle(i) for i in range(self.particles_number  )]
        print("particulas creadas:"+str(len(self.particles)))

        interval_array=np.array(self.var_max) - np.array(self.var_min)
        self.vmax = interval_array * 0.6

        for particle in self.particles:
            #Generate random array for each particle
            particle.random_array(self.variables_number)
            #Scale the random values
            particle.values_array = particle.values_array*(self.var_max-self.var_min) + self.var_min

            # if particle.values_array[2] < particle.values_array[1]:
                
            #     random = np.random.random_sample()
            #     maximo = particle.values_array[1]-0.1
            #     particle.values_array[2] = random*(maximo-self.var_min[2]) + self.var_min[2]

            """pendiete por revisar"""
            """  if particulas[i,2] > particulas[i,1]:
            random = np.random.random_sample()
            maximo = particulas[i,1]-1
            particulas[i,2] = random*(maximo-var_min[j]) + var_min[j] """


    def nuevas_particulas(self,particulas_ant, pi_best, pg, vel_anterior, iteration):
    #     #Particulas => xi(t-1)
    #     #pi => individual optimal position!?
    #     # x son particulas que vienen definidas desde la creacion del enjambre
    #     # Solo se van actualizando en el transcurso de las iteraciones

        [item.fill_zeros_array(global_.n_variables) for item in self.x_particles]#llenar de ceros las particulas x

        vel = np.zeros([global_.n_particulas, global_.n_variables])#llenar de ceros la variable velocidad
        
        #Cambio dinámico de la inercia
        phi = 0.85 * self.phiv**(iteration-0.15) #0.8 y 1
        phi1 = 2.0 #valores que se pueden revisar. Seguir el valor el mejor fit propio
        phi2 = 2.1 #esto va valores componen self-knowledge.  seguir el mejor fit global
        damping = 0.7 #este damping se utiliza cando las particulas tocan los limitesmáximos y mínimos.

        for i in range(global_.n_particulas):
            
            rand = np.random.random() #valores entre 0 y 1
            particula_anterior=particulas_ant[i]

            for idx,dimension in enumerate(particula_anterior.values_array):
                """ 
                Calcula la velocidad de la particula i, dada su pi, pg y su velocidad
                 y posicion anterior 

                 pi => una particula especifica
                pbest=> su fitness value

                 pg => cualquier particula con la mejor solucion
                 gbest=> global bets

                 vi => velocidad anterior
                """

                """lo importante es la realción entre phi1 y phi2 , si es grande la velocidad de convergencia es alta
                si la relacion es pequeña, la velocidad es baja"""

       

                ###inercia +  atraccion a la mejor posicion de la particula i +  atraccion a la mejor posición global
                ###


                vel[i][idx] = phi * (vel_anterior[i][idx]) + phi1 * rand * ((pi_best[i].values_array)[idx] - dimension) + \
                     phi2 * rand * (pg[idx] - dimension)

                #Limiting velocity when too large
                if np.abs(vel[i][idx]) > self.vmax[idx]:
                    signo = np.sign(vel[i][idx])
                    vel[i][idx] =  self.vmax[idx]*signo
                    

                #Calculating new paticles
                self.x_particles[i].values_array[idx] = (particulas_ant[i].values_array[idx] + vel[i][idx]).round(decimals=2, out=None) ## xi(t-1)+vi( 

                """In this part we apply a bounce tecnique in the wall defined
                by the limits of max and min values for dimensions"""       
                if self.x_particles[i].values_array[idx] > self.var_max[idx]:
                    
                    
                    vel[i][idx]= vel[i][idx]*damping

                    self.x_particles[i].values_array[idx] = (self.var_max[idx]-np.abs(vel[i][idx])).round(decimals=2, out=None) ## xi(t-1)+vi(t)
                    

                elif self.x_particles[i].values_array[idx] < self.var_min[idx]:
                   
                    vel[i][idx]= vel[i][idx]*damping

                    self.x_particles[i].values_array[idx] = (self.var_min[idx]+np.abs(vel[i][idx]) ).round(decimals=2, out=None) ## xi(t-1)+vi(t)
                    
                else:
                    self.x_particles[i].values_array[idx] = (particulas_ant[i].values_array[idx] + vel[i][idx]).round(decimals=2, out=None) ## xi(t-1)+vi( 

                #This sections is used to force a=B*2
                if idx==global_.A_dimension_index+1:
                   self.x_particles[i].values_array[idx] = (self.x_particles[i].values_array[idx-1])*0.5
            if i>0:
                relation = self.drilling_relation( self.x_particles[i].values_array, self.x_particles[i].values_array[global_.A_dimension_index])
                print(relation)

        return self.x_particles,vel

    def drilling_relation(self,dimension,height):
        relation = (height/2)*1/dimension
        return relation



    def get_particle_best_fit(self, pi):
        index_pg = np.argmin(self.pbest) #toma el indice del particle best entre todas las particulas
        self.best_index = index_pg
        print("get particle best pg="+str(pi[index_pg].values_array))
        self.pg = pi[index_pg].values_array # seleccionar la mejor posicion-particula del array de particulas
        self.gbest = np.min(self.pbest)  #best global fitness 
        return index_pg

#Fitness func how close a given solution is to the optimum solution
def fitness(results,iter):
    
    importlib.reload(fit)

    s11 = results[0]
    s21 = results[1]
    s31 = results[2]
    s41 = results[3]
    amp_imbalance = results[4]
    #rashid 166-208
    #regions=[169,205] 

    #standar 2+3 band
    #regions = [70, 108]
    
    #band 3 84-116
    #regions = [68, 113]

    regions=[87,113] 
    
    num_of_constraints= 5 #we are evaluating two signals S31 y S41

    fitnessObj=fit.fitness_func()
    fitnessObj.regions = regions
    fitnessObj.set_priorization_regions(regions,s21[:,0],s21[:,1],s31[:,1],amp_imbalance[:,1]) #create array of subdivided domain values
    fitnessObj.set_bandwidth(s21[:,0]) #set bandwidtharray and normalize domain
    
    funcs = fitnessObj.set_sub_functions(deviation_s31,deviation_s21,oscillation_s31,oscillation_s21)
    fi_matrix = calculate_subfunction(funcs,fitnessObj,num_of_constraints)
    #you can create as many constraint as you want 


   

    _=fitnessObj.set_constraints('region_1_S31',true_value=-3.0, min_val=-3.5, max_val=-2.5,type_constraint='in_limit')
    _=fitnessObj.set_constraints('region_1_S21',true_value=-5.0, min_val=-3.5, max_val=-2.5,type_constraint='in_limit')
    _=fitnessObj.set_constraints('region_1_over_S31',true_value=-2, min_val=-3.5, max_val=-1,type_constraint='overshoot')
    _=fitnessObj.set_constraints('region_1_over_S21',true_value=-3, min_val=-5, max_val=-1,type_constraint='overshoot')


    _=fitnessObj.set_constraints('region_2_S31',true_value=-2.9, min_val=-3.3, max_val=-2.7,type_constraint='in_limit')
    _=fitnessObj.set_constraints('region_2_S21',true_value=-3.1, min_val=-3.3, max_val=-2.7,type_constraint='in_limit')
    _=fitnessObj.set_constraints('region_2_over_S31',true_value=-3.2, min_val=-3.5, max_val=-2.5,type_constraint='overshoot')
    _=fitnessObj.set_constraints('region_2_over_S21',true_value=-2.8, min_val=-3.5, max_val=-2.5,type_constraint='overshoot')


    _=fitnessObj.set_constraints('region_3_S31',true_value=-3.0, min_val=-3.5, max_val=-2.5,type_constraint='in_limit')
    _=fitnessObj.set_constraints('region_3_S21',true_value=-3.0, min_val=-3.5, max_val=-2.5,type_constraint='in_limit')
    _=fitnessObj.set_constraints('region_3_over_S31',true_value=-3, min_val=-3.5, max_val=-1,type_constraint='overshoot')
    _=fitnessObj.set_constraints('region_3_over_S21',true_value=-3, min_val=-5, max_val=-1,type_constraint='overshoot')


    _=fitnessObj.set_constraints('region_1_ampimb',true_value=1, min_val=0.0, max_val=0.9,type_constraint='in_limit')
    _=fitnessObj.set_constraints('region_2_ampimb',true_value=0.8, min_val=0.05, max_val=0.8,type_constraint='in_limit')
    _=fitnessObj.set_constraints('region_3_ampimb',true_value=1, min_val=0.0, max_val=0.8,type_constraint='in_limit')

    
    """Evaluate S31 Constraints"""
    evaluated_constraint_S31=[]

    evaluated_constraint_S31.append(
        fitnessObj.evaluate_constraints(data_to_asses=fitnessObj.Y_regions_s31[0],
                                        constrain_name='region_1_S31'))
    evaluated_constraint_S31.append(
        fitnessObj.evaluate_constraints(data_to_asses=fitnessObj.Y_regions_s31[1],
                                        constrain_name='region_2_S31'))
    evaluated_constraint_S31.append(
        fitnessObj.evaluate_constraints(data_to_asses=fitnessObj.Y_regions_s31[2],
                                        constrain_name='region_3_S31'))


    evaluated_constraint_S31.append(
        fitnessObj.evaluate_constraints(data_to_asses=fitnessObj.Y_regions_s31[0],
                                        constrain_name='region_1_over_S31'))
    evaluated_constraint_S31.append(
        fitnessObj.evaluate_constraints(data_to_asses=fitnessObj.Y_regions_s31[1],
                                        constrain_name='region_2_over_S31'))
    evaluated_constraint_S31.append(
        fitnessObj.evaluate_constraints(data_to_asses=fitnessObj.Y_regions_s31[2],
                                        constrain_name='region_3_over_S31'))
    """Evaluate S21 Constraints"""
    evaluated_constraint_S21=[]
    evaluated_constraint_S21.append(
        fitnessObj.evaluate_constraints(data_to_asses=fitnessObj.Y_regions_s21[0],
                                        constrain_name='region_1_S21'))
    evaluated_constraint_S21.append(
        fitnessObj.evaluate_constraints(data_to_asses=fitnessObj.Y_regions_s21[1],
                                        constrain_name='region_2_S21'))
    evaluated_constraint_S21.append(
        fitnessObj.evaluate_constraints(data_to_asses=fitnessObj.Y_regions_s21[2],
                                        constrain_name='region_3_S21'))

    evaluated_constraint_S21.append(
        fitnessObj.evaluate_constraints(data_to_asses=fitnessObj.Y_regions_s21[0],
                                        constrain_name='region_1_over_S21'))
    evaluated_constraint_S21.append(
        fitnessObj.evaluate_constraints(data_to_asses=fitnessObj.Y_regions_s21[1],
                                        constrain_name='region_2_over_S21'))
    evaluated_constraint_S21.append(
        fitnessObj.evaluate_constraints(data_to_asses=fitnessObj.Y_regions_s21[2],
                                        constrain_name='region_3_over_S21'))

    evaluated_constraint_ampImbalance=[]
    
    evaluated_constraint_ampImbalance.append(
        fitnessObj.evaluate_constraints(data_to_asses=fitnessObj.Y_regions_amp_imbalance[0],
                                        constrain_name='region_1_ampimb'))
    evaluated_constraint_ampImbalance.append(
        fitnessObj.evaluate_constraints(data_to_asses=fitnessObj.Y_regions_amp_imbalance[1],
                                        constrain_name='region_2_ampimb'))
    evaluated_constraint_ampImbalance.append(
        fitnessObj.evaluate_constraints(data_to_asses=fitnessObj.Y_regions_amp_imbalance[2],
                                        constrain_name='region_3_ampimb'))

    """Penalties for Dynamic Weighting"""
    num_of_regions= len(fitnessObj.normalized_regions_bandwidth)
    #Constraint for S31 Level
    #Constraint for S41 Level
    #Constraint for S31 Overshoot
    #Constraint for S41 Overshoot
    #ampimbalance level

    penalties = np.empty([num_of_regions, num_of_constraints])

    for i in range(num_of_regions):
        penalties[i][0] = 1-np.mean(evaluated_constraint_S31[i])#S31 general constraints by region

    for i in range(num_of_regions):    
        penalties[i][1] = 1-np.mean(evaluated_constraint_S21[i])#S41 general constraints by region

    for i in range(num_of_regions, num_of_regions*2):
        penalties[i-num_of_regions][2] = np.mean(evaluated_constraint_S31[i])#S31 overshoot constraints by region

    for i in range(num_of_regions, num_of_regions*2):
        penalties[i-num_of_regions][3] = np.mean(evaluated_constraint_S21[i])#S31 overshoot constraints by region
    
    for i in range(num_of_regions):
        penalties[i-num_of_regions][4] = np.mean(evaluated_constraint_ampImbalance[i])#S31 general constraints by region

    """row = every region
    column every signal evaluated.
    We have constraint evaluated in every region for every signal"""

    """Penalty matrix creates dynamics weigths adding a penalty to bad constraint performance
    [[S31_region1 S31_region2 S31_region3]
    [S41_region1 S41_region2 S41_region3]]
    """

    
    weights = fitnessObj.set_weights()
    weights_penalized = (100*weights + penalties)
    xmax, xmin = weights_penalized.max(), weights_penalized.min()   
    weights_penalized = (weights_penalized - xmin)/(xmax - xmin)
    """Evaluate products and sums"""
    prod =np.dot(weights_penalized.T,fi_matrix )

    log_prod = np.log(100*prod)
    #log_prod = prod

    #Just take diagonal as they are de FiWi product.
    products = np.diagonal(log_prod)  
    lambda_= 0.008 # 10 creates a strong relevance on oscillations

    #Cost counts for signals being close to truth value
    #and being inside constraint boundaries in every region
    #cost = np.sum(products[0:2])/len(funcs)

    #considers all functions witouth amp constraint
    """Usar en caso de guía plana"""
    #cost = np.sum([products[0],products[1]])


    #considers just all function. work well when testing wings
    """Usar en caso de guía con extrusiones"""
    cost = np.sum([products[0],products[1]])
    #cost = np.sum([products[4]])

    #Oscillation term counts for the integral to measure big resonances 
    #in every region and counts for the overshoot values in every region
    oscillation = lambda_*np.sum([products[2],products[3]])

    fitness =  cost + oscillation
    fitness = fitness.round(decimals=5, out=None)

    print("fitness="+str(iter))
    print("fitness="+str(fitness))
    fitnessObj.reset_constraints()

    del fitnessObj.regions
    del fitnessObj.normalized_bandwith #whole domain normalized
    del fitnessObj.regions_bandwidth #array of subdivided freq axis
    del fitnessObj.normalized_regions_bandwidth
    del fitnessObj.functions_array
    del fitnessObj
    del fi_matrix
    del funcs
 

    data_to_store = {
        "weights":{
            "note":"changing weights-focus on S31 and S41 parameters to test their part of the function by removing s11 s21 closeness eval.",
           "w_similarity_s11": 0,
            "w_similarity_s31":0,
            "w_closeness_s31_s21":0,
            "w_grad":0
        },
        "function":'testing new function',
    }
    #si cambio la formula, cambio el string para almacenarla

    #return indice,data_to_store,[dydx2_31, x_values_31, dydx2_41, x_values_41]
    return fitness, data_to_store,[[], [], [], []]


def calculate_subfunction(sub_functions,fitnessObj,num_of_constraints):
    
    #subfunctions_matrix = np.empty([len(fitnessObj.normalized_regions_bandwidth), (num_of_constraints)])
    subfunctions_matrix = np.ones((len(fitnessObj.normalized_regions_bandwidth), (num_of_constraints)))
    for idx , region in  enumerate(fitnessObj.normalized_regions_bandwidth):
        data = []
        if idx==0:#deviation_s31
            pass

        if idx==1:#deviation_s41
            pass

        if idx==2:#oscillation_s31
            pass


        if idx==3: #oscillation_s41 
            pass

        """Calculating for S31 MSE"""
        result = sub_functions[0](fitnessObj.Y_regions_s31[idx],-3)
        #print("S31 region " + str(idx)+", MSE="+str(result))
        print(result)

        subfunctions_matrix[idx][0] = result

        """Calculating for S41 MSE"""
        result = sub_functions[1](fitnessObj.Y_regions_s21[idx],-3)
        #print("S41 region " + str(idx)+", MSE="+str(result))

        subfunctions_matrix[idx][1] = result


        """Calculatign for S31"""
        data_31 = np.stack((region,fitnessObj.Y_regions_s31[idx]), axis=0)
        result = sub_functions[2](data_31)

        #print("S31 region " + str(idx)+", abs-integral of the 2nd derivative="+str(np.abs(result)))

        subfunctions_matrix[idx][2] = result

        """Calculatign for S41 integral of 2nd der."""

        data_21 = np.stack((region,fitnessObj.Y_regions_s21[idx]), axis=0)
        result = sub_functions[3](data_21)

        #print("S41 region " + str(idx)+", abs-integral of the 2nd derivative="+str(np.abs(result)))

        subfunctions_matrix[idx][3] = result

    return subfunctions_matrix



def derivate(data ):
    dydx1 = np.gradient(data[1],data[0])
    dydx2 = np.gradient(dydx1,data[0])
    return dydx2,data[0]

def integrate_data (x,y):
    y_int = np.abs(integrate.trapz(y, x=x))
    return y_int

def deviation_s31(data_Y,level):
    
    Y_true = np.full( shape=len(data_Y),fill_value=level, dtype=np.int)
    Y_pred = data_Y

    # Calculation of Mean Squared Error (MSE)
    MSE = mean_squared_error(Y_true,Y_pred)

    return MSE

def deviation_s21(data_Y,level):
    Y_true = np.full( shape=len(data_Y),fill_value=level, dtype=np.int)
    Y_pred = data_Y

    # Calculation of Mean Squared Error (MSE)
    MSE = mean_squared_error(Y_true,Y_pred)

    return MSE

def oscillation_s31(data):
    
    derivative = derivate(data)
    result = integrate_data(derivative[0],data[0])
    return result

def oscillation_s21(data):
    
    derivative = derivate(data)
    result = integrate_data(derivative[0],data[0])
    return result
    
    
    

    
