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

import reboot_lib as rbl

####################################################################

############     Stupid main program    ########################

####################################################################
wishlist = ['mare', 'lasagna']
needslist = ['casa', 'bicicletta']
skilllist = ['ho studiato cose', 'sollevo tu babbo', 'so cucinà']

gigi = rbl.Pip(name = 'Gigi', age = '27', wishes = wishlist, needs = needslist, happyness = 8, skills = skilllist)

gigi.description()
gigi.chenepensidelcovid()
