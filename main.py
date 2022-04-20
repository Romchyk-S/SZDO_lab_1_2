# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:43:09 2022

@author: romas
"""



import choosing_ordering as co


operation_chosen = 1


while operation_chosen == 1 or operation_chosen == 2:
    
    operation_chosen = int(input("Оберіть задачу (1 побудова упорядкувань для графу, 2 побудова впорядкування для дерева): "))
    
    if operation_chosen == 1:
        
        print()
    
        quantity = int(input("Введіть кількість вершин графу: "))
    
        print()
        
        s_upper, s_lower = co.graph_ordering(quantity)
        
        
        print("Упорядкування S верхнє:")
        
        print(s_upper)
        
        print()
        
        print("Упорядкування S нижнє:")
        
        print(s_lower)
        
        print()
    
    
    if operation_chosen == 2:
        
        levels = int(input("Введіть кількість рівнів дерева: "))
        
        # максимальна кількість породжених вершин?
        
        h = int(input("Введіть ширину впорядкування: "))
        
        print()
        
        tree_order = co.tree_ordering(levels, h)
        
        print(f"Упорядкування дерева ширини {h}:")
        
        print(tree_order)
        
print()
        
print("Дякуємо за роботу")