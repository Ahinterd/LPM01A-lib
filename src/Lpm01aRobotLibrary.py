"""
Robot Library Wrapper around LPM01A-lib from https://github.com/lazicdanilo/LPM01A-lib
"""

import string
import sys

from LPM01A import LPM01A

class Lpm01aRobotLibrary:
    def __init__(self):
        pass
    
    def LPM01A_init(self, port:string, baud_rate:int=3686400,supply_mV:int=3300, sampling_rate_hz:int=100_000, folderpath:str=None, filename:str=None):
        self.port = port
        self.baud_rate=baud_rate
        self.supply_mV = supply_mV
        self.sampling_rate_hz = sampling_rate_hz
        self.lpm = LPM01A(port=self.port, baud_rate=self.baud_rate, folderpath=folderpath, filename=filename)
        self.lpm.init_device(mode="ascii",voltage=self.supply_mV, freq=self.sampling_rate_hz, duration=0)
        
    def LPM01A_start(self):
        if self.lpm is None:
            return
        self.lpm.start_capture()
        
    def LPM01A_stop(self):
        if self.lpm is None:
            return
        self.lpm.stop_capture()
    def LPM01A_deinit(self):
        if self.lpm is None:
            return
        self.lpm.deinit_capture()
    def LPM01A_get_average_current(self) -> int:
        if self.lpm is None:
            return
        return self.lpm.get_average_current()
