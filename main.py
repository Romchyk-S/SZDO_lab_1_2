# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:43:09 2022

@author: romas
"""


import graph as g

import S_algorithms as s

import tree as t



print()

quantity = int(input("Введіть кількість вершин графу: "))

print()


vert_arr, connections = g.build_graph(quantity)

g.show_graph(connections)


res_arr = s.s_upper(vert_arr)

print("Упорядкування S верхнє:")

print(res_arr)

print()


res_arr = s.s_lower(vert_arr)

print("Упорядкування S нижнє:")

print(res_arr)

print()



levels = int(input("Введіть кількість рівнів дерева: "))

print()

t.build_tree(levels)