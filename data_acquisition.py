#!/bin/env python3

import time
from src.LPM01A import LPM01A


try:
    lpm = LPM01A(port="/dev/ttyACM1", baud_rate=3686400, print_info_every_ms=10_000, folderpath="./lpm01a_csv_files", filename="test.csv")
    lpm.init_device(mode="ascii", voltage=3300, freq=1000, duration=0)
    lpm.start_capture()
    time.sleep(1)
    print(f"Average current = {lpm.get_average_current()}")        
    
except KeyboardInterrupt:
    print("KeyboardInterrupt detected. Exiting...")    
finally:
    lpm.stop_capture()
    lpm.deinit_capture()
    exit(0)
