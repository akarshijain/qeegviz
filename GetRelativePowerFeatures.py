from FeatureSet import FeatureSet
from GetAbsolutePowerFeatures import GetAbsolutePowerFeatures

absolutePowerFeatures = GetAbsolutePowerFeatures()

class GetRelativePowerFeatures(FeatureSet):
    
    REL_THETA_POWER = 'relativeThetaPower'
    REL_DELTA_POWER = 'relativeDeltaPower'
    REL_ALPHA_POWER = 'relativeAlphaPower'
    REL_BETA_POWER = 'relativeBetaPower'
    REL_GAMMA_POWER = 'relativeGammaPower'
    
    def _getRelativePower(self, absoluteFeature, fullPower):
        relativePower = {electrode: absoluteFeature[electrode] / fullPower.get(electrode, 0)
                        for electrode in absoluteFeature.keys()}
        
        return relativePower
    
    def getFeatureNames(self):
        return [self.REL_THETA_POWER, self.REL_DELTA_POWER, self.REL_ALPHA_POWER, self.REL_BETA_POWER, self.REL_GAMMA_POWER]
    
    def getFeatures(self, filterSignalsDict, epochs):
        
        absolutePower = {}
        absolutePower = absolutePowerFeatures.getFeatures(filterSignalsDict, epochs)
        
        relativePowerFeatures = {}
        relativePowerFeatures[self.REL_DELTA_POWER] = self._getRelativePower(absolutePower[absolutePowerFeatures.DELTA_POWER], absolutePower[absolutePowerFeatures.FULL_POWER])
        relativePowerFeatures[self.REL_THETA_POWER] = self._getRelativePower(absolutePower[absolutePowerFeatures.THETA_POWER], absolutePower[absolutePowerFeatures.FULL_POWER])
        relativePowerFeatures[self.REL_ALPHA_POWER] = self._getRelativePower(absolutePower[absolutePowerFeatures.ALPHA_POWER], absolutePower[absolutePowerFeatures.FULL_POWER])
        relativePowerFeatures[self.REL_BETA_POWER] = self._getRelativePower(absolutePower[absolutePowerFeatures.BETA_POWER], absolutePower[absolutePowerFeatures.FULL_POWER])
        relativePowerFeatures[self.REL_GAMMA_POWER] = self._getRelativePower(absolutePower[absolutePowerFeatures.GAMMA_POWER], absolutePower[absolutePowerFeatures.FULL_POWER])
        
        return relativePowerFeatures

