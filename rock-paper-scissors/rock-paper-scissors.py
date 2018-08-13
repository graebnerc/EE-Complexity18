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
        """Constructor method. 
        It is called whenever you create an instance of the class.
        """
        self.strategy = np.random.randint(0, 3) # creates the instance variable "strategy", which is assigned a random integer 0, 1, or 2
        self.payoff = 0 # creates the instance variable "payoff". After being instantiated every Agent starts with zero payoff
    
    def get_strategy(self):
        """Getter method for agent strategy"""
        return self.strategy # Simply return the value of the instance variable "strategy"
    
    def receive_payoff(self, amount):
        """Method for handing payoff to the agent"""
        self.payoff += amount # Increase the instance variable "payoff" by adding "amount" to it. "amount" must be specified as an argument of the method
        
    def reset_payoff(self):
        """Method for returning sum of payoffs and
           setting the sum of payoffs to 0 for the
           following iteration.
           """
        p = self.payoff # define, as an intermediate step, the variable p (which will be deleted after the method has been executed)
        self.payoff = 0 # the instance variable "payoff" will be set to zero
        return p # the function returns the value of the variable p (which has been defined before)

    def new_strategy(self):
        """Method to assign a new strategy"""
        self.strategy = np.random.randint(0, 3) # the instance variable "strategy" will be set randomly to 0, 1, or 2

class Simulation():
    def __init__(self):
        """Constructor method"""
        self.number_agents = 100 # The simulation always starts with 100 agents, therefore we set the instance variable "number_agents" to 100
        self.max_time = 250 # The instance variable "max_time" is alwyss instantiated with value "250"
        self.games_per_iteration = 10 * \
                              self.number_agents # In every round there should be ten times as many games played, as there are agents
        self.history = [[], [], []] # To save the simulation results we create a list that consists of three empty lists.
        self.agent_list = [] # We create an empty list. Later, we will place the agents into this list
        for i in range(self.number_agents): # we loop through a list of indices. It starts at 0 and has as many entries as there should be agents
            new_agent = Agent() # we create a new instance of class Agents
            self.agent_list.append(new_agent) #  we place this instance into the list created three lines above

    def run(self):
        """Method to control the simulation run"""
        for t in range(self.max_time):
            """randomly matched games"""
            for i in \
                   range(self.games_per_iteration): # for the number of games to be played in every time step...
                a1, a2 = np.random.choice( # we choose two agents at random
                        self.agent_list, # we choose the agents from the agent_list (that contains the instances of all agents)
                        size = 2, # we tell python that we do want to get two agents out of the list
                        replace = False) # we tell python it should not replace agents, otherwise an agent could play against herself
                self.game(a1, a2) # call the method "game", which is defined below and matches two agents, both to be given as an argument
            
            """collect history data""" # place a zero to all three lists tracking the history of the simulation
            self.history[0].append(0) # These three lists contain the number of agents currently playing this strategy
            self.history[1].append(0) # Below we go through all agents and increment the counter for every strategy by one if we find an agent that plays this strategy
            self.history[2].append(0)
            
            #for i in range(len(self.history)): # this would be an equivalent way to do this
            #    self.history[i].append(0)
            
            payoffs = [] # create an empty list
            for a in self.agent_list: # go through all agents
                p = a.reset_payoff() # resent the payoff of the current agent by calling her reset_payoff method. This method also returns the current payoff of the agent
                payoffs.append(p) # take this current payoff and append it to the list created three lines earlier
                s = a.get_strategy() # get the strategy of the current agent
                self.history[s][t] += 1 # increase the counter for agents playing this strategy in time t by 1
                
            """evolution"""
            a_change = np.argmin(payoffs) # Returns the indice of the minimum values in the list "payoffs"
            self.agent_list[a_change].new_strategy() #  We use this indice to spot the worst agent and to let him choose a new strategy
            
            print("\r Completed time step {0} / {1}".format( # print the current time step of the simulation
                                 t, self.max_time), end="")
        
        self.plot()
            
        
    def game(self, a1, a2): # this method takes two arguments: the two agents to be matched against each other
        """Method for handling a single game"""
        a1_strat = a1.get_strategy() # get the strategy of the first agent
        a2_strat = a2.get_strategy() # get the strategy of the second agent
        # now go through all possible variants and allocate payoffs
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
        a1.receive_payoff(p1) # call the method 'receive_payoff' for player 1, and provide the payoff received as an argument
        a2.receive_payoff(p2) # call the method 'receive_payoff' for player 2, and provide the payoff received as an argument

    def plot(self):
        """Method for plotting the simulation results"""
        colors = ["r", "g", "b"] # define the colors for the different lines in the plot
        for i in range(len(self.history)): # for each list containing info on the nb of users of a particular strategy do the following:
            time_list = list( # Create a list for the x axis, spanning from zero to the maximum nb of time steps
                    range(len(self.history[i])))
            plt.plot(time_list, # The x axis is the list just created
                     self.history[i], # The y axis are the number of users of the strategy currently considered
                     colors[i]) # set the color of the line in the plot
        plt.show() # show the plow


S = Simulation() # create an instance of the simulation class
S.run() # run the simulation
