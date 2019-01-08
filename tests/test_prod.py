import pytest
import kv_prod_union as kv

def test_prod_0_0():
  samples_1 = []
  samples_2 = []
  samples_expected = []
  samples = kv.prod(samples_1, samples_2)
  assert samples == samples_expected

def test_prod_0_2():
  samples_1 = []
  samples_2 = [{'k2':21}, {'k2':22}]
  samples_expected = [{'k2':21}, {'k2':22}]
  samples = kv.prod(samples_1, samples_2)
  assert samples == samples_expected

def test_prod_2_0():
  samples_1 = [{'k2':21}, {'k2':22}]
  samples_2 = []
  samples_expected = [{'k2':21}, {'k2':22}]
  samples = kv.prod(samples_1, samples_2)
  assert samples == samples_expected

def test_prod_2_2():
  samples_1 = [{'k1':11}, {'k1':12}]
  samples_2 = [{'k2':21}, {'k2':22}]
  samples_expected = [{'k1':11, 'k2':21}, {'k1':11, 'k2':22}, {'k1':12, 'k2':21}, {'k1':12, 'k2':22}]
  samples = kv.prod(samples_1, samples_2)
  assert samples == samples_expected

