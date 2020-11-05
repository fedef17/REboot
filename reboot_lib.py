#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import sys
import os
import glob

from matplotlib import pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation
import seaborn as sns

from datetime import datetime
import pickle
from copy import deepcopy as dcopy

import random

####################################################################

############     SEM-pip classes library    ########################

####################################################################

class Community(object):
    """
    A community of pips. Ideally the smallest self-contained socio-economic entity.
    Defaults to 1000 pips.
    """

    def __init__(self, n_pips = 1000, location = 'countryside', resources = None, infrastructure = None):
        self.n_pips = n_pips
        self.location = location
        self.resources = resources
        self.infrastructure = infrastructure

        return

    def generate_pips(self, age_dist_function = age_dist_function):
        """
        Generates the pips, randomly picking among the age distribution. Optionally takes f=age_dist_function, f(n_pips) = list of ages.
        """

        self.pips_list = []

        ages = age_dist_function(self.n_pips)
        names = give_names(self.n_pips)
        for ag, na in zip(ages, names):
            print(na, ag)
            pip = Pip(name = na, age = ag, wishes = None, needs = None, happyness = None, skills = None)
            self.pips_list.append(pip)




class Pip(object):
    """
    A simple pip.
    """

    # All "properties" of a pip
    properties = 'name age wishes needs happyness skills'.split()

    def __init__(self, name = None, age = None, wishes = None, needs = None, happyness = None, skills = None):
        for nom, cos in zip(self.properties, [name, age, wishes, needs, happyness, skills]):
            setattr(self, nom, cos)

        return

    def description(self):
        print("Hi! I'm {}, nice to meet you :) I can tell you this:\n".format(self.name))
        for nom in self.properties[1:]:
            print('{}: {}\n'.format(nom, getattr(self, nom)))

        return

    def chenepensidelcovid(self):
        print('{}, che ne pensi del covid?\n'.format(self.name))
        print('DIOCAN che bale!\n')
        return

    def assign_to_prod_unit(self):
        pass

    def assign_to_welf_unit(self):
        pass

    def set_learning_mode(self):
        pass

    def set_production_mode(self):
        pass

    def check_happy(self):
        pass

    def check_needs(self):
        pass



########################################################################

# Define age weights for the population (here: italian population for 2020)
p_weights = []
for age in range(0, 101):
    if age < 20:
        p = 0.2/20
    elif 20 <= age <= 65:
        p = 0.57/46
    else:
        p = 0.46/34 - 0.46/35**2 * (age - 66)

    p_weights.append(p)

p_weights = np.array(p_weights)

pip_names = np.array(['Freddie', 'Joaquin', 'Gabriella', 'Leonia', 'Zona', 'Felicia', 'Preston', 'Vasiliki', 'Akiko', 'Shawn', 'Rosalia', 'Charlene', 'Joslyn', 'Jeanie', 'Jamila', 'Torie', 'Genna', 'Shaquana', 'Marisol', 'Shellie', 'Nery', 'Celia', 'Melanie', 'Eva', 'Angelica', 'Lorri', 'Cierra', 'Yanira', 'Solomon', 'Kimberli', 'Maegan', 'Kisha', 'Deeanna', 'Young', 'Gaylene', 'Donn', 'Delphia', 'Brenna', 'Porter', 'Frederick', 'Claudette', 'Garret', 'Moon', 'Callie', 'Asuncion', 'Gay', 'Dwight', 'Olga', 'Yevette', 'Earlean', 'Reid', 'Buffy', 'Gaylene', 'Chelsie', 'Carole', 'Pinkie', 'Corrina', 'Yolanda', 'Britni', 'Sierra', 'Jolanda', 'Annemarie', 'Season', 'Aimee', 'Easter', 'Shannan', 'Roosevelt', 'Merlene', 'Gail', 'Keitha', 'Jess', 'Anamaria', 'Lilliam', 'Lucile', 'Beverley', 'Raphael', 'Veronique', 'Daron', 'Chi', 'Phylis', 'Joya', 'Elicia', 'Jeramy', 'Dwana', 'Daniela', 'Myrtle', 'Alfreda', 'Viviana', 'Makeda', 'Dave', 'Kurtis', 'Tommy', 'Glynda', 'Sarina', 'Lenora', 'Keli', 'Broderick', 'Ali', 'Eduardo', 'Marylouise'])

def age_dist_function(num_pips, p_weights = p_weights):
    rand_ages = random.choices(np.arange(101), weights=p_weights, k = num_pips)
    rand_ages.sort()

    # age_groups = []
    # for yy in np.arange(101):
    #     age_groups.append(np.sum(rand_ages == yy))

    return rand_ages#, age_groups

def give_names(num_pips, pip_names = pip_names):
    rand_noms = random.choices(np.arange(100), k = num_pips)
    nomi = pip_names[rand_noms]

    return nomi
