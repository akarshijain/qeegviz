#!/usr/bin/env python
# coding: utf-8

import numpy as np

class CalculateICC:
    def __init__(self, featuresAtEachEpochDict):
        self.featuresAtEachEpochDict = featuresAtEachEpochDict
        self.subjectsList = []
        for subject in featuresAtEachEpochDict:
            self.subjectsList.append(subject)
        self.numSubjects = len(self.subjectsList)
        self.numSessions = len(featuresAtEachEpochDict[self.subjectsList[0]])
        
#msp - mean square error between the subjects
    def _calculateMSP(self):
        perSubjectMean = np.zeros(self.numSubjects)
        for i in range(self.numSubjects):
            subject = self.subjectsList[i]
            perSubjectMean[i] = np.mean(self.featuresAtEachEpochDict[subject])
        overallMean = np.mean(perSubjectMean)
        perSubjectErrorSquare = np.square(perSubjectMean - overallMean)
        msp = (self.numSessions / (self.numSubjects - 1))*np.sum(perSubjectErrorSquare)
        return msp
    
#mse - mean square error within the subjects
    def _calculateMSE(self):
        perSubjectMean = np.zeros(self.numSubjects)
        for i in range(self.numSubjects):
            subject = self.subjectsList[i]
            perSubjectMean[i] = np.mean(self.featuresAtEachEpochDict[subject])
        squareError = 0
        for i in range(self.numSubjects):
            subject = self.subjectsList[i]
            errorValue = self.featuresAtEachEpochDict[subject] - perSubjectMean[i]
            squareErrorForSubject = np.sum(np.square(errorValue))
            squareError += squareErrorForSubject
        mse = (1/((self.numSubjects-1)*(self.numSessions-1)))*squareError
        return mse
    
    def calculateICC(self):
        msp = self._calculateMSP()
        mse = self._calculateMSE()
        icc = (msp-mse)/(msp+((self.numSessions-1)*mse))
        return icc
