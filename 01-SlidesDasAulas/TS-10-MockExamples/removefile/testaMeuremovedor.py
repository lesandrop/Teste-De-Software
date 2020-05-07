#!/usr/bin/env python
# -*- coding: utf-8 -*-

from meuremovedor import remova
from unittest.mock import MagicMock
from unittest.mock import patch

import unittest

class RomovaTestCase(unittest.TestCase):
    
    @patch('meuremovedor.os.path')
    @patch('meuremovedor.os')
    def test_remova(self, meuremovedor_os, meuremovedor_path):
        # set up the mock
        meuremovedor_path.isfile = MagicMock(return_value=False)
        
        flag = remova("any path")

        #O arquivo não foi removido
        self.assertFalse(flag, "O arquivo a ser removido não existe")

        # Este assert ser false mostra que os.remove NÃO foi chamado
        self.assertFalse(meuremovedor_os.remove.called, "Failed to not remove the file if not present.")
        
        # make the file 'exist'
        meuremovedor_path.isfile = MagicMock(return_value=True)
        
        flag = remova("any path")

        #O arquivo foi removido
        self.assertTrue(flag, "O arquivo a ser removido existe")
              
        meuremovedor_os.remove.assert_called_with("any path")