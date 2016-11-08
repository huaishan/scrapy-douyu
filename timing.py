#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time

sleep_time = 5 * 60

while True:
    os.system(r'timing.bat')
    print 'Sleep {0}s...'.format(sleep_time)
    time.sleep(sleep_time)
