#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solutions for the second problem set at the Exploring Economics Summer School 2018

@author: Claudius Graebner
@email: claudius@claudius-graebner.com

Note: There are many more solutions to the tasks, and often there is not really
the 'best' way to do it.

There is also a more extensive explanation on the data analysis available on 
the course homepage.

The code assumes that in your working directory you have:

- a folder "output" in which you save the plots
- a folder "data" with the gml files of the graphs

"""

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#%% Import the graphs
# Underlying data comes from https://github.com/mathbeveridge/asoiaf

book1 = nx.read_gml("data/GoT_book1.gml")
book5 = nx.read_gml("data/GoT_book5.gml")
books = [book1, book5]

#%% Visualize the network

fig, ax = plt.subplots(figsize=(30,30))
nx.draw(book5, with_labels=True, node_color="#00a3cc", ax=ax)
plt.savefig("output/graph-normal.pdf", bbox_inches="tight") 

#%% Calculate transitivity

got_book1_trans = nx.transitivity(book1)
got_book5_trans = nx.transitivity(book5)

# One way to make sense of the clustering in GoT is to look at it over time.
# Did clustering increase over the books?

trans_books = [got_book1_trans, got_book5_trans]
plt.plot([1,5], trans_books)

# Compare this to the random graph

import scipy.special
nb_vertices = [book1.number_of_nodes(),
              book5.number_of_nodes()]
nb_edges = [book1.number_of_edges(),
              book5.number_of_edges()]

expected_clustering = []
for i in range(len(nb_vertices)):
    expected_clustering.append(nb_edges[i]/scipy.special.binom(nb_edges[i], 2))

fig, ax = plt.subplots()
ax.plot([1,5], trans_books)
ax.plot([1,5], expected_clustering)

plt.savefig("output/GoT-transitivity.pdf", bbox_inches="tight") 

#%% Degree centrality

deg_cens = [nx.degree_centrality(books[i]) for i in range(len(books))] 

fig, axes = plt.subplots(1,2, figsize=(12,4))

axes[0].spines["top"].set_visible(False) # Remove plot frame line on the top 
axes[0].spines["right"].set_visible(False) # Remove plot frame line on the right
axes[0].get_xaxis().tick_bottom()  # Remove ticks on the bottom
axes[0].get_yaxis().tick_left()  # Remove the ticks on the left
axes[0].hist(deg_cens[0].values(), color="#3F5D7D", density=True)
axes[0].set_title("Degree centrality in the first book")
axes[0].set_xlabel("Normalized degree")
axes[0].set_ylabel("Nb of vertices")

axes[1].spines["top"].set_visible(False) # Remove plot frame line on the top 
axes[1].spines["right"].set_visible(False) # Remove plot frame line on the right
axes[1].get_xaxis().tick_bottom()  # Remove ticks on the bottom
axes[1].get_yaxis().tick_left()  # Remove the ticks on the left
axes[1].hist(deg_cens[1].values(), color="#3F5D7D", density=True)
axes[1].set_title("Degree centrality in the fifth book")
axes[1].set_xlabel("Normalized degree")
axes[1].set_ylabel("Nb of vertices")
plt.tight_layout(True) # Good to get better alignment

plt.savefig("output/centrality_pagerank_hist.pdf", bbox_inches="tight") 


# Print the dictionary, sorted according to dictionary values

sorted(deg_cens[0].items(), key=lambda x:x[1], reverse=True)[0:10] # Look at top 10

sorted(deg_cens[1].items(), key=lambda x:x[1], reverse=True)[0:10]

# Color the nodes according to degree centrality

fig, ax = plt.subplots(figsize=(30,30))
nx.draw(book5, with_labels=True, node_color=list(deg_cens[1].values()), 
        ax=ax)


#%% Eigenvector centrality

eigen_cens = [nx.pagerank(books[i]) for i in range(len(books))] # this is a dictionary

fig, axes = plt.subplots(1,2, figsize=(12,4))

axes[0].spines["top"].set_visible(False) # Remove plot frame line on the top 
axes[0].spines["right"].set_visible(False) # Remove plot frame line on the right
axes[0].get_xaxis().tick_bottom()  # Remove ticks on the bottom
axes[0].get_yaxis().tick_left()  # Remove the ticks on the left
axes[0].hist(eigen_cens[0].values(), color="#3F5D7D", density=True)
axes[0].set_title("Eigenvector centrality in the first book")
axes[0].set_xlabel("PageRank score")
axes[0].set_ylabel("Nb of vertices")

axes[1].spines["top"].set_visible(False) # Remove plot frame line on the top 
axes[1].spines["right"].set_visible(False) # Remove plot frame line on the right
axes[1].get_xaxis().tick_bottom()  # Remove ticks on the bottom
axes[1].get_yaxis().tick_left()  # Remove the ticks on the left
axes[1].hist(eigen_cens[1].values(), color="#3F5D7D", density=True)
axes[1].set_title("Eigenvector centrality in the fifth book")
axes[1].set_xlabel("PageRank score")
axes[1].set_ylabel("Nb of vertices")
plt.tight_layout(True) # Good to get better alignment

plt.savefig("output/centrality_degree-centrality_hist.pdf", bbox_inches="tight") 

sorted(eigen_cens[0].items(), key=lambda x:x[1], reverse=True)[0:10] # Look at top 10

sorted(eigen_cens[1].items(), key=lambda x:x[1], reverse=True)[0:10] # Look at top 10

fig, ax = plt.subplots(figsize=(30,30))
nx.draw(book5, with_labels=True, node_color=list(eigen_cens[1].values()), 
        ax=ax)

plt.savefig("output/centrality_degree-centrality_graph.pdf", bbox_inches="tight") 

#%% Betweenness centrality

between_cens = [nx.betweenness_centrality(books[i]) for i in range(len(books))] # this is a dictionary

eigen_cens = [nx.pagerank(books[i]) for i in range(len(books))] # this is a dictionary

fig, axes = plt.subplots(1,2, figsize=(12,4))

axes[0].spines["top"].set_visible(False) # Remove plot frame line on the top 
axes[0].spines["right"].set_visible(False) # Remove plot frame line on the right
axes[0].get_xaxis().tick_bottom()  # Remove ticks on the bottom
axes[0].get_yaxis().tick_left()  # Remove the ticks on the left
axes[0].hist(between_cens[0].values(), color="#3F5D7D", density=True)
axes[0].set_title("Betweenness centrality in the first book")
axes[0].set_xlabel("PageRank score")
axes[0].set_ylabel("Nb of vertices")

axes[1].spines["top"].set_visible(False) # Remove plot frame line on the top 
axes[1].spines["right"].set_visible(False) # Remove plot frame line on the right
axes[1].get_xaxis().tick_bottom()  # Remove ticks on the bottom
axes[1].get_yaxis().tick_left()  # Remove the ticks on the left
axes[1].hist(between_cens[1].values(), color="#3F5D7D", density=True)
axes[1].set_title("Betweenness centrality in the fifth book")
axes[1].set_xlabel("PageRank score")
axes[1].set_ylabel("Nb of vertices")
plt.tight_layout(True) # Good to get better alignment

plt.savefig("output/centrality_pagerank_hist.pdf", bbox_inches="tight") 

sorted(between_cens[0].items(), key=lambda x:x[1], reverse=True)[0:10] # Look at top 10

sorted(between_cens[1].items(), key=lambda x:x[1], reverse=True)[0:10] # Look at top 10

fig, ax = plt.subplots(figsize=(30,30))
nx.draw(book5, with_labels=True, 
        node_color=list(between_cens[1].values()), 
        ax=ax)

plt.savefig("output/centrality_pagerank_graph.pdf", bbox_inches="tight") 


#%% Optional: Comparison of the centrality measurs

# We now create a plot with three panes, a histogram for each measure

fig, axes = plt.subplots(1,3, figsize=(12,4))
for x in range(3):
    axes[x].spines["top"].set_visible(False) # Remove plot frame line on the top 
    axes[x].spines["right"].set_visible(False) # Remove plot frame line on the right
    axes[x].get_xaxis().tick_bottom()  # Remove ticks on the bottom
    axes[x].get_yaxis().tick_left()  # Remove the ticks on the left

axes[0].scatter(deg_cens[1].values(), eigen_cens[1].values(), color="#3F5D7D")
axes[0].set_title("Degree vs. Eigenvector centrality")

axes[1].scatter(deg_cens[1].values(), between_cens[1].values(), color="#3F5D7D")
axes[1].set_title("Degree vs. Betweenness centrality")

axes[2].scatter(eigen_cens[1].values(), between_cens[1].values(), color="#3F5D7D")
axes[2].set_title("Eigenvector vs. Betweenness centrality")

plt.tight_layout(True) # Good to get better alignment

plt.savefig("output/comparison-centralities.pdf", bbox_inches="tight") 

