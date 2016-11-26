#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
A Python program using ciscoconfparse that parses a config file. Note, this
config file is not fully valid (i.e. parts of the configuration are missing).
The script will find all of the crypto map entries in the file (lines
that begin with 'crypto map CRYPTO') and for each crypto map entry print
out its children.
"""
