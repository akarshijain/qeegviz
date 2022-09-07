import signalFilters

def getFilterSignals(signalsDict, sampleRate):
        
    filterSignalsDict = {}
    filterSignalsDict['fullPower'] = signalFilters.filterSignalDict(signalsDict, signalFilters.designFilter_70Hz_noNotch, None, sampleRate)      
    filterSignalsDict['deltaPower'] = signalFilters.filterSignalDict(signalsDict, signalFilters.designFilter_4Hz, None, sampleRate)
    filterSignalsDict['thetaPower'] = signalFilters.filterSignalDict(signalsDict, signalFilters.designFilter_4Hz_8Hz, None, sampleRate)
    filterSignalsDict['alphaPower'] = signalFilters.filterSignalDict(signalsDict, signalFilters.designFilter_8Hz_13Hz, None, sampleRate)
    filterSignalsDict['betaPower'] = signalFilters.filterSignalDict(signalsDict, signalFilters.designFilter_13Hz_30Hz, None, sampleRate)
    filterSignalsDict['gammaPower'] = signalFilters.filterSignalDict(signalsDict, signalFilters.designFilter_30Hz_45Hz, None, sampleRate)
    
    return filterSignalsDict

