#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np
import dataFile as getData
import MatlabBinFileReader as binFileReader

SAMPLE_RATE = binFileReader.getSampleRate()

def _getMinNumSamples(signalsDict):
    numSamples = np.empty(0)
    idx = 0
    for subject in signalsDict:
        for electrode in signalsDict[subject]:
            numSamples = np.append(numSamples, len(signalsDict[subject][electrode]))
            idx = idx+1
    return int(min(numSamples))

def getEpochsArr(epochs, numSamples, sampleRate, stepSize):
    epochSize = epochs*sampleRate
    beginTime = np.arange(0, numSamples, stepSize)
    numEpochs = beginTime.shape[0] 
    epochsArr = np.zeros(shape = (numEpochs, 2), dtype = np.int32)
    epochsArr[:,0] = beginTime
    epochsArr[:,1] = beginTime + epochSize
    return epochsArr

def getEpochsDict(signalsDict, epochList):
    epochsDict = {}
    numSamples = _getMinNumSamples(signalsDict)
    for epoch in epochList:
        stepSize = epoch * SAMPLE_RATE
        epochsDict[epoch] = getEpochsArr(epoch, numSamples, SAMPLE_RATE, stepSize)
    return epochsDict
        