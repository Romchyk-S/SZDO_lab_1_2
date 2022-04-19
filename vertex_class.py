# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 13:06:53 2022

@author: romas
"""

class Vertex:
    
    index = 0
    
    
    def __init__(self, i, arr_out, arr_in):
        
        self.index = i
                
        self.connected_out = arr_out
        
        self.connected_in = arr_in
        
        self.connected_out_copy = arr_out
        
        self.connected_in_copy = arr_in
  
        
    def __repr__(self):
         
        return f"{self.index}"
    
    def connect_vertex(self, vert):
        
        self.connected_out.append(vert)
        
        vert.connected_in.append(self)
            
    def get_connections_out(self):
        
        return self.connected_out
    
    def get_connections_in(self):
        
        return self.connected_in
    
    def count_connections_in_arr(self, vert_arr):
        
        connections_arr = self.get_connections_in()
        
        count = 0
        
        for v in connections_arr:
            
            if v in vert_arr:
              
                count += 1
                
        return count
    
    def count_connections_out_arr(self, vert_arr):
        
        connections_arr = self.get_connections_out()
        
        count = 0
        
        for v in connections_arr:
            
            if v in vert_arr:
              
                count += 1
                
        return count
                
    
    def get_index(self):
        
        return self.index
    
    def check_already_connected(self, vert):
        
        if vert in self.get_connections_out():
            
            return True
        
        else:
            
            return False
    
    def check_backward_connection(self, vert):
        
        if vert in self.get_connections_in():
            
            return True
        
        else:
            
            return False
        
    def __lt__(self, other):
        
       return (self.index < other.index)
       