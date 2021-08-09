import json
import unittest
import pathlib as pt
from Weekly_assignment_1 import write_json as wr
json_string = None

class TestCase(unittest.TestCase):
	def TestUserName(self):
		self.assertTrue(wr(),'vipul')

class TestCase(unittest.TestCase):
	def test_json_file(self):
		path = pt.Path('output.json')
		self.assertTrue(path.is_file())
unittest.main()

