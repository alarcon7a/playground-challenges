from exercise import multiply_numbers
from importlib import reload, import_module
import shutil

def reload_module(name):
  module = import_module(name)
  shutil.rmtree("__pycache__", ignore_errors=True)
  reload(module)
  return module

def test_numbers():
    reload_module('exercise')
    tests_list = [1, 2, 3]
    rta = multiply_numbers(tests_list)
    assert rta == [2, 4, 6]

def test_negative_numbers():
    reload_module('exercise')
    tests_list = [0, -1, 2]
    rta = multiply_numbers(tests_list)
    assert rta == [0, -2, 4]

def test_empty_list():
    reload_module('exercise')
    tests_list = []
    rta = multiply_numbers(tests_list)
    assert rta == []