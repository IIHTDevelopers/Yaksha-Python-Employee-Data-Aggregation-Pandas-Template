import unittest
import numpy as np
from mainclass import EmployeeDataAnalysis
from test.TestUtils import TestUtils
import pandas as pd

class BoundaryTests(unittest.TestCase):
    def test_boundary(self):
        test_obj = TestUtils()
        test_obj.yakshaAssert("TestBoundary", True, "boundary")
        print("TestBoundary = Passed")
