#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path

def remova(filename):
    if os.path.isfile(filename):
        os.remove(filename)
        return True
    return False