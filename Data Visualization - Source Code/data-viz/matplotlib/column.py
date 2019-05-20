#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pickle

# load our data (rb means read binary data)
with open('fruit-sales.pickle', 'rb') as f:
    data = pickle.load(f)

print(data)
