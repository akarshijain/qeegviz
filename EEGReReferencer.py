#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np
   
def convertToCzReference(signals):
    if not "Cz" in signals:
        raise Exception("Cz Electrode not found.")
        
    reReferenceSignals = {}
    for electrode in signals.keys():
        reReferenceSignals[electrode] = signals[electrode] - signals["Cz"]
    return reReferenceSignals

def convertToAvgReference(subjectSignalsDict): 
    subjectSignalsArray = np.array(list(subjectSignalsDict.values()))
    avgSignals = np.average(subjectSignalsArray, axis = 0)

    reReferenceSignals = {}
    for electrode in subjectSignalsDict:
        reReferenceSignals[electrode] = np.subtract(subjectSignalsDict[electrode], avgSignals)
    return reReferenceSignals

