#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:15:44 2018

@author: Torsten Heinrich
"""
import numpy as np

class Agent():
    def __init__(self):
        self.strategy = np.random.randint(0, 3)
        self.payoff = 0
    
    def get_strategy(self):
        return self.strategy
    
    def receive_payoff(self, amount):
        self.payoff += amount
        
    def reset_payoff(self):
        p = self.payoff
        self.payoff = 0
        return p

    def new_strategy(self):
        self.strategy = np.random.randint(0, 3)

a = Agent()
b = Agent()