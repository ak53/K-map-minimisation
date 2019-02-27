import unittest
from HW2_2018014 import minFunc



class testpoint(unittest.TestCase):
	def test_minFunc(self):
		self.assertEqual(minFunc(4,"()d-"),"0")
		self.assertEqual(minFunc(4,"()d(0,5,6)"),"0")
		self.assertEqual(minFunc(4,"(0,1,2,4,5,6,8,9,12,13,14)d-"),"W'Z'+XZ'+Y'")
		self.assertIn(minFunc(4,"(1,3,7,11,15)d(0,2,5)"),"W'X'+YZ or W'Z+YZ")
		self.assertEqual(minFunc(4,'(0,1,3,7,8,9,11,15)d-'),"X'Y'+YZ")
		self.assertEqual(minFunc(4,"(0,4,5,7,8,11,12,15)d-"),"W'XZ+WYZ+Y'Z'")
		self.assertIn(minFunc(4,"(4,6,9,10,11,13)d(2,12,15)"),"W'XZ'+WX'Y+WZ or W'XZ'+WZ+X'YZ'") ##
		self.assertEqual(minFunc(4,"(6,7,8,9)d(10,11,12,13,14,15)"),"W+XY")
		self.assertEqual(minFunc(4,"(0,1,2,3,9,10)d(4,5,6)"),"W'X'+X'Y'Z+X'YZ'")
		self.assertEqual(minFunc(3,"(0,1,2,3,4,5,6,7)d-"),"1")
		self.assertEqual(minFunc(3,"(4,5,7)d-"),"WX'+WY")
		self.assertEqual(minFunc(3,"(0,1,3,5,7)d(4,6)"),"X'+Y")
		self.assertEqual(minFunc(3,"(2,3,4,5)d(6,7)"),"W+X")
		self.assertEqual(minFunc(2,"(0,1)d(2,3)"),"1")
		self.assertEqual(minFunc(2,"(0,1,2)d-"),"W'+X'")
		
                
if __name__=='__main__':
	unittest.main()
