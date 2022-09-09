#!/usr/bin/env python
# coding: utf-8

# In[1]:
import os

import numpy as np

import MatlabBinFileReader as binReader
import EEGReReferencer as signalReReferencer
import dataFile as getData

def _getMinNumSamples(signalsDict):
    numSamples = np.empty(0)
    idx = 0
    for subject in signalsDict:
        for electrode in signalsDict[subject]:
            numSamples = np.append(numSamples, len(signalsDict[subject][electrode]))
            idx = idx+1
    return int(min(numSamples))

def _getResizeArr(signalsDict):
    numSamples = _getMinNumSamples(signalsDict)
    for subject in signalsDict:
        for electrode in signalsDict[subject]:
            signalsDict[subject][electrode] = np.resize(signalsDict[subject][electrode], numSamples)
    return signalsDict

def getDefaultSignalsDict(subjectList):
    defaultSignalsDict = {}
    for subject in subjectList:
        #defaultSignalsDict[subject] = binReader.loadSignals(f'./dataset/{subject}')
        defaultSignalsDict[subject] = binReader.loadSignals(subject)
    defaultSignalsDict = _getResizeArr(defaultSignalsDict)  
    return defaultSignalsDict

def getAvgSignalsDict(subjectList):
    avgSignalsDict = {}
    defaultSignalsDict = getDefaultSignalsDict(subjectList)
    for subject in subjectList:
        avgSignalsDict[subject] = signalReReferencer.convertToAvgReference(defaultSignalsDict[subject])
    return avgSignalsDict

def getCzSignalsDict(subjectList):
    czSignalsDict = {}
    defaultSignalsDict = getDefaultSignalsDict(subjectList)
    for subject in subjectList:
        czSignalsDict[subject] = signalReReferencer.convertToCzReference(defaultSignalsDict[subject])
    return czSignalsDict