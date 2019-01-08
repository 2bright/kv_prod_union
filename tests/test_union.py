import pytest
import kv_prod_union as kv

def test_union_0_0():
  samples_1 = []
  samples_2 = []
  samples_expected = []
  samples = kv.union(samples_1, samples_2)
  assert samples == samples_expected

def test_union_0_2():
  samples_1 = []
  samples_2 = [{'k2':21}, {'k2':22}]
  samples_expected = [{'k2':21}, {'k2':22}]
  samples = kv.union(samples_1, samples_2)
  assert samples == samples_expected

def test_union_2_0():
  samples_1 = [{'k2':21}, {'k2':22}]
  samples_2 = []
  samples_expected = [{'k2':21}, {'k2':22}]
  samples = kv.union(samples_1, samples_2)
  assert samples == samples_expected

def test_union_2_2():
  samples_1 = [{'k1':11}, {'k1':12}]
  samples_2 = [{'k2':21}, {'k2':22}]
  samples_expected = [{'k1':11}, {'k1':12}, {'k2':21}, {'k2':22}]
  samples = kv.union(samples_1, samples_2)
  assert samples == samples_expected

