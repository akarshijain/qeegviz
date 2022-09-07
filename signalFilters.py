# signalFilters.py
#
# Code for filtering signals into various bands
# High level public functions: filterSignalArray, filterSignalDict
import numpy as np
from scipy import signal

def designFilter_70Hz_noNotch(sampleRate):
    #Design Bandpass filter
    lp_wp = (2.0 * 70) / sampleRate
    lp_ws = (2.0 * 90) / sampleRate
    hp_wp = (2.0 * 0.5) / sampleRate
    hp_ws = (2.0 * 0.01) / sampleRate
    wp = [hp_wp, lp_wp]
    ws = [hp_ws, lp_ws]
    gpass = 0.1
    gstop = 20
    b,a = signal.iirdesign(wp, ws, gpass, gstop, analog=False, ftype='ellip', output='ba')
    
    return b,a


def designNotchFilter(sampleRate):
    #Design notch filter
    #f0 = 60.0 #For utemple and physionet data only
    f0 = 50.0
    Q = 30.0  # Quality factor
    b_n, a_n = signal.iirnotch((2 * f0)/sampleRate, Q)
    
    return b_n, a_n


def designFilter_4Hz(sampleRate):
    #Design Bandpass filter
    lp_wp = (2.0 * 4) / sampleRate
    lp_ws = (2.0 * 5) / sampleRate
    hp_wp = (2.0 * 0.5) / sampleRate
    hp_ws = (2.0 * 0.01) / sampleRate
    wp = [hp_wp, lp_wp]
    ws = [hp_ws, lp_ws]
    gpass = 0.1
    gstop = 20
    b,a = signal.iirdesign(wp, ws, gpass, gstop, analog=False, ftype='ellip', output='ba')
    
    return b,a


def designFilter_4Hz_8Hz(sampleRate):
    #Design Bandpass filter
    lp_wp = (2.0 * 8) / sampleRate
    lp_ws = (2.0 * 8.5) / sampleRate
    hp_wp = (2.0 * 4) / sampleRate
    hp_ws = (2.0 * 3.5) / sampleRate
    wp = [hp_wp, lp_wp]
    ws = [hp_ws, lp_ws]
    gpass = 0.1
    gstop = 20
    b,a = signal.iirdesign(wp, ws, gpass, gstop, analog=False, ftype='ellip', output='ba')
    
    return b,a


def designFilter_8Hz_13Hz(sampleRate):
    #Design Bandpass filter
    lp_wp = (2.0 * 13) / sampleRate
    lp_ws = (2.0 * 13.5) / sampleRate
    hp_wp = (2.0 * 8) / sampleRate
    hp_ws = (2.0 * 7.5) / sampleRate
    wp = [hp_wp, lp_wp]
    ws = [hp_ws, lp_ws]
    gpass = 0.1
    gstop = 20
    b,a = signal.iirdesign(wp, ws, gpass, gstop, analog=False, ftype='ellip', output='ba')
    
    return b,a


def designFilter_13Hz_30Hz(sampleRate):
    #Design Bandpass filter
    lp_wp = (2.0 * 30) / sampleRate
    lp_ws = (2.0 * 30.5) / sampleRate
    hp_wp = (2.0 * 13) / sampleRate
    hp_ws = (2.0 * 12.5) / sampleRate
    wp = [hp_wp, lp_wp]
    ws = [hp_ws, lp_ws]
    gpass = 0.1
    gstop = 30
    b,a = signal.iirdesign(wp, ws, gpass, gstop, analog=False, ftype='ellip', output='ba')
    
    return b,a


def designFilter_30Hz_45Hz(sampleRate):
    #Design Bandpass filter
    lp_wp = (2.0 * 45) / sampleRate
    lp_ws = (2.0 * 45.5) / sampleRate
    hp_wp = (2.0 * 30) / sampleRate
    hp_ws = (2.0 * 29.5) / sampleRate
    wp = [hp_wp, lp_wp]
    ws = [hp_ws, lp_ws]
    gpass = 0.1
    gstop = 30
    b,a = signal.iirdesign(wp, ws, gpass, gstop, analog=False, ftype='ellip', output='ba')
    
    return b,a


def filterSignalDict_8Hz(signalDict, sampleRate):
    #Design Bandpass filter
    lp_wp = (2.0 * 8) / sampleRate
    lp_ws = (2.0 * 8.5) / sampleRate
    hp_wp = (2.0 * 0.5) / sampleRate
    hp_ws = (2.0 * 0.01) / sampleRate
    #wp = [hp_wp, lp_wp]
    #ws = [hp_ws, lp_ws]
    wp = hp_wp
    ws = hp_ws
    gpass = 0.05
    gstop = 20
    b,a = signal.iirdesign(wp, ws, gpass, gstop, analog=False, ftype='ellip', output='ba')
    b2,a2 = signal.iirdesign(lp_wp, lp_ws, gpass, gstop, analog=False, ftype='ellip', output='ba')
    
    filtered_signalDict = {}
    for electrode in signalDict:
        filtered_signal = signal.filtfilt(b, a, signalDict[electrode], method="gust")
        filtered_signal2 = signal.filtfilt(b2, a2, filtered_signal, method="gust")
        filtered_signalDict[electrode] = filtered_signal2
        
    return filtered_signalDict


#
# filterSignnalArray: Filters an array of signals
#
# @param signalArray: The signals to filter
# @param designFilterFn: The function object for the filter
# @param notchFn: Optional. The notch filter to use
# @param sampleRate: The sample rate of the signal
#
# @return The filtered signal
#
def filterSignalArray(signalArray, designFilterFn, notchFn, sampleRate):
    b,a = designFilterFn(sampleRate)
    if notchFn is not None:
        useNotchFilter = True
        b_n, a_n = notchFn(sampleRate)
    else:
        useNotchFilter = False

    filtered_signalArray = np.zeros(signalArray.shape)
    numElectrodes = signalArray.shape[0]
    
    for electrodeIdx in range(numElectrodes):
        filtered_signal = signal.filtfilt(b, a, signalArray[electrodeIdx], method="gust")
        if useNotchFilter:
            notch_filtered_signal = signal.filtfilt(b_n, a_n, filtered_signal, method="gust")
            filtered_signalArray[electrodeIdx] = notch_filtered_signal
        else:
            filtered_signalArray[electrodeIdx] = filtered_signal
        
    return filtered_signalArray


#
# filterSignnalArray: Filters a dictionary of signals
#
# @param signalDict: The signals to filter (mapping from electrode name to signals)
# @param designFilterFn: The function object for the filter
# @param notchFn: Optional. The notch filter to use
# @param sampleRate: The sample rate of the signal
#
# @return The filtered signal dictionary
#

def filterSignalDict(signalDict, designFilterFn, notchFn, sampleRate):
    b,a = designFilterFn(sampleRate)
    if notchFn is not None:
        useNotchFilter = True
        b_n, a_n = notchFn(sampleRate)
    else:
        useNotchFilter = False
        
    filtered_signalDict = {}
    for electrode in signalDict:
        filtered_signal = signal.filtfilt(b, a, signalDict[electrode], method="gust")
        if useNotchFilter:
            notch_filtered_signal = signal.filtfilt(b_n, a_n, filtered_signal, method="gust")
            filtered_signalDict[electrode] = notch_filtered_signal
        else:
            filtered_signalDict[electrode] = filtered_signal
        
    return filtered_signalDict

