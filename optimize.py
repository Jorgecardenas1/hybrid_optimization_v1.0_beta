# -*- coding: utf-8 -*-

from glob import glob
import logging
import os
import datetime
import numpy as np
import json
import sys

from scipy.sparse import data
import inquirer


import Settings.setting as setting
import PSO.pso as pso
 
import Simulation.simulate as simulate
import test 
import Simulation.global_ as global_
import Settings.messages as msg
import Simulation.dataManagement as db

def main(bypass):
   
    logging.info(msg.STARTED)
    ### Process
    global swarm 
    swarm = set_Swarm() #initialize swarm



    for index in range(len(swarm.particles)):
        particle = swarm.particles[index]
        
        print(msg.SIM_ID+global_.simulationID)
        #Prepare simulation intermediate file
        logging.info(msg.INITIAL_PARTICLE + str(particle.id_) + str(particle.values_array))
       
        simulate.create_sim_file(particle.values_array,0,particle.id_)

        logging.info(msg.SIM_FILE_OK)

        #start simulation
        logging.info(msg.SIM_PARTICLE_START + str(particle.id_))

        if bypass!="-bypass":
            simulate.run_simulation_hfss(global_.HFSS_RUN_STRINGS)


        #get simulation results
        s11,s21,s31,s41, amp_imbalance = simulate.read_simulation_results(0,particle.id_)
        #evaluate fitness for each particle
        #fit
        fit, data_to_store, derivative_array = pso.fitness([s11,s21,s31,s41, amp_imbalance],[0,particle.id_]) #get the index of the particle (geometry)
        
        data_to_plot={
            "dy2_31":derivative_array[0],
            "x_31":derivative_array[1],
            "y2_21":derivative_array[2],
            "x_21":derivative_array[3]
        }
    
        db_manager.save_data_to_plot(data_to_plot,0,particle.id_)
        #p best is keeping fit values
        swarm.pbest[particle.id_] = fit

        logging.info(msg.FITNESS_VALS+str(fit))

    elapsed=setting.get_elapsed_time()
    
    logging.info(msg.TIME_ELAPSED+str(elapsed))

    best_index=swarm.get_particle_best_fit(swarm.particles)

    logging.info(msg.PBEST + str(swarm.pbest))
    logging.info(msg.GBEST + str(swarm.gbest)) #swarm.gbest comes from get_particle_best_fit
    logging.info(msg.PGVALUE + str(swarm.pg))
    logging.info(msg.BEST_PARTICLE_INDEX + str(best_index)+'\n')

    sim_results = {
        "elapsed_time": str(elapsed),
        "data_to_store": json.dumps(data_to_store)

    }

    data_to_store={
        "sim_id":global_.simulationID,
        "created_at":Simulation.date,
        "sim_setup":json.dumps(Simulation.get_simulation_params()),
        "sim_results":json.dumps(sim_results),
        "pbest":json.dumps(swarm.pbest.tolist()),
        "gbest":swarm.gbest,
        "best_particle_id":best_index,
        "best_particle": json.dumps(swarm.particles[best_index].values_array.tolist()),
        "iteration":0
    }
    
    db_manager.load_df()
    db_manager.fill_df(data_to_store)

    ### Iterations
    logging.info(msg.START_ITERATIONS)
    run_iterations(global_.iteraciones,bypass=bypass )
    ### Finished process
    logging.info(msg.FINISHED)


def set_Swarm():
    swarm = pso.Swarm(global_.n_particulas,global_.n_variables,global_.var_max,global_.var_min)
    swarm.create()
    logging.info(msg.PARTICLES_CREATED)
    return swarm

def run_iterations(iteraciones,bypass ):
  
    pi_best = swarm.particles.copy()#array initial particles

    for i in range(iteraciones):
        print(msg.NUM_ITERATIONS+str(iteraciones))
        print("current it.:"+str(i))

        logging.info(msg.ITERATION + str(i))
        logging.info("Calculando nuevas particulas...")
       
       ### particulas anterior es una copia del objeto arreglo de Particulas
       ### que es propiedad del objeto Swarm
        particulas_anterior = []
        particulas_anterior  = swarm.particles.copy() #Array de particulas
        logging.info("Calculando las velocidades y posiciones siguientes..")

        ### el objeto swarm se ocupa de crear las particulas nuevas
        ### que realmente son actualizaciones de las particulas anteriores
        #array Particulas que se van actualizando
        #array Particulas iniciales
        #pg -> mejor posocion encontrada para cualquier particula
        #arreglo de velocidades
        x , v = swarm.nuevas_particulas(particulas_anterior, pi_best, swarm.pg, swarm.velocidades,i)
        ### se actualizan las particulas originales con las nuevas particulas actualizadas

        for index_, particle in enumerate(x):

            swarm.particles[index_].values_array = particle.values_array
            #swarm.particles  = x.copy() #aqui se está copiando un objeto

        swarm.velocidades = np.copy(v) #aquí un arreglo de vectores
        logging.info(msg.SIM_NEW_PARTICLE+"\n")

        #Array valores se ocupa de recibir los valores de fitness de cada particula en la 
        #actual iteraciòn
        valores = np.zeros(global_.n_particulas)
        
        ### se itera sobre cada particula y se simula
        # [print(i.id_) for i in swarm.particles]

        for index in range(len(swarm.particles)):
            particle = swarm.particles[index]
            setting.start_timing()

                 
            logging.info(msg.PARTICLE+ str(particle.id_)+':' + str(particle.values_array))

            #Prepare simulation intermediate file

            simulate.create_sim_file(particle.values_array,i+1,particle.id_)

            logging.info(msg.SIM_FILE_OK)

            #start simulation
            logging.info(msg.SIM_PARTICLE_START + str(particle.id_))

            if bypass!="-bypass":
                simulate.run_simulation_hfss(global_.HFSS_RUN_STRINGS)

            #get simulation results
            s11,s21,s31,s41, amp_imbalance = simulate.read_simulation_results(i+1,particle.id_)
            
            #fit
            valores[index], data_to_store,derivative_array = pso.fitness([s11,s21,s31,s41,amp_imbalance],[i+1,particle.id_]) #get the index of the particle (geometry)
            data_to_plot={
                "dy2_31":derivative_array[0],
                "x_31":derivative_array[1],
                "y2_21":derivative_array[2],
                "x_21":derivative_array[3]
            }
    
            db_manager.save_data_to_plot(data_to_plot,i+1,particle.id_)
            
            logging.info(msg.FITNESS_VALS+str(valores))
            logging.info(msg.ITERATION+str(i+1)+'\n')

            #Calculate fitness values for every particle in current iteration
            #if current particle is the best in current iteration
            #sort pbest
            if valores[index] < swarm.pbest[index]:
                swarm.pbest[index] = valores[index]
                pi_best[index] = swarm.particles[index] #swarm particles is updated before with new particle

        ## After each iteration we end up with pbest, pi
        #these values come from the iteration 0
        if np.min(swarm.pbest) < swarm.gbest:

            swarm.gbest = np.min(swarm.pbest) #swarm.gbest comes from get_particle_best_fit
            swarm.pg = pi_best[np.argmin(swarm.pbest)].values_array
        
        best_index=np.argmin(swarm.pbest)


        logging.info(msg.PBEST+ str(swarm.pbest))
        logging.info(msg.GBEST+ str(swarm.gbest))
        logging.info("pi_best  = "+ str(particle.values_array))
            
        elapsed=setting.get_elapsed_time()

        logging.info(msg.TIME_ELAPSED+elapsed)

        sim_results = {
            "elapsed_time": str(elapsed),
            "data_to_store": json.dumps(data_to_store)
        }

        data_to_store={
            "sim_id":global_.simulationID,
            "created_at":Simulation.date,
            "sim_setup":json.dumps(Simulation.get_simulation_params()),
            "sim_results":json.dumps(sim_results),
            "pbest":json.dumps(swarm.pbest.tolist()),
            "gbest":swarm.gbest,
            "best_particle_id":best_index,
            "best_particle": json.dumps(swarm.particles[best_index].values_array.tolist()),
            "iteration":i+1
        }
        
        db_manager.load_df()
        db_manager.fill_df(data_to_store)

    ###Cierre del ciclo
    print("Minimo global encontrado: "+str(swarm.gbest))
    logging.info(msg.GLOBAL_MIN_VAL+str(swarm.gbest))
     

    
 
def prepare_simulation_file(particle, id):
    simulate.create_sim_file(particle,0,id +1)

if __name__ == "__main__":
   
    args = sys.argv[1:]
    
    questions = [
    inquirer.List('size',
                message="Number of branches?",
                choices=['5', '7','8', '9','80','Band 2+3 8 br - flex',"Band 3 - 8Br","Band 3 - flat 8Br Flex","Band 3 - 8Br Flex","Band 3 - 12Br Flex",'100','rashid band 5','rashid band 5 benchmark H1H2','rashid band 5 - extrusion','rashid band 5 - extrusion_free'\
                    ,'winged band 2+3','winged band 2+3 free param','3-winged band 2+3 free param','3-winged band 2+3 fixed param','3-winged band 2+3 flex distribution','10-br 3-winged band 2+3 flex distribution','12-br 3-winged band 2+3 flex distribution','12-br 3-winged band 2+3 fixed param reduced vector'\
                        ,'3-winged band 2+3 Rashid Parameters Vector','3-winged 10 br band 2+3 Rashid Parameters Vector','3-winged 12 br band 2+3 Rashid Parameters Vector','3-winged 14 br band 2+3 Rashid Parameters Vector'],
            ),
    ]
    answers = inquirer.prompt(questions)


    
    if answers["size"]!='Band 2+3 8 br - flex' and answers["size"]!= "Band 3 - 8Br" and answers["size"]!="Band 3 - flat 8Br Flex" and answers["size"]!="Band 3 - 8Br Flex" and answers["size"]!="Band 3 - 12Br Flex" and answers["size"]!= 'rashid band 5' and answers["size"]!= 'winged band 2+3' \
        and answers["size"]!='rashid band 5 - extrusion' and answers["size"]!='rashid band 5 - extrusion_free' \
            and answers["size"]!='rashid band 5 benchmark H1H2' \
                and answers["size"]!='3-winged band 2+3 flex distribution'\
            and answers["size"]!='winged band 2+3 free param' and answers["size"]!='3-winged band 2+3 free param'\
                and answers["size"]!='10-br 3-winged band 2+3 flex distribution' and answers["size"]!='12-br 3-winged band 2+3 flex distribution' and answers["size"]!='12-br 3-winged band 2+3 fixed param reduced vector' and answers["size"]!='3-winged band 2+3 fixed param' and answers["size"]!='3-winged band 2+3 Rashid Parameters Vector' \
                    and answers["size"]!='3-winged 10 br band 2+3 Rashid Parameters Vector' and answers["size"]!='3-winged 14 br band 2+3 Rashid Parameters Vector'\
                        and answers["size"]!='3-winged 12 br band 2+3 Rashid Parameters Vector':


        global_.branches =int(answers["size"])

    elif answers["size"]=='Band 2+3 8 br - flex':
        global_.branches='Band 2+3 8 br - flex'
    elif answers["size"]=="Band 3 - 8Br":
        global_.branches = "Band 3 - 8Br"
    
    elif answers["size"]=="Band 3 - flat 8Br Flex":
        global_.branches="Band 3 - flat 8Br Flex"
    elif answers["size"]=="Band 3 - 8Br Flex":
        global_.branches= "Band 3 - 8Br Flex"

    elif answers["size"]=="Band 3 - 12Br Flex":
        global_.branches="Band 3 - 12Br Flex"

    elif answers["size"]=='rashid band 5':
        global_.branches = 'rashid band 5'
    
    elif answers["size"]=='rashid band 5 - extrusion':
        global_.branches = 'rashid band 5 - extrusion'

    elif answers["size"]=='rashid band 5 - extrusion_free':
        global_.branches = 'rashid band 5 - extrusion_free'
    elif answers["size"]=='rashid band 5 benchmark H1H2':
        global_.branches='rashid band 5 benchmark H1H2'

    elif answers["size"]== 'winged band 2+3':
        global_.branches = 'winged band 2+3'

    elif answers["size"]=='winged band 2+3 free param':
        global_.branches = 'winged band 2+3 free param'

    elif answers["size"]=='3-winged band 2+3 free param':
        global_.branches = '3-winged band 2+3 free param'

    elif answers["size"]=='3-winged band 2+3 fixed param':
        global_.branches = '3-winged band 2+3 fixed param'

    elif answers["size"]=='3-winged band 2+3 flex distribution':
        global_.branches='3-winged band 2+3 flex distribution'
    elif answers["size"]=='12-br 3-winged band 2+3 fixed param reduced vector':
        global_.branches='12-br 3-winged band 2+3 fixed param reduced vector'
    elif answers["size"]=='10-br 3-winged band 2+3 flex distribution':
        global_.branches='10-br 3-winged band 2+3 flex distribution'
    elif answers["size"]=='12-br 3-winged band 2+3 flex distribution':
        global_.branches='12-br 3-winged band 2+3 flex distribution'
    elif answers["size"]=='3-winged band 2+3 Rashid Parameters Vector':
        global_.branches = '3-winged band 2+3 Rashid Parameters Vector'
    elif  answers["size"]=='3-winged 10 br band 2+3 Rashid Parameters Vector':
        global_.branches = '3-winged 10 br band 2+3 Rashid Parameters Vector'
    elif  answers["size"]=='3-winged 12 br band 2+3 Rashid Parameters Vector':
        global_.branches = '3-winged 12 br band 2+3 Rashid Parameters Vector'
   
    elif  answers["size"]=='3-winged 14 br band 2+3 Rashid Parameters Vector':
        global_.branches = '3-winged 14 br band 2+3 Rashid Parameters Vector'
    else:
        pass
    # 1. Check for the arg pattern:
    #   python3 affirm.py -affirm Bart
    #   e.g. args[0] is '-affirm' and args[1] is 'Bart'
    if len(args) == 2 and args[0] == '-bypass':

        sim_ID = args[1]
        ### Setting global variables and folders
        global_.current_path = setting.check_current_path()
        global_.local_system = setting.check_os()
        #global_.direccion_archivos = setting.check_current_path()


        ## setting logging file
        logging.basicConfig(filename= os.path.join( os.path.normpath(global_.direccion_archivos),r"control.log"),\
            force=True, encoding='utf-8', level=logging.INFO)
        logging.basicConfig(format='%(asctime)s %(message)s')
        logging.info(datetime.datetime.today())

        ### Setting simulation
        ## this object has simulation results for the current run
        # pbest array

        Simulation = simulate.Simulation(datetime.datetime.today())
        Simulation.set_simulation_params()

        global_.setSimID()
        Simulation.id_ = sim_ID
        global_.simulationID = sim_ID

        logging.info(msg.SIM_ID+ str(Simulation.id_)+" bypass")


        db_manager = db.DBManager(global_.simulationID)
        db_manager.load_df()

        ### Setting environment
        #setting.set_direccion_ansoft()
        setting.set_folders()

        main(args[0])

    else:
        ### Setting global variables and folders
        global_.current_path = setting.check_current_path()
        global_.local_system = setting.check_os()

        if global_.branches == 7:
            global_.nombre_proyecto = "Band2+3_Hybrid_testV2"
            global_.nombre_diseno = "Optimized Hybrid"

        if global_.branches == 8:
            global_.nombre_proyecto = "Band2+3_Hybrid_testV4"
            global_.nombre_diseno = "Optimized Hybrid"

        #8 branches with a and b variable
        if global_.branches == 80:
            global_.nombre_proyecto = "Band2+3_Hybrid_testV4_avar"
            global_.nombre_diseno = "Optimized Hybrid"

        if global_.branches  == 'Band 2+3 8 br - flex':
            global_.nombre_proyecto = "Band2+3_Hybrid_8br_fixedparam_flex"
            global_.nombre_diseno = "Optimized Hybrid"

        if global_.branches == "Band 3 - 8Br":
            global_.nombre_proyecto = "Band3_Hybrid_testV4_avar"
            global_.nombre_diseno = "Optimized Hybrid"

        if global_.branches=="Band 3 - flat 8Br Flex":
            global_.nombre_diseno="Optimized Hybrid"
            global_.nombre_proyecto="Band3_Hybrid_8br_flex"

        if global_.branches=="Band 3 - 8Br Flex":
            global_. nombre_proyecto = "Band3_Hybrid_8br_fixedparam_flex"
            global_.nombre_diseno = "Optimized Hybrid"
        
        if global_.branches=="Band 3 - 12Br Flex":
            global_. nombre_proyecto = "Band3_Hybrid_12br_3_extruded_fixedparam_flex"
            global_.nombre_diseno = "Optimized Hybrid"

        if global_.branches == 9:
            global_.nombre_proyecto = "Band2+3_Hybrid_testV3"
            global_.nombre_diseno = "Optimized Hybrid"
        
        if global_.branches == 100: #10 branches
            global_.nombre_proyecto = "Band2+3_Hybrid_testV4_10Br"
            global_.nombre_diseno = "Optimized Hybrid"

        if global_.branches == 'rashid band 5': #10 branches
            global_.nombre_proyecto = "Band2+3_Hybrid_Rashid_Benchmark"
            global_.nombre_diseno = "Optimized Hybrid"

        """This is considering the sizes and proportions rahid did H1 H2 L , a and b
        to simulate fewer free parameters. The vector get just 8 entries in size"""
        if global_.branches == 'rashid band 5 benchmark H1H2':
            global_.nombre_proyecto = "Band5_Hybrid_8br_3_extruded_BenchmarkRashid"
            global_.nombre_diseno = "Optimized Hybrid"



        if global_.branches == 'rashid band 5 - extrusion': #10 branches
            global_.nombre_proyecto = "Band2+3_Hybrid_Rashid_extruded"
            global_.nombre_diseno = "Optimized Hybrid"

        if global_.branches == 'rashid band 5 - extrusion_free': #10 branches
            global_.nombre_proyecto = "Band2+3_Hybrid_Rashid_freeparam_extruded"
            global_.nombre_diseno = "Optimized Hybrid"
        
        if global_.branches == 'winged band 2+3': #10 branches
            global_.nombre_proyecto = "Band2+3_Hybrid_8br_extruded"
            global_.nombre_diseno = "Optimized Hybrid"

        if global_.branches =='winged band 2+3 free param':
            global_.nombre_proyecto = "Band2+3_Hybrid_8br_extruded_freeparam"
            global_.nombre_diseno = "Optimized Hybrid"

        if global_.branches=='3-winged band 2+3 free param':
            global_.nombre_diseno="Optimized Hybrid"
            global_.nombre_proyecto = "Band2+3_Hybrid_8br_3_extruded_freeparam"

        if global_.branches=='3-winged band 2+3 fixed param':
            global_.nombre_diseno="Optimized Hybrid"
            global_.nombre_proyecto = "Band2+3_Hybrid_8br_3_extruded_fixedparam"
        
        if global_.branches=='3-winged band 2+3 flex distribution':
            global_.nombre_proyecto="Band2+3_Hybrid_8br_3_extruded_fixedparam_flex"
            global_.nombre_diseno="Optimized Hybrid"
            
        if global_.branches=='12-br 3-winged band 2+3 fixed param reduced vector':
            global_.nombre_diseno="Optimized Hybrid"
         
            global_.nombre_proyecto = "Band2+3_Hybrid_12br_3_extruded_fixedparam"
        
        if global_.branches == '10-br 3-winged band 2+3 flex distribution':
            global_.nombre_proyecto='Band2+3_Hybrid_10br_3_extruded_fixedparam_flex'
            global_.nombre_diseno="Optimized Hybrid"

        if global_.branches == '12-br 3-winged band 2+3 flex distribution':
            global_.nombre_proyecto='Band2+3_Hybrid_12br_3_extruded_fixedparam_flex'
            global_.nombre_diseno="Optimized Hybrid"
        if global_.branches=='3-winged band 2+3 Rashid Parameters Vector':
            global_.nombre_diseno = "Optimized Hybrid"
            global_.nombre_proyecto = 'Band2+3_Hybrid_8br_3_extruded_BenchmarkRashid'
        
        if global_.branches =='3-winged 10 br band 2+3 Rashid Parameters Vector':
            global_.nombre_diseno="Optimized Hybrid"
            global_.nombre_proyecto = 'Band2+3_Hybrid_10br_3_extruded_BenchmarkRashid'
        if global_.branches =='3-winged 12 br band 2+3 Rashid Parameters Vector':
            global_.nombre_diseno="Optimized Hybrid"
            global_.nombre_proyecto = 'Band2+3_Hybrid_12br_3_extruded_BenchmarkRashid'
        
        if global_.branches =='3-winged 14 br band 2+3 Rashid Parameters Vector':
            global_.nombre_diseno="Optimized Hybrid"
            global_.nombre_proyecto = 'Band2+3_Hybrid_14br_3_extruded_BenchmarkRashid'
        
        #global_.direccion_archivos = setting.check_current_path()


        ## setting logging file
        logging.basicConfig(filename= os.path.join( os.path.normpath(global_.direccion_archivos),r"control.log"),\
            force=True, encoding='utf-8', level=logging.INFO)
        logging.basicConfig(format='%(asctime)s %(message)s')
        logging.info(datetime.datetime.today())

        ### Setting simulation
        ## this object has simulation results for the current run
        # pbest array

        Simulation = simulate.Simulation(datetime.datetime.today())
        Simulation.set_simulation_params()


        global_.setSimID()
        Simulation.id_ = global_.simulationID

        logging.info(msg.SIM_ID+ str(Simulation.id_))


        db_manager = db.DBManager(global_.simulationID)
        db_manager.load_df()

        ### Setting environment
        #setting.set_direccion_ansoft()

        setting.set_folders()
        main('')
        
    ## Main Process
   