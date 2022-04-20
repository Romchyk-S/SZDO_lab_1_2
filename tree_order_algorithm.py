# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 17:19:35 2022

@author: romas
"""

import copy as c


def tree_order(tree, h):
    
    tree_for_marking = c.deepcopy(tree)
    
    marking(tree_for_marking)
    
    build_ordering(tree, h)
    
    return 0

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

def build_ordering(tree, h):
    
    temp_arr = []
    
    return 0