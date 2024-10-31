import unittest
from collections import namedtuple
from nombres import *

class TestNombres(unittest.TestCase):

    def setUp(self):
        self.datos = [
            FrecuenciaNombre(2002, 'ALEJANDRO', 8020, 'Hombre')
            FrecuenciaNombre(2002, 'PABLO', 5799, 'Hombre')
            FrecuenciaNombre(2002, 'MARÍA', 6900, 'Mujer')
            FrecuenciaNombre(2003, 'ALEJANDRO', 7500, 'Hombre')
            FrecuenciaNombre(2003, 'PABLO', 6200, 'Hombre')
            FrecuenciaNombre(2003, 'MARÍA', 7000, 'Mujer')     
        ]