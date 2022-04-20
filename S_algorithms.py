# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:08:25 2022

@author: romas
"""

def s_upper(vert_arr):
    
    res_arr = []
    
    vert_arr_copy = vert_arr.copy()
    
    res_arr = build_s_upper(vert_arr_copy, res_arr)
    
    return res_arr

def build_s_upper(vert_arr_copy, res_arr):
    
    temp_arr = []
    
    for v in vert_arr_copy:
        
        if v.count_connections_out_arr(vert_arr_copy) == 0:
            
            temp_arr.append(v)
                
    for v in temp_arr:
        
        vert_arr_copy.remove(v)
    
    res_arr.insert(0, temp_arr)
    
    if len(vert_arr_copy) == 0:  
        
        return res_arr
    
    else:
        
        res_arr = build_s_upper(vert_arr_copy, res_arr)
        
        return res_arr

def s_lower(vert_arr):
    
    res_arr = []
    
    vert_arr_copy = vert_arr.copy()
    
    res_arr = build_s_lower(vert_arr_copy, res_arr)
    
    return res_arr

def build_s_lower(vert_arr_copy, res_arr):

    temp_arr = []
    
    for v in vert_arr_copy:
        
        if v.count_connections_in_arr(vert_arr_copy) == 0:
            
            temp_arr.append(v)
                
    for v in temp_arr:
        
        vert_arr_copy.remove(v)
    
    res_arr.append(temp_arr)
    
    if len(vert_arr_copy) == 0: 
        
        return res_arr
    
    else:
        
        res_arr = build_s_lower(vert_arr_copy, res_arr)
        
        return res_arr
    
        