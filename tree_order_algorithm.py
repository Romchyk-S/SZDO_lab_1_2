# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 17:19:35 2022

@author: romas
"""

import copy as c


def tree_order(tree, h):
    
    tree_for_marking = c.deepcopy(tree)
    
    marking(tree_for_marking)
    
    tree_for_ordering = c.deepcopy(tree)
    
    res_arr = build_ordering(tree_for_ordering, h, [])
    
    return res_arr

def marking(tree_1):
    
    
    r = 0
    
    while r < len(tree_1):
        
        i = 0
        
        while i < len(tree_1[r]):
            
            if(tree_1[r][i].count_connections_out_arr(tree_1) == 0):
                
                tree_1[r][i].add_mark(r+1)
            
            i += 1
        
        r += 1
        
        
    tree_len = 0
        
    for t in tree_1:
        
        for v in t:
            
            if v.check_mark_exists():
                
                t.remove(v)
                
            tree_len += 1
                
    if tree_len == 0:
        
        return 0
    
    else:
        
        marking(tree_1)
        
        return 0
    
def create_marked_arr():
    
    return 0

def build_ordering(tree, h, res_arr):
    
    temp_arr = []
    
    tree_len = 0
    
    
    for t in tree:
        
        for v in t:
            
            if v.count_connections_in_arr(tree) == 0:
                
                temp_arr.append(v)
                
            tree_len += 1
                
    if len(temp_arr) > h:
        
        desired_length = len(temp_arr) - h
        
        while len(temp_arr) > desired_length:
            
            temp_arr.remove(temp_arr[0])
            
    for v in temp_arr:
        
        for t in tree:
            
            if v in t:
    
                t.remove(v)
                
    if len(temp_arr) != 0:
        
        res_arr.insert(0, temp_arr)
        
    if tree_len == 0:
        
        return res_arr
    
    else:
        
        res_arr = build_ordering(tree, h, res_arr)
        
        return res_arr