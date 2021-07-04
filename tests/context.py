# -*- coding: utf-8 -*-

from os import path as ospath
from sys import path as syspath

import sample

syspath.insert(0, ospath.abspath(ospath.join(ospath.dirname(__file__), '..')))
