# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 16:58:41 2022

@author: romas
"""


import random as r

import vertex_class as vc

import treelib as tl



def build_tree(levels):
    
    vert_arr = []
    
    root_vertex = vc.Vertex(1, [], [])
    
    vert_arr.append([root_vertex])
    
    tree = tl.Tree()
    
    tree.create_node(root_vertex, root_vertex)
    
    created_vertices = 1
    
    
    i = 0
    
    while i < levels-1:
        
        vert_arr_temp = []
            
        while len(vert_arr_temp) == 0:
            
            vert_arr_temp, created_vertices, tree = create_level(created_vertices, vert_arr[i], tree)
            
        vert_arr.append(vert_arr_temp)
        
        i += 1
    
    tree.show()

    return vert_arr

def create_level(vert_count, vertices_prev_level, tree):

    i = 0 
    
    vert_arr_temp = []    
    
    while i < len(vertices_prev_level):
    
        new_vertices = r.randint(0, 3)
    
        j = 0
        
        while j < new_vertices:
            
            new_vert = vc.Vertex(vert_count+j+1, [], [])
            
            vert_arr_temp.append(new_vert)
            
            vertices_prev_level[i].connect_vertex(new_vert)
            
            tree.create_node(new_vert, new_vert, parent = vertices_prev_level[i])
            
            j += 1
            
        vert_count += new_vertices
        
        i += 1
     
    return vert_arr_temp, vert_count, tree
