#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import sd

from unittest.mock import patch    
from unittest.mock import MagicMock

class RomovaTestCase(unittest.TestCase):

    def test_umValor(self):
        indata = [0]
        outdata = sd.std_calc(indata)

        self.assertAlmostEqual(outdata,0)

    @patch('sd.mean.avg_calc')
    def test_valoresIguaisZero(self,mean_avg_calc):
      
        # set up the mock
        sd.mean.avg_calc = MagicMock(return_value=0)
        
        indata = [0,0,0]
        outdata = sd.std_calc(indata)

        self.assertAlmostEqual(outdata,0.0)

    @patch('sd.mean.avg_calc')
    def test_valoresIguais(self,mean_avg_calc):
      
        # set up the mock
        sd.mean.avg_calc = MagicMock(return_value=10.0)
        
        indata = [10,10,10]
        outdata = sd.std_calc(indata)

        self.assertAlmostEqual(outdata,0.0)

    @patch('sd.mean.avg_calc')
    def test_valorNegativo(self,mean_avg_calc):
      
        # set up the mock
        sd.mean.avg_calc = MagicMock(return_value=3.33)
        
        indata = [10,-10,10]
        outdata = sd.std_calc(indata)

        self.assertAlmostEqual(outdata,11.547,places=2)

    @patch('sd.mean.avg_calc')
    def test_valoresDiferentes(self,mean_avg_calc):
      
        # set up the mock
        sd.mean.avg_calc = MagicMock(return_value=3)
        
        indata = [5,4,3,2,1]
        outdata = sd.std_calc(indata)

        self.assertAlmostEqual(outdata,1.58,places=2)

    @patch('sd.mean.avg_calc')
    def test_doisValoresDiferentesMutante(self, mean_avg_calc):
        # set up the mock
        sd.mean.avg_calc = MagicMock(return_value=4)
        
        indata = [5,3]
        outdata = sd.std_calc(indata)

        #O arquivo não foi removido
        self.assertAlmostEqual(outdata,1.41,places=2)