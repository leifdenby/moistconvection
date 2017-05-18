import numpy as np

class RICO_SCM:
    @np.vectorize
    def temp(self, z):
        if 0.0 <= z < 740.:
            return 299.2 + (292.0 - 299.2) / (740) * z 
        elif 740 < z < 4000:
            return 292.0 + (278.0 - 292.0) / (4000 - 740) * (z - 740)
        elif 4000 < z < 15000:
            return 278.0 + (203.0 - 278.0) / (15000 - 4000) * (z - 4000)
        elif 15000 < z < 17500:
            return 203.0 + (194.0 - 203.0) / (17500 - 15000)* (z - 15000)
        elif 17500 < z < 20000:
            return 194.0 + (206.0 - 194.0) / (20000 - 17500)* (z - 17500)
        elif 20000 < z < 60000:
            return 206.0 + (270.0 - 206.0) / (60000 - 20000)* (z - 20000) 
        else:
            raise Exception("z out of range")

    def q_v(self, z):
        """ Water vapour specific concentration in [kg/kg]"""
        return self._q_v(z)/1000.

    @np.vectorize
    def _q_v(z):
        if 0 <= z < 740:
            return 16.0 + (13.8 - 16.0) / (740) * z
        elif 740 < z < 3260:
            return 13.8 + (2.4 - 13.8) / (3260 - 740) * (z - 740)
        elif 3260 < z < 4000:
            return 2.4 + (1.8 - 2.4) / (4000 - 3260) * (z - 3260)
        elif 4000 < z < 9000:
            return 1.8 + (0 - 1.8) / (10000 - 4000) * (z - 4000)
        else:
            return 0.0
