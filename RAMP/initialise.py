# -*- coding: utf-8 -*-

#%% Initialisation of a model instance again testing git

from core import np
import importlib

#Primo_test_Prova a pullare in una specifica branch dal main
def yearly_pattern():
    '''
    Definition of a yearly pattern of weekends and weekdays, in case some appliances have specific wd/we behaviour
    '''
    #Yearly behaviour pattern
    Year_behaviour = np.zeros(365)
    Year_behaviour[5:365:7] = 1
    Year_behaviour[6:365:7] = 1
    
    return(Year_behaviour)


def user_defined_inputs(j):
    '''
    Imports an input file and returns a processed User_list
    '''
    User_list = getattr((importlib.import_module('input_file_%d' %j)), 'User_list') #todo It is important to look at the scenario you are using as an input, I could give as an imput another file with for example the community services and another one with the IGA in this way I would be able to compute the proportion in comparison with the total
    return(User_list)


def Initialise_model():
    '''
    The model is ready to be initialised
    '''
    num_profiles = int(input("please indicate the number of profiles to be generated: ")) #asks the user how many profiles (i.e. code runs) he wants
    print('Please wait...') 
    Profile = [] #creates an empty list to store the results of each code run, i.e. each stochastically generated profile
    
    return (Profile, num_profiles)
    
def Initialise_inputs(j):
    Year_behaviour = yearly_pattern()
    user_defined_inputs(j)
    user_list = user_defined_inputs(j)
    
    # Calibration parameters
    '''
    Calibration parameters. These can be changed in case the user has some real data against which the model can be calibrated
    They regulate the probabilities defining the largeness of the peak window and the probability of coincident switch-on within the peak window
    '''
    peak_enlarg = 0 #percentage random enlargement or reduction of peak time range length
    mu_peak = 0.5 #median value of gaussian distribution [0,1] by which the number of coincident switch_ons is randomly selected
    s_peak = 1 #standard deviation (as percentage of the median value) of the gaussian distribution [0,1] above mentioned

    return (peak_enlarg, mu_peak, s_peak, Year_behaviour, user_list)

'''Aggreagate demand , assumptions for the scenarios, '''
