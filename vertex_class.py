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

        return self.count_connections(connections_arr, vert_arr)

    def count_connections_out_arr(self, vert_arr):

        connections_arr = self.get_connections_out()

        return self.count_connections(connections_arr, vert_arr)

    def count_connections(self, conn_arr, vert_arr):

        count = 0

        for v in conn_arr:

            if type(vert_arr[0]) == Vertex:

                if v in vert_arr:

                    count += 1

            else:

                i = 0

                while i < len(vert_arr):

                    if v in vert_arr[i]:

                        count += 1

                    i += 1

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

    def add_mark(self, num):

        self.mark = num

    def check_mark_exists(self):

        try:

            return True

        except AttributeError:

            return False

    def __lt__(self, other):

       return (self.index < other.index)
