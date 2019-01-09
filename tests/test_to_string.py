import pytest
import kv_prod_union as kv

def test_include_key_False():
  sample = {
    'key1': True,
    'key2': 1,
    'key3': 0.2,
  }
  str_expected = 'True--1--0.2'
  str_result = kv.to_string(sample, None, False)
  assert str_result == str_expected

def test_key_alias_None():
  sample = {
    'key1': True,
    'key2': 1,
    'key3': 0.2,
  }
  str_expected = 'key1-True--key2-1--key3-0.2'
  str_result = kv.to_string(sample, None)
  assert str_result == str_expected

def test_key_alias():
  sample = {
    'key1': True,
    'key2': 1,
    'key3': 0.2,
  }
  str_expected = 'k1-True--k2-1--k3-0.2'
  key_alias = {
    'key1': 'k1',
    'key2': 'k2',
    'key3': 'k3',
  }
  str_result = kv.to_string(sample, key_alias)
  assert str_result == str_expected
