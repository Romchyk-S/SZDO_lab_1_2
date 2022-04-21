# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 17:19:35 2022

@author: romas
"""

import copy as c


def tree_order(tree, h):
    
    tree_for_ordering = c.deepcopy(tree)
    
    res_arr = build_ordering(tree_for_ordering, h, [])
    
    return res_arr

def build_ordering(tree, h, res_arr):
    
    temp_arr = []
    
    tree_len = 0
    
    
    for t in tree:
        
        for v in t:
            
            if v.count_connections_in_arr(tree) == 0:
                
                temp_arr.append(v)
                
            tree_len += 1

    
    while len(temp_arr) > h:
        
        temp_arr.remove(temp_arr[0])
        
    for v in temp_arr:
        
        for t in tree:
            
            if v in t:
    
                t.remove(v)
                
    if len(temp_arr) != 0:
        
        res_arr.append(temp_arr[::-1])
        
    if tree_len == 0:
        
        return res_arr
    
    else:
        
        res_arr = build_ordering(tree, h, res_arr)
        
        return res_arr