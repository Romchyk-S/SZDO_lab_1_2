# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 15:51:07 2022

@author: romas
"""

import graph as g

import S_algorithms as s

import tree as t


def graph_ordering(num, connect):
    
    vert_arr, connections = g.build_graph(num)

    g.show_graph(connections)

    s_upper_res = s.s_upper(vert_arr)
    
    s_lower_res = s.s_lower(vert_arr)
    
    return s_upper_res, s_lower_res

def tree_ordering(num):
    
    t.build_tree(num)
    
    return 0