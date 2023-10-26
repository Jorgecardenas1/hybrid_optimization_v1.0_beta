# *Quadrature Hybrid Optimization*
## **Geometry Optimization**

This package is intended to provide a tool that supports the optimization process of different components as cavities or antennas, which electromagnetic performance is highly dependant on geometry. 

We apply optimization algorithms supported on HDFS simulations which provides a reliable tool to evaluate how every alternative geometry bahaves and to collect data derived from every optimization batch.

---
## **What's included**
1. ### **Version: v0.1**
-   PSO optimization algorithm
-   Log file: Here you can find complete tracking of the optimizatio process
-   Data collection in CSV files
-   Passing configuration data through json files.
-   Simulation control by ID
-   
1. ### **Version: v0.9**

-   Hybrid selection by number of branches
-   Managing multiple hybrid phyton model files 
-   Fitness function
    --  You can configure the fitness function, weigths and constrains.
    -   PSO/fitness_func.py
    -   Fitness includes a lamda value, to be tunned as it defines the mix you want for the oscillatory behavior typical at the tails of the operation band, for the S parameters.


2. ### **To review**
-   How to make dynamic setting of arbitrary hybrids.

---

3. ### **Requirements** :
    _Things you need to set prior executing the script._

* [Requirements file]() - Make sure to install al requirements from requirements.txt

* [Hybrid_Design.py]() - Add to the root folder a file contains the geometric model for HFSS.

*   You have to make sure to add the following imports to your model's script.

```bash
import Simulation.funciones as fn
from Simulation.global_ import *
```

*   Also, make sure you add this line at the end of your script, including the ***.aedt** having you base model:

```bash
oProject.SaveAs("C:\Users\Astrolab\Documents\Ansoft\Band2+3_Hybrid_testV2.aedt", True)

```

*   Third, you have to properly set the HFSS file which you are going to use as the base model and the one the PSO algorithm is going to modify during every iteration.

Modify **global_.py** file with the simulation parameters:


```bash

global nombre_proyecto
nombre_proyecto = "Band2+3_Hybrid_testV2"

global nombre_diseno 
nombre_diseno = "Optimized Hybirid"

global nombre_variables
nombre_variables = "variables"

global nombre_particle 
nombre_particle = "particle"

global unidades
unidades = "mm"

global direccion_Ansoft
direccion_Ansoft=r"C:\\Users\\Astrolab\\Documents\\Ansoft\\" 
```


## **How to use**
1. Set the simulation parameters
In order to do that, you have to modify **simulate.py** script.

-   n_variables: lenght of each particle describing the geometric dimensions.

-   iteraciones: iterations to run during PSO.

-   n_particulas: number of particles you want to use during simulation

```
bash
def set_simulation_params(self):
        global_.n_variables = 8
        global_.iteraciones = 2
        global_.n_particulas = 2

        global_.nominales = [0.64,0.69,0.55,0.76,1.18,2.28,3.5,0.6]
        global_.var_min = [0.2,0.2,0.2,0.2,0.5,1.5,2.5,0.5]
        global_.var_max = [1.5,1.5,1.5,1.5,2.0,3.5,5.0,0.8]

        logging.info(msg.PARAMS_SET)
```



## **2. Run:**

* ### Full simulation
```bash
python3 optimize.py
```

* ### With bypass
You can access previous results from other simulations and not having to run again the full simulation.
This could be usefull to test different features that could use the data you already have in your output folder.

```bash
python3 optimize.py -bypass simulation id
```

```bash
python3 optimize.py -bypass 9fce9be1-f892-4531-9fc8-b852ba9b7ba4
```

## **Review your results after optimizing**
* [output files]() - you find an output folder where you find subfolders with identification numbers for every optimization run.


/

    output/
        output.csv
        optimization_id/
            files/
            figures/


There you can find raw data and graphs for every optimization run.

* [output.csv]() - This file is the place where the optimization results are saved to further use for statistical analysis purposes.

| sim_id | created_at | sim_setup | pbest | gbest | best_particle_id  | best_particle | iteration |
|--------|------------|-----------|-------|-------|------------------|-----------|-----------|
| simulation identifier| date |   json with setup parameters   |  fitness values    |best global fitness| best particle index number |best particle geometric values|iteration where results where found|



<br>
<br>


* [control.log]() - A datailed log file with every optimization run having the PSO results, run time, particles etc.


## **Credits**


## **License**
