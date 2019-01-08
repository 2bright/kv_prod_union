import pytest
import kv_prod_union as kv

def test_compile_1():
  sampling_config = {
    'k1': True,
    'k2': [1, 2],
    'k3': [3, 4],
  }
  samples_expected = [
    {'k1': True, 'k2': 1, 'k3': 3},
    {'k1': True, 'k2': 1, 'k3': 4},
    {'k1': True, 'k2': 2, 'k3': 3},
    {'k1': True, 'k2': 2, 'k3': 4},
  ]
  samples = kv.compile(sampling_config)
  assert samples == samples_expected

def test_compile_2():
  sampling_config = {
    'k1': [1, (2, {'k2':[3,4]})],
    'k3': [5, 6],
  }
  samples_expected = [
    {'k1': 1, 'k3': 5},
    {'k1': 1, 'k3': 6},
    {'k1': 2, 'k2': 3, 'k3': 5},
    {'k1': 2, 'k2': 3, 'k3': 6},
    {'k1': 2, 'k2': 4, 'k3': 5},
    {'k1': 2, 'k2': 4, 'k3': 6},
  ]
  samples = kv.compile(sampling_config)
  assert samples == samples_expected

def test_compile_3():
  sampling_config = {
    ('k1', 'k2'): [([1, 2], [3, 4]), (5, [6, 7]), (8, 9)]
  }
  samples_expected = [
    {'k1': 1, 'k2': 3},
    {'k1': 1, 'k2': 4},
    {'k1': 2, 'k2': 3},
    {'k1': 2, 'k2': 4},
    {'k1': 5, 'k2': 6},
    {'k1': 5, 'k2': 7},
    {'k1': 8, 'k2': 9},
  ]
  samples = kv.compile(sampling_config)
  assert samples == samples_expected

def test_compile_4():
  sampling_config = {
    ('k1', 'k2'): [(1, [2, 3], {'k3':4}), (2, [2, 3], {'k3':5}), (5, 6)]
  }
  samples_expected = [
    {'k1': 1, 'k2': 2, 'k3': 4},
    {'k1': 1, 'k2': 3, 'k3': 4},
    {'k1': 2, 'k2': 2, 'k3': 5},
    {'k1': 2, 'k2': 3, 'k3': 5},
    {'k1': 5, 'k2': 6},
  ]
  samples = kv.compile(sampling_config)
  assert samples == samples_expected

def test_compile_5():
  sampling_config = {
    ('k1', 'k2'): [(1, [2, 3], {('k3', 'k4'):[(4, [6, 7])]}), (8, 9)]
  }
  samples_expected = [
    {'k1': 1, 'k2': 2, 'k3': 4, 'k4': 6},
    {'k1': 1, 'k2': 2, 'k3': 4, 'k4': 7},
    {'k1': 1, 'k2': 3, 'k3': 4, 'k4': 6},
    {'k1': 1, 'k2': 3, 'k3': 4, 'k4': 7},
    {'k1': 8, 'k2': 9},
  ]
  samples = kv.compile(sampling_config)
  assert samples == samples_expected

def test_compile_6():
  sampling_config = {
    ('k1', 'k2'):
    [
      (1, [2, 3], {
       ('k3', 'k4'): ([4, (5, {'k5':10})], [6, 7])
      }),
      (8, 9)
    ]
  }
  samples_expected = [
    {'k1': 1, 'k2': 2, 'k3': 4, 'k4': 6},
    {'k1': 1, 'k2': 2, 'k3': 4, 'k4': 7},
    {'k1': 1, 'k2': 2, 'k3': 5, 'k4': 6, 'k5':10},
    {'k1': 1, 'k2': 2, 'k3': 5, 'k4': 7, 'k5':10},
    {'k1': 1, 'k2': 3, 'k3': 4, 'k4': 6},
    {'k1': 1, 'k2': 3, 'k3': 4, 'k4': 7},
    {'k1': 1, 'k2': 3, 'k3': 5, 'k4': 6, 'k5':10},
    {'k1': 1, 'k2': 3, 'k3': 5, 'k4': 7, 'k5':10},
    {'k1': 8, 'k2': 9},
  ]
  samples = kv.compile(sampling_config)
  assert samples == samples_expected
