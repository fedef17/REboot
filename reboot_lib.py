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


####################################################################

############     REboot classes library    ########################

####################################################################

## General notes: a map is definitely needed at a certain point. Urbanistics, in the sense of the city architecture, is key for that -> in this sense it is better to consider multiple production/welfare units of a fixed dimension, than having very big units for big cities.

####################################################################

################### Infrastructure
inames = dict()
inames['logistics'] = 'road train metro bike_lane city_pavement'.split() # I'd separate ideally the intra and extra-city logistics
inames['tools'] = 'agriculture extraction industry medicine'.split()
inames['buildings'] = 'building forniture heating hydraulics electricity'.split()
inames['energy'] = 'solar_panels wind_mill hydro_power ff_splill ff_pipes'.split() ## ff = fossil fuel
inames['urban_env'] = 'parks trees'.split()

itypes = 'logistics tools buildings energy urban_env'.split()

class Infrastructure(object):
    """
    General class for the Infrastructure.
    """

    def __init__(self, iname = None, itype = None):
        self.iname = iname
        self.itype = itype

        return

    def build(self, amount = None):
        """
        Produces a given amount of the infrastructure. Returns the work needed to produce it. Also, the time is fundamental here, but can't be dealt with in the stationary case..
        """

        return work_needed#, time_needed

    def link_to_unit(self):
        """
        The infrastructure is linked to a ProdUnit/WelfUnit.
        """
        pass

################### Welfare units
wnames = dict()
wnames['education'] = 'school1 school2 university research practice'.split()
wnames['health'] = 'nurse doctor psychologist ...'.split()
wnames['social_services'] = 'transport social_assistance administration'.split()
wnames['environment'] = 'cleaning waste_dsp protection'.split()
wnames['distribution'] = 'food resources production'.split() ### The goods produced are distributed by distribution Welfare Units. The capitalist supermarket is here. But no such thing in our world.

wtypes = 'education health social_services environment distribution'.split()

class WelfUnit(object):
    """
    General class for a Welfare Unit.
    """

    def __init__(self, wname = None, wtype = None):
        self.wname = wname
        self.wtype = wtype

        return

    def assist(self, n_pips, infrastructure = None):
        """
        Produce a given amount of wname for a number of pips. Calculates the necessary work. As for the resources, the work generally depends on the infrastructure. Not only, the infrastructure also sets the maximum number of pips that can be assisted (e.g. hospital beds).

        In this way, this function makes sense only for health and education. Maybe also for social_services and distribution: in this sense all pips need the services, while it is only a part of the community for health and education. The environment welfare class might have a different function.

        A simpler way to do this in first instance is to set average necessary numbers for a given population. Of course the number might increase in special situations, like a new pandemic, but it is simpler to always look at the number in function of the total population and its age distribution (e.g. education (mainly) interests the younger population, while health is probably a more complex function, with heavier weights for the elder).
        """

        return work_needed

    def assign_pips(self):
        pass


################### Production units
# oppure, alternativa: estrazione, processamento. per molte cose ci sono questi due stadi. poi processamento può partire anche da prodotti di altri processamenti.

pnames = dict()
pnames['food'] = 'crop meat water fish ...'.split()
pnames['construction'] = 'logistic building energy_infra'.split()
pnames['industry'] = 'forniture clothing machines chemistry stuff ...'.split() # Also non-essential production, for example for the free time (sports, other) might appear here. A LOT OF STUFF has to appear here. This is probably the most difficult section to cathegorize.

pnames['extraction'] = 'material fuel'.split()
pnames['immaterial'] = 'research writing art'.split() # generally immaterial production. This is actually heavily linked to welfare.. can this be seen in terms of production? This would be good for applied research (i.e. solve some problem), but how for pure research or arts? Difficult to estimate a needed amount: the more, the better.

ptypes = 'food construction industry extraction immaterial'.split()


################### Production objects. This is the material effect of production, and represents the goods produced. The category of the goods are the same that for production.
class Good(object):
    """
    General class for Goods produced by a Production Unit. Goods can be summed, stored, moved, ecc. They are created by a ProdUnit.
    """

    def __init__(self, amount, pname = None, ptype = None):
        self.pname = pname
        self.ptype = ptype
        self.amount = amount

        return

    def assign_to_distribution_unit(self, amount):
        """
        Produce a given amount of pname. Calculates the necessary work to produce amount. As for the resources, the work generally depends on the infrastructure.
        """

        return work_needed#, time_needed

    def consume(self):
        """
        Goods are of different types. Food is consumed shortly after being distributed: this action destroys the good object, maybe producing a given amount of waste? Which is also a good in this sense. Other goods, like the infrastructure goods, are thought to last a lot more, but they also consume on a different timescale, or become obsolete in some cases.

        This gives a sense to the time axis :)
        """

        # Remove from list of available goods in the community.
        pass



class ProdUnit(object):
    """
    General class for a Production Unit.
    """

    def __init__(self, pname = None, ptype = None):
        self.pname = pname
        self.ptype = ptype

        return

    def produce(self, amount, infrastructure = None):
        """
        Produce a given amount of pname. Calculates the necessary work to produce amount. As for the resources, the work generally depends on the infrastructure.
        """

        # Adds the corresponding good to the list of goods available in the community.

        return work_needed#, time_needed

    def assign_pips(self):
        pass

    def create_good(self):
        pass


################### Resources

rnames = dict()
rnames['renewable'] = 'field water sun wind sea forest'.split()
rnames['finite'] = 'material fuel'.split()

rtypes = 'renewable finite'.split()


class Resource(object):
    """
    General class for a natural resource. Parent class of Renewable and Finite resource classes.

    The resource has a cost in terms of work needed at a certain level of infrastructure, and gives an output also function of the actual level of infrastructure and of the work done. Example: a crop field of 1km2. If the agriculture is mostly hand-made, the infrastructure is low, but we need more work and probably will have less output (but better quality) than a completely automated crop field with fertilizers which need low work but high infrastructure level.
    """

    def __init__(self, rname = None, rtype = None, amount = None):
        self.rname = rname
        self.rtype = rtype
        self.amount = amount

        return

    def set_cost_function(self, work_cost = None, environmental_cost = None, output = None, infra_levels = None):
        """
        These is fixed for each resource type. The function relates output and environmental costs to the work done and infrastructure level.

        Future: costs may vary in function of the place. E.g. an oil spill in the Arctic vs in the desert vs deep in the ocean.

        Present: the functions are simply nested lists: infra_levels + environmental_cost -> work_cost, output
        not simple at all. Given an infra_level, we can choose among the desired env_cost, and set then the work..
        NO. For each (infra_level, env_cost) tuple we have a (work_cost, output) tuple. Env_cost might just be low/high, if for example we decide to reduce the impact on the environment or not.
        """

        # Sets this attribute, fun is a 2-argument function
        self.output_function = fun1
        self.envcost_function = fun2

        return

    def output(self, actual_work, actual_infra):
        """
        The actual output is a function of the work done and the infrastructure available.
        """
        output = self.output_function(actual_work, actual_infra)

        return output

    def environmental_cost(self, actual_work, actual_infra):
        """
        The environmental_cost is a function of the work done and the infrastructure available.
        This allows to decide whether to exploit or not a given resource. Not using a resource will give a positive outcome as a negative environmental cost (e.g. a field that turns to a forest, a cave to a mountain environment, ecc., the salt of the Earth).
        """
        env_cost = self.envcost_function(actual_work, actual_infra)

        return env_cost


class Renewable(Resource):
    """
    A renewable resource.
    """

    def __init__(self, rname = None, rtype = None, density = None, extension = None):
        self.rname = rname
        self.rtype = rtype
        self.density = density
        self.extension = extension

        return

class Finite(Resource):
    """
    A finite resource.
    """

    def __init__(self, rname = None, rtype = None, amount = None):
        self.rname = rname
        self.rtype = rtype
        self.amount = amount

        return



#####################################################################################

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

    def check_needs(self, time = 'year'):
        """
        This function checks all needs of the Community in a given time window. For the stationary case, we can assume 1 year as reference. Maybe also for the non-stationary case.
        """

        needs = dict()
        for prod in all_prods:
            needs[prod] = amount # this is done for all productions

        for welf in all_welf:
            needs[welf] = n_pips # number of needing pips. Is self.n_pips for some welfare units.
            # sarebbe più semplice se in un primo momento calcolassi tutti i bisogni di welfare come media sulla popolazione. Anche se mantenere un'impostazione basata sui needs permette più flessibilità ad esempio a livello dell'età della popolazione.

        return needs

    def check_happy(self):
        pass

    def assign_prod_units(self):
        pass

    def assign_welf_units(self):
        pass



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
