# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 15:51:07 2022

@author: romas
"""

import graph as g

import S_algorithms as s

import tree as t

import tree_order_algorithm as tro


def graph_ordering(num_vert):
    
    vert_arr, connections = g.build_graph(num_vert)

    g.show_graph(connections)

    s_upper_res = s.s_upper(vert_arr)
    
    s_lower_res = s.s_lower(vert_arr)
    
    return s_upper_res, s_lower_res

def tree_ordering(num_levels, width, num_child_vert):
    
    tree_created = t.build_tree(num_levels, num_child_vert)
    
    tree_order_res = tro.tree_order(tree_created, width)
    
    return tree_order_res