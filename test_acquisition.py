#!/bin/env python3

from src.LPM01A import LPM01A

try:
    lpm = LPM01A(port="/dev/ttyACM0", baud_rate=3864000, print_info_every_ms=10_000)
    lpm.init_device(mode="ascii", voltage=3300, freq=1000, duration=0)
    lpm.start_capture()
    data = lpm.read_and_parse_data()
    if data is not None:
        print(
        f"Average current for previous {data[0]} ms: {data[1]} uA\n"
        f"Local timestamp: {data[2]} ms\n"
        f"Num of received values: {data[3]}\n"
        f"LPM01A buffer usage: {data[4]}%\n"                    
    )
except KeyboardInterrupt:
    print("KeyboardInterrupt detected. Exiting...")    
finally:
    lpm.stop_capture()
    lpm.deinit_capture()
    exit(0)
