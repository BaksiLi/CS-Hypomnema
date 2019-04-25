#!/usr/bin/env python
# -*- coding: utf-8 -*-

LIFO_list = list()
FIFO_list = list()


def LIFO_push(LIFO_list, x):
    LIFO_list.append(x)  # add x to the end


def LIFO_pop(LIFO_list):
    return LIFO_list.pop(-1)  # return the value removed if needed


def FIFO_push(FIFO_list, x):
    FIFO_list.append(x)


def FIFO_pop(FIFO_list):
    return FIFO_list.pop(0)


def DFS(maze_graph, initial_vertex):

    def add_to_explored_vertices(explored_vertices, vertex):
        explored_vertices.append(vertex)

    def is_explored(explored_vertices, vertex):
        return vertex in list(explored_vertices)

    # explored vertices list
    explored_vertices = list()
    queuing_structure = list()
    parent_dict = dict()

    # push the initial vertex to the queuing_structure
    LIFO_push(queuing_structure, (initial_vertex, None))
    while len(queuing_structure) > 0:
        (current_vertex, parent) = queuing_structure.pop()
        # if the current vertex is not explored
        if not is_explored(explored_vertices, current_vertex):
            # add current_vertex to explored vertices
            add_to_explored_vertices(explored_vertices, current_vertex)
            # use parent_dict to map the parent of the current verte
            parent_dict[current_vertex] = parent
            # for each neighbor of the current vertex in the maze graph:
            for neighbour in maze_graph[current_vertex]:
                # if neighbor is not explored:
                if not is_explored(explored_vertices, neighbour):
                    queuing_structure.append((neighbour, current_vertex))
    return explored_vertices, parent_dict


def BFS(maze_graph, initial_vertex, target_vertex = None) :
    
    # explored vertices list
    explored_vertices = list()
    
    #LIFO stack
    queuing_structure = list()
    
    #Parent Dictionary
    parent_dict = dict()
        

    FIFO_push(queuing_structure,(initial_vertex,None)) # push the initial vertex to the queuing_structure
    while len(queuing_structure) > 0: #   while queuing_structure is not empty:
        # current_vertex,parent = queuing_structure.pop()
        # if the current vertex is not explored
            # add current_vertex to explored vertices
            # use parent_dict to map the parent of the current vertex
            # for each neighbor of the current vertex in the maze graph:
                # if neighbor is not explored:
                    # push the tuple (neighbor,current_vertex) to the queuing_structure
        current_vertex,parent = FIFO_pop(queuing_structure)
        #
        # YOUR CODE HERE
        #
        if not is_explored(explored_vertices, current_vertex):
            add_to_explored_vertices(explored_vertices, current_vertex)
            parent_dict[current_vertex] = parent

            # Break the while loop if current vertex is target vertex
            if current_vertex == target_vertex:
                break

            for neighbor in maze_graph[current_vertex]:
                if not is_explored(explored_vertices, neighbor):
                    FIFO_push(queuing_structure,(neighbor,current_vertex))

    return explored_vertices,parent_dict 

def create_walk_from_parents(parent_dict,initial_vertex,target_vertex):
    list_walk = []
    n = target_vertex
    while n != initial_vertex:
        for i in parent_dict:  # keys
            if i == n:
                list_walk.append(n)
                n = parent_dict[i]
    return list_walk[::-1]BS
