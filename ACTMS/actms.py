# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 08:24:27 2019

@author: Sebastian Blum
"""

import actr
import numpy as np
import pandas as pd



'''
Create a dictionary to save all the simulation parameters
''' 
dict = {}

def writeToProtocol(name, variable):
    dict.update( { name : variable } )

def getProtocol():
    return pd.DataFrame([dict])

def deleteProtocol():
    dict.clear()




'''
Forward parameters from one model to another
''' 
main_name = "main-model" # default is main model, normative has to be specified

def set_main_model(name):
    global main_name
    main_name = name

def simulate_submodel(model, action):
    actr.set_current_model(model)
    actr.schedule_mod_buffer_chunk("goal",["state", "simulate", "action", action],0) # simulate dynamic
    writeToProtocol( "action-" + str(action), "simulate-" + str(model))

def return_from_submodel(input, action, goalstatevar, imaginalslot):
    actr.set_current_model(main_name)
    actr.schedule_mod_buffer_chunk("goal", ["state", goalstatevar], 0)
    actr.schedule_mod_buffer_chunk("imaginal", [imaginalslot, "\'" + input + "\'"], 0)
    writeToProtocol("forwardto-" + str(main_name) + "-" + str(action), input)




'''
UTILITY LEARNING OVER MODELS
''' 
utilitylist = list
savelist = list

def resetutility():
    global utilitylist
    utilitylist = list

def saveutility():
    global savelist
    savelist = utilitylist

def getutility():
    global utilitylist
    utilitylist = actr.spp([':name', ':u'])

def setutility():
    global utilitylist

    for idx,val in enumerate(utilitylist[0:14]):
            utilitylist[idx][1] = 0

    for idx,val in enumerate(utilitylist):
        actr.spp(val[0],':u',val[1])
    print("-"*30 + " Utility Reset ")         

def setsaveutility():
    global savelist
    for idx,val in enumerate(savelist[0:14]):
            savelist[idx][1] = 0

    for idx,val in enumerate(savelist):
        actr.spp(val[0],':u',val[1])
    print("-"*30 + " Utility Reset ")       




'''
STATE THAT PROGRAM HAS ENDED
''' 
def end_program(input):
    if input == 1:
        return True
        
# FINISHED COMMAND TO RUN THE MODEL
def init_actms():
    actr.add_command("simulate-submodel", simulate_submodel, "back to main function")
    actr.add_command("return-from-submodel", return_from_submodel, "back to main function")
    actr.add_command("end-program", end_program,"returns that model is finished")
   
