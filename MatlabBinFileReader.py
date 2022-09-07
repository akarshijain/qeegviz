import numpy as np

ELECTRODE_NAMES = ['Fp1','Fp2','F3','F4','C3','C4','P3','P4','O1',
                    'O2','F7','F8','T3','T4','T5','T6','Fz','Cz','Pz']

def _readMatlabBinFile(fileName):
    return np.fromfile(fileName, dtype='<f')  #little-endian single precisionfloat

def getElectrodeNames():
    return ELECTRODE_NAMES

def getNumElectrodes():
    numElectrodes = len(ELECTRODE_NAMES)
    return numElectrodes

def getSampleRate():
    sampleRate = 256
    return sampleRate

def loadSignals(fileName):
    numElectrodes = getNumElectrodes()

    arr = _readMatlabBinFile(fileName)
    signals = arr.reshape(19, -1)

    signalsDict = {}
    for idx in range(numElectrodes):
        electrode = ELECTRODE_NAMES[idx]
        signalsDict[electrode] = signals[idx]
    return signalsDict