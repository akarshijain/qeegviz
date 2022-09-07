#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import GetAllSubjectsSignalsDict as allSubjectsSignalsDict
import GetFeaturesAtEachEpochDict as featuresAtEachEpochDict
import dataFile as getData

from CalculateICC import CalculateICC

ELECTRODES_LIST = getData.getElectrodeList()
numElectrodes = len(ELECTRODES_LIST)

def getICCValues(subjectList, featureName, referenceName, epochList):

    numEpochs = len(epochList)

    featureList = getData.getFeatureList(featureName)
    numFeatures = len(featureList)

    numFeatureValues = numEpochs*numFeatures*numElectrodes
    iccValuesArr = np.zeros(numFeatureValues)

    if (referenceName == 'averageReference'):
        signalsDict = allSubjectsSignalsDict.getAvgSignalsDict(subjectList)
    elif(referenceName == 'czReference'):
        signalsDict = allSubjectsSignalsDict.getCzSignalsDict(subjectList)
    else: 
        signalsDict = allSubjectsSignalsDict.getDefaultSignalsDict(subjectList) 

    featuresDict = featuresAtEachEpochDict.getFeaturesAtEachEpochDict(subjectList, signalsDict, featureName, epochList)
    
    for idx in range(0, numFeatureValues-1):
        icc = CalculateICC(featuresDict[idx])
        iccValuesArr[idx] = icc.calculateICC() 
    iccValuesArr = iccValuesArr.reshape(numEpochs, numFeatures, numElectrodes)
    
    return iccValuesArr  #epoch[featureList[electrodes]]]

