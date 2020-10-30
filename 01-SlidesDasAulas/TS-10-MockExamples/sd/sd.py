#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import mean

def std_calc(data):
	
	n = len(data)
	if n <= 1:
		return 0.0

	avg = mean.avg_calc(data)

	std = 0.0

	for i in data:
		std += (float(i) - avg)**2

	std = math.sqrt(std / float(n-1))

	return std