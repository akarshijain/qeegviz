ELECTRODE_LIST = ['Fp1','Fp2','F3','F4','C3','C4','P3','P4','O1','O2',
                  'F7','F8','T3','T4','T5','T6','Fz','Cz','Pz']
FEATURE_DICT = {'AbsolutePowerFeature': ['fullPower', 'alphaPower', 'betaPower', 
                'deltaPower', 'gammaPower', 'thetaPower'], 
                'RelativePowerFeature': ['relativeAlphaPower', 'relativeBetaPower', 
                'relativeThetaPower', 'relativeGammaPower', 'relativeDeltaPower']}

def getFeatureList(featureName):
    return FEATURE_DICT[featureName]

def getFeatureName():
    return list(FEATURE_DICT.keys())
    
def getElectrodeList():
    return ELECTRODE_LIST