#!/usr/bin/env python
# coding: utf-8

from abc import ABC, abstractmethod

#base interface
class FeatureSet(ABC):
    
    # return list of feature names
    @abstractmethod
    def getFeatureNames(self):
        pass

    # return key-value pairs of (FeatureName, FeatureValue)
    @abstractmethod
    def getFeatures(self, eegEpoch):
        pass