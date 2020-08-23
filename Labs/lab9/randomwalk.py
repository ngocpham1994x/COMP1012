#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
random.seed(10122019)
import numpy
import matplotlib.pyplot as plt

def random_walk_2D(np, ns):
    xpositions = numpy.zeros(np)
    ypositions = numpy.zeros(np)
    # extent of the axis in the plot:
    xymax = 3*numpy.sqrt(ns); xymin = -xymax

    NORTH = 1;  SOUTH = 2;  WEST = 3;  EAST = 4  # constants

    for step in range(ns):
        for i in range(np):
            direction = random.randint(1, 4)
            if direction == NORTH:
                ypositions[i] += 1
            elif direction == SOUTH:
                ypositions[i] -= 1
            elif direction == EAST:
                xpositions[i] += 1
            elif direction == WEST:
                xpositions[i] -= 1


    plt.plot(xpositions, ypositions, 'ko')
    plt.axis([xymin, xymax, xymin, xymax])
    plt.title('{particles} particles after {steps} steps'.format(particles=np, steps=ns))
    plt.savefig('tmp_{steps}.pdf'.format(steps=ns))
    
    return xpositions, ypositions



np        = 100  # number of particles
ns        = 100  # number of steps
x, y = random_walk_2D(np, ns)