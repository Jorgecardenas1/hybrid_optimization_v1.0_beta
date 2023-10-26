import numpy as np


class fitness_func():
    regions = [] #user provided information about segmentation regions inthe freq domain
    normalized_bandwith=[] #whole domain normalized
    regions_bandwidth=[] #array of subdivided freq axis
    normalized_regions_bandwidth=[]
    Y_regions_s21=[] #array of subdivided freq axis
    Y_regions_s31=[] #array of subdivided freq axis
    Y_regions_amp_imbalance=[]
    constraints_dic = {}
    functions_array=[]
    
    def set_constraints(self,constraint_name,true_value, min_val, max_val,type_constraint):
        #dictionary must pass constraints by
        self.constraints_dic[constraint_name]={'true_value':true_value,'min':min_val,'max':max_val,'type':type_constraint}
        return self.constraints_dic
    
    def reset_constraints(self):
        #dictionary must pass constraints by
        self.constraints_dic={}

        return True
    
    def evaluate_constraints(self,data_to_asses,constrain_name):

        constraint= self.constraints_dic[constrain_name]

        if constraint['type'] == 'in_limit':
                
            eval_= np.where((data_to_asses < constraint['max']) & (data_to_asses > constraint['min']), True, False)

            return eval_
            
        elif constraint['type'] == 'sum':
            pass
        elif constraint['type'] == 'out_limit':
            
            eval_= np.where((data_to_asses > constraint['max']) & (data_to_asses < constraint['min']), True, False)

            return eval_
        
        elif constraint['type'] == 'overshoot':
            
            eval_= np.where((data_to_asses > constraint['max']) | (data_to_asses < constraint['min']), True, False)
            
            return eval_


    def set_bandwidth(self,freq_values_array):
        self.normalized_bandwith=[]
        self.normalized_regions_bandwidth = []
        self.normalized_bandwith = (freq_values_array - freq_values_array.min()) / (freq_values_array.max() - freq_values_array.min()) 
        for region in self.regions_bandwidth:
            self.normalized_regions_bandwidth.append((region - freq_values_array.min()) / (freq_values_array.max() - freq_values_array.min()))
        
        

    def set_sub_functions(self,deviation_s31,deviation_s21,oscillation_s31,oscillation_s21):
        self.functions_array=[]
        self.functions_array=[
            deviation_s31,
            deviation_s21,
            oscillation_s31,
            oscillation_s21
        ]

        return self.functions_array

    def set_weights(self):
        
        weights_matrix = np.empty([len(self.normalized_regions_bandwidth), 5])
        #rows regions
        #cols functions to evaluate
        


        """Region 1"""
        weights_matrix[0][0]=0.05 #desviacion 31
        weights_matrix[0][1]=0.05 #desviacion 41
        weights_matrix[0][2]=0.01 #osc. 31 Estos corresopnden con lambda de la eq de tikhonov
        weights_matrix[0][3]=0.01 #osc. 41
        weights_matrix[0][4]=0.1 #Amp imbalance

        
        """Region 2"""
        weights_matrix[1][0]=0.47
        weights_matrix[1][1]=0.47
        weights_matrix[1][2]=0.005 #osc. 31 Estos corresopnden con lambda de la eq de tikhonov
        weights_matrix[1][3]=0.005
        weights_matrix[1][4]=0.62#Amp Imbalance

        """Region 3"""
        weights_matrix[2][0]=0.01
        weights_matrix[2][1]=0.01
        weights_matrix[2][2]=0.001 #osc. 31 Estos corresopnden con lambda de la eq de tikhonov
        weights_matrix[2][3]=0.001
        weights_matrix[2][4]=0.1 #Amp Imbalance

        
        
        
        return weights_matrix

    def set_targets():
        pass

    def set_priorization_regions(self,regions,freq_values_array,Y21_values_array,Y31_values_array,AmpImbalance_values_array):
        low_lim=0
        high_lim=0
        self.regions_bandwidth = []
        for index,freq in enumerate(regions):
            idx, value = min(enumerate(freq_values_array), key=lambda x: abs(x[1]-freq))
            
            if index==0:
                low_lim=0
                high_lim = idx
                
                self.regions_bandwidth.append(freq_values_array[low_lim:high_lim])
                self.Y_regions_s21.append(Y21_values_array[low_lim:high_lim])
                
                self.Y_regions_s31.append(Y31_values_array[low_lim:high_lim])
                
                self.Y_regions_amp_imbalance.append(AmpImbalance_values_array[low_lim:high_lim])

            elif index==len(self.regions)-1:
                low_lim = high_lim                
                self.regions_bandwidth.append(freq_values_array[low_lim:idx])
                self.regions_bandwidth.append(freq_values_array[idx:])
                
                self.Y_regions_s21.append(Y21_values_array[low_lim:idx])
                self.Y_regions_s31.append(Y31_values_array[low_lim:idx])
                self.Y_regions_amp_imbalance.append(AmpImbalance_values_array[low_lim:idx])

                self.Y_regions_s21.append(Y21_values_array[idx:])
                self.Y_regions_s31.append(Y31_values_array[idx:])
                self.Y_regions_amp_imbalance.append(AmpImbalance_values_array[idx:])

            else:
                low_lim = high_lim+1
                high_lim = idx
                self.regions_bandwidth.append(freq_values_array[low_lim:idx])
                self.Y_regions_s21.append(Y21_values_array[low_lim:idx])
                self.Y_regions_s31.append(Y31_values_array[low_lim:idx])
                self.Y_regions_amp_imbalance.append(AmpImbalance_values_array[low_lim:idx])

