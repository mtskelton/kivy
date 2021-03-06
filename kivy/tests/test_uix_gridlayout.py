'''
uix.gridlayout tests
========================
'''

import unittest

from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class UixGridLayoutTest(unittest.TestCase):
    
    def test_gridlayout_get_max_widgets_cols_rows_None(self):
        gl = GridLayout()
        expected = None
        value = gl.get_max_widgets()
        self.assertEqual(expected, value)
        
    def test_gridlayout_get_max_widgets_rows_None(self):
        gl = GridLayout()
        gl.cols = 1
        expected = None
        value = gl.get_max_widgets()
        self.assertEqual(expected, value)
        
    def test_gridlayout_get_max_widgets_cols_None(self):
        gl = GridLayout()
        gl.rows = 1
        expected = None
        value = gl.get_max_widgets()
        self.assertEqual(expected, value)
        
    def test_gridlayout_get_max_widgets_with_rows_cols(self):
        gl = GridLayout()
        gl.rows = 5
        gl.cols = 3
        expected = 15
        value = gl.get_max_widgets()
        self.assertEqual(expected, value)
        
        
        # wgts = [Widget() for i in range(4)]
        # for wgt in wgts:
            # gl.add_widget(wgt)
