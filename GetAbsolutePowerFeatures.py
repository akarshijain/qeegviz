#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import scipy.fft
import numpy as np

from FeatureSet import FeatureSet
from abc import ABC, abstractmethod


class GetAbsolutePowerFeatures(FeatureSet):
    
    FULL_POWER = 'fullPower'
    DELTA_POWER = 'deltaPower'
    THETA_POWER = 'thetaPower'
    ALPHA_POWER = 'alphaPower'
    BETA_POWER = 'betaPower'
    GAMMA_POWER = 'gammaPower'
    
    #helper functions
    def _getPower(self, signalsDict):
        fftCoeffs = scipy.fft.fft(signalsDict)
        return np.sum(np.square(np.abs(fftCoeffs)))
    
    def _getAbsolutePower(self, filterSignalsDict, epochs):
        absolutePower = {}
        numEpochs = epochs.shape[0]
        for (electrode, signals) in filterSignalsDict.items():
            absolutePower[electrode] = np.zeros(numEpochs)
            for epochIdx in range (numEpochs):
                startIdx = epochs[epochIdx][0]
                endIdx = epochs[epochIdx][1]
                absolutePower[electrode][epochIdx] = self._getPower(signals[startIdx:endIdx])
        return absolutePower

    def getFeatureNames(self):
        return [self.DELTA_POWER, self.THETA_POWER, self.ALPHA_POWER, self.BETA_POWER, self.GAMMA_POWER]

    def getFeatures(self, filterSignalsDict, epochs):  
        
        absolutePowerFeature = {}
        absolutePowerFeature[self.FULL_POWER] = self._getAbsolutePower(filterSignalsDict[self.FULL_POWER], epochs)
        absolutePowerFeature[self.DELTA_POWER] = self._getAbsolutePower(filterSignalsDict[self.DELTA_POWER], epochs)
        absolutePowerFeature[self.THETA_POWER] = self._getAbsolutePower(filterSignalsDict[self.THETA_POWER], epochs)
        absolutePowerFeature[self.ALPHA_POWER] = self._getAbsolutePower(filterSignalsDict[self.ALPHA_POWER], epochs)
        absolutePowerFeature[self.BETA_POWER] = self._getAbsolutePower(filterSignalsDict[self.BETA_POWER], epochs)
        absolutePowerFeature[self.GAMMA_POWER] = self._getAbsolutePower(filterSignalsDict[self.GAMMA_POWER], epochs)

        return absolutePowerFeature

