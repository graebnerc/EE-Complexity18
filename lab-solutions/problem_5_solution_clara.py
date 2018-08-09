#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 10:28:15 2018

@author: clara
"""

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class Simulation():
    def __init__(self):
        self.no_of_agents = 3000
        self.g = nx.barabasi_albert_graph(self.no_of_agents, 5)
        self.infection_prob = 0.05
        self.agents = []
        self.max_t = 250
        self.timelist=[]
        self.history=[ [],[],[],[] ]
        self.vulnerable_list=[] #not yet infected agents
        self.immune_list = [] #immune agents
        self.infected_list = [] #infected agents
        self.dead_list = [] #dead agents
        self.figure = None
        #self.figure_exes = None
        for i in range(self.g.number_of_nodes()):
            agent = Agent(self, self.g,i)
            self.agents.append(agent)
            self.g.node[i]["agent"] = agent
       
        #print(self.agents)
        
    def run(self):
        #seed epidemic
        patient_zero_id = np.random.choice(self.g.nodes())
        """patient_zero müsste type agent sein..."""
        patient_zero = self.g.node[patient_zero_id]["agent"] 
        patient_zero.become_infected()
        print("patient zero", patient_zero_id)
        
        for t in range(self.max_t):
            self.timelist.append(t)           
            immune =[a for a in self.agents if (a.is_immune() and a.is_dead()== False)]
            infected =[a for a in self.agents if (a.is_infected() and a.is_dead()== False)]
            vulnerable = [a for a in self.agents if (a.is_infected() == False and \
                          a.is_immune() == False and a.is_dead()== False)]
            dead = [a for a in self.agents if a.is_dead()==True]
            self.history[0].append(len(vulnerable))
            self.history[1].append(len(infected))
            self.history[2].append(len(immune))
            self.history[3].append(len(dead))
            assert (len(vulnerable) + len(infected) + len(immune) + len(dead) \
                    == self.no_of_agents), "too many agents..."
            #dead
            for agent in self.agents:
                agent.iterate()
         
            self.plot(interactive=True,time=t)
            
        self.plot(interactive=False,time=-1)
    
    def plot(self, interactive, time):
        #print("tot", self.dead_list[-1], "immune", self.immune_list[-1], \
         #     "vulnerable", self.vulnerable_list[-1], "infected", self.infected_list[-1])
        colors = ["r", "g", "b", "m"]
        names = ["vulnerable", "infected", "immune", "dead"]
        
        if self.figure is None:
            self.figure = plt.figure()
            self.figure_axes = self.figure.add_subplot(1, 1, 1)
            self.figure_axes.set_xlabel("Time")
            self.figure_axes.set_ylabel("Number of Agents")
            self.figure_axes.set_xlim(0, self.max_t)
            self.figure_axes.set_ylim(0, self.no_of_agents)
            
        
        if interactive:
            plt.ion()
            
            for i in range(len(self.history)):
                if len(self.history[i]) > 1:                    
                    self.figure_axes.plot(self.timelist[-2:], self.history[i][-2:], colors[i],\
                                          label = names[i])
            if time == 1:
                plt.legend()
                plt.title("Infection probablity "+str(self.infection_prob))
            plt.draw()
            plt.pause(.001)
        else:
            plt.ioff()
            plt.show()

        
    
         

class Agent():
    
    def __init__(self,S,graph,node_id):
        self.simulation = S
        self.g=graph
        self.node_id = node_id
        self.infected = False
        self.immune = False
        self.dead = False       
        self.time_infected = 0 #number of timesteps the current infection lasts
        self.time_immune = 0
        
    """become infected"""
    def become_infected(self):
        if self.infected == False:
            self.infected = True
            self.time_infected = 0
            
    
    """become immune"""
    def become_immune(self):
        self.infected=False
        self.immune= True
        self.time_immune=0
        
    """get neighbors of this agent"""
    def get_neighbors(self):
        return nx.neighbors(self.g, self.node_id)
    
    """returns whether an agent is infected or not"""
    def is_infected(self):
        return self.infected
    
    def is_immune(self):
        return self.immune
    
    def is_dead(self):
        return self.dead
    
    """agent dies *.* """
    def rip(self):
        #self.g.remove_edges_from(self.g.edges(self.node_id))
        self.dead = True
       
        
        
    
    def iterate(self):
        #print("Agent number", self.node_id)
        if self.dead == True:
            return 0
        
        if self.infected == True: #infected patient might die
            d = np.random.random()
            if d < 0.01:
                self.rip()
                                
            elif self.time_infected == 9:
                self.become_immune() #after 10 timesteps patient becomes immune
                
            else: self.time_infected += 1
            
        elif self.immune == False:
            nb = list(self.get_neighbors())
            
            "go through all neighbors of this agent"""
            for i in range(len(nb)):                
                """check if neighbor with id i is infected"""
                if (self.g.node[nb[i]]["agent"].is_infected() == True \
                    and self.g.node[nb[i]]["agent"].is_dead() == False):
                    """if yes, infect this agent with probability of 10%"""
                    p = np.random.random()                
                    if p < self.simulation.infection_prob:
                        self.become_infected()
                        
        elif self.immune == True and self.time_immune == 14:
            self.immune = False
            self.time_immune = 0
            
            
        else: self.time_immune +=1

S=Simulation()
S.run()

                    
            
            
            
            
    

        
    