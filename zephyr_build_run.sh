#!/bin/bash

## Build and run Zephyr
west build -p=auto -b qemu_x86 fw_test/lwm2m_client -p -- -DCONF=overlay-lwm2m-1.1.conf
west build -t run
