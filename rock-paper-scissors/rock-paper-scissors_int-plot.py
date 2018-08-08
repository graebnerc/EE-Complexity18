#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:15:44 2018

@author: Torsten Heinrich
"""

import numpy as np
import matplotlib.pyplot as plt

"""Agent class"""
class Agent():
    def __init__(self):
        """Constructor method"""
        self.strategy = np.random.randint(0, 3)
        self.payoff = 0
    
    def get_strategy(self):
        """Getter method for agent strategy"""
        return self.strategy
    
    def receive_payoff(self, amount):
        """Method for handing payoff to the agent"""
        self.payoff += amount
        
    def reset_payoff(self):
        """Method for returning sum of payoffs and
           setting the sum of payoffs to 0 for the
           following iteration."""
        p = self.payoff
        self.payoff = 0
        return p

    def new_strategy(self):
        """Method to assign a new strategy"""
        self.strategy = np.random.randint(0, 3)

class Simulation():
    def __init__(self):
        """Constructor method"""
        self.number_agents = 100
        self.max_time = 250
        self.games_per_iteration = 10 * \
                              self.number_agents
        self.history = [[], [], []]
        self.time_hist = []
        self.agent_list = []
        self.figure = None
        self.figure_exes = None
        for i in range(self.number_agents):
            new_agent = Agent()
            self.agent_list.append(new_agent)

    def run(self):
        """Method to control the simulation run"""
        for t in range(self.max_time):
            self.time_hist.append(t)
            
            """randomly matched games"""
            for i in \
                   range(self.games_per_iteration):
                a1, a2 = np.random.choice(
                        self.agent_list,
                        size = 2,
                        replace = False)
                self.game(a1, a2)
            
            """collect history data"""
            self.history[0].append(0)
            self.history[1].append(0)
            self.history[2].append(0)
            
            #for i in range(len(self.history)):
            #    self.history[i].append(0)
            
            payoffs = []
            for a in self.agent_list:
                p = a.reset_payoff()
                payoffs.append(p)
                s = a.get_strategy()
                self.history[s][t] += 1
                
            """evolution"""
            a_change = np.argmin(payoffs)
            self.agent_list[a_change].new_strategy()
            
            print("\r Completed time step {0} / {1}".format(
                                 t+1, self.max_time), end="")
        
            self.plot(interactive=True)
        self.plot(interactive=False)
            
        
    def game(self, a1, a2):
        """Method for handling a single game"""
        a1_strat = a1.get_strategy()
        a2_strat = a2.get_strategy()
        
        if a1_strat == a2_strat:
            """draw"""
            p1, p2 = 0, 0
        elif a1_strat == 0 and a2_strat == 1:
            """a2 wins"""
            p1, p2 = -1, 1
        elif a1_strat == 0 and a2_strat == 2:
            """a1 wins"""
            p1, p2 = 1, -1            
        elif a1_strat == 1 and a2_strat == 0:
            """a1 wins"""
            p1, p2 = 1, -1            
        elif a1_strat == 1 and a2_strat == 2:
            """a2 wins"""
            p1, p2 = -1, 1
        elif a1_strat == 2 and a2_strat == 0:
            """a2 wins"""
            p1, p2 = -1, 1
        elif a1_strat == 2 and a2_strat == 1:
            """a1 wins"""
            p1, p2 = 1, -1
        a1.receive_payoff(p1)
        a2.receive_payoff(p2)

    def plot(self, interactive):
        """Method for plotting the simulation results"""
        colors = ["r", "g", "b"]
        if self.figure is None:
            self.figure = plt.figure()
            self.figure_axes = self.figure.add_subplot(1, 1, 1)
            self.figure_axes.set_xlabel("Time")
            self.figure_axes.set_xlabel("Number of Agents")
            self.figure_axes.set_xlim(0, 252)
            self.figure_axes.set_ylim(20, 50)
        
        if interactive:
            plt.ion()
            
            for i in range(len(self.history)):
                if len(self.history[i]) > 1:
                    #print(self.time_hist[-2:], self.strategies_hist[i][-2:])
                    self.figure_axes.plot(self.time_hist[-2:], self.history[i][-2:], colors[i])
            plt.draw()
            plt.pause(.01)
        else:
            plt.ioff()
            plt.show()

S = Simulation()
S.run()
