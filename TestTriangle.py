# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    def testSideATrue(self):
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral','2,2,2 should be equilateral');
    def testSideAUnder(self):
        self.assertEqual(classifyTriangle(0,2,2),'InvalidInput','2,2,2 should be equilateral');
    def testSideAOver(self):
        self.assertEqual(classifyTriangle(202,2,2),'InvalidInput','2,2,2 should be equilateral');

    def testSideBTrue(self):
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral','2,2,2 should be equilateral');
    def testSideBUnder(self):
        self.assertEqual(classifyTriangle(2,0,2),'InvalidInput','2,0,2 should be equilateral');
    def testSideBOver(self):
        self.assertEqual(classifyTriangle(2,202,2),'InvalidInput','2,202,2 should be equilateral');

    def testSideCTrue(self):
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral','2,2,2 should be equilateral');
    def testSideCUnder(self):
        self.assertEqual(classifyTriangle(2,2,0),'InvalidInput','2,2,0 should be equilateral');
    def testSideCOver(self):
        self.assertEqual(classifyTriangle(2,2,202),'InvalidInput','2,2,202 should be equilateral');

    def testSideALong(self):
        self.assertEqual(classifyTriangle(2.34,2,2),'InvalidInput','2.34,2,2 should be isosceles');
    def testSideBLong(self):
        self.assertEqual(classifyTriangle(2,2.34,2),'InvalidInput','2,2.34,2 should be isosceles');
    def testSideCLong(self):
        self.assertEqual(classifyTriangle(2,2,2.34),'InvalidInput','2,2,2.34 should be isosceles');


    def testSideRelation(self):
        self.assertEqual(classifyTriangle(4,4,4),'Equilateral','This should be considered valid');


    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(3,5,4),'Right','5,3,4 is a Right triangle');
        
    def testIsoscelesTriangleC(self):
        self.assertEqual(classifyTriangle(21,21,23),'Isosceles','21,21,23 is an isosceles triangle');
    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(21,23,21),'Isosceles','21,23,21 is an isosceles triangle');
    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(23,21,21),'Isosceles','23,21,21 is an isosceles triangle');

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 is a scalene triangle');
    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(3,4,2),'Scalene','3,4,2 is a scalene triangle');
    def testScaleneTriangleC(self):
        self.assertEqual(classifyTriangle(4,2,3),'Scalene','4,2,3 is a scalene triangle');

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

