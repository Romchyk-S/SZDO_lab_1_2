# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 16:53:05 2022

@author: romas
"""


import random as r

import vertex_class as vc

import networkx as nx

import matplotlib.pyplot as plt


def build_graph(quant):

   vert_arr = []

    
   i = 1

   while i <= quant:
       
       vert_arr.append(vc.Vertex(i, [], []))
       
       i += 1
       

   i = 0

   while i < quant:
       
       connected_vertices = r.sample(vert_arr, 2)
       
       if not(connected_vertices[0].check_already_connected(connected_vertices[1])) and not(connected_vertices[0].check_backward_connection(connected_vertices[1])):
       
           connected_vertices[0].connect_vertex(connected_vertices[1]) 
       
           i += 1

   for v in vert_arr:
       
       if len(v.get_connections_in()) == 0 and len(v.get_connections_out()) == 0:
           
           num = r.randint(0, 1)
           
           v_1 = r.sample(vert_arr, 1)[0]
           
           while v_1.get_index() == v.get_index():
               
               v_1 = r.sample(vert_arr, 1)[0]
           
           if num == 0:
               
               v.connect_vertex(v_1)
               
           else:
               
               v_1.connect_vertex(v)


   connections = []

   for v in vert_arr:
       
       connected_arr = v.get_connections_out()
       
       if len(connected_arr) > 0:
           
           for t in connected_arr:
               
               connections.append((v, t))
               

   print("Зв'язки між вершинами: ")

   print(connections)

   print() 
   
   return vert_arr, connections

def show_graph(connections):
    
    G = nx.DiGraph()

    G.add_edges_from(connections)

    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size = 250)

    nx.draw_networkx_labels(G, pos)

    nx.draw_networkx_edges(G, pos, arrows = True)

    plt.show()