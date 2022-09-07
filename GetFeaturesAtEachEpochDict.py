#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import MatlabBinFileReader as binFileReader
import GetEpochsDict as getEpochsDict
import dataFile as getData
import GetFilterSignals as filterSignals

from GetAbsolutePowerFeatures import GetAbsolutePowerFeatures
from GetRelativePowerFeatures import GetRelativePowerFeatures

absolutePowerFeatures = GetAbsolutePowerFeatures()
relativePowerFeatures = GetRelativePowerFeatures()

ELECTRODES_LIST = binFileReader.getElectrodeNames()
SAMPLE_RATE = binFileReader.getSampleRate()

def _arrangeFeaturesDict(subjectList, signalsDict, featureList, epochList):
    featuresDict = {}
    idx = 0 
    for electrode in ELECTRODES_LIST:
        for power in featureList:
            for epoch in epochList:
                featuresDict[idx] = {}
                for subject in subjectList:
                    featuresDict[idx][subject] = signalsDict[subject][epoch][power][electrode]
                idx = idx + 1
    return featuresDict

def getFeaturesAtEachEpochDict(subjectList, signalsDict, featureName, epochList):
    featureList = getData.getFeatureList(featureName)
    featuresAtEachEpochDict = {}
    filterSignalsDict = {}
    epochsDict = getEpochsDict.getEpochsDict(signalsDict, epochList)
    

    if (featureName == 'AbsolutePowerFeature'):
        for subject in signalsDict:
            featuresAtEachEpochDict[subject] = {}
            filterSignalsDict = filterSignals.getFilterSignals(signalsDict[subject], SAMPLE_RATE)
            for epoch in epochsDict:
                featuresAtEachEpochDict[subject][epoch] = absolutePowerFeatures.getFeatures(filterSignalsDict, epochsDict[epoch])
    else:
        for subject in signalsDict:
            featuresAtEachEpochDict[subject] = {}
            filterSignalsDict = filterSignals.getFilterSignals(signalsDict[subject], SAMPLE_RATE)
            for epoch in epochsDict:
                featuresAtEachEpochDict[subject][epoch] = relativePowerFeatures.getFeatures(filterSignalsDict, epochsDict[epoch])
                
    featuresAtEachEpochDict = _arrangeFeaturesDict(subjectList, featuresAtEachEpochDict, featureList, epochList)

    return featuresAtEachEpochDict

