class V():
  '''escape value if dict or list or tuple
  '''
  value = None
  def __init__(self, value):
    self.value = value

def prod(samples_1, samples_2):
  samples = []
  if len(samples_1) == 0:
    return samples_2
  if len(samples_2) == 0:
    return samples_1
  for s1 in samples_1:
    for s2 in samples_2:
      samples.append(dict(list(s1.items()) + list(s2.items())))
  return samples

def union(samples_1, samples_2):
  return samples_1 + samples_2

def prod_union(sampling_config):
  if not isinstance(sampling_config, dict):
    raise TypeError('sampling_config must be type of dict')
  samples = []
  if len(sampling_config) > 1:
    for k_tuple, v_list in sampling_config.items():
      samples = prod(samples, prod_union({k_tuple: v_list}))
  elif len(sampling_config) == 1:
    for k_tuple, v_list in sampling_config.items():
      if not isinstance(k_tuple, tuple):
        k_tuple = (k_tuple,)
      if not isinstance(v_list, list):
        v_list = [v_list]
      if len(v_list) > 1:
        for v_tuple in v_list:
          samples = union(samples, prod_union({k_tuple:v_tuple}))
      elif len(v_list) == 1:
        v_tuple = v_list[0]
        if not isinstance(v_tuple, tuple):
          v_tuple = (v_tuple,)
        if len(v_tuple) == len(k_tuple) + 1:
          sub_sampling_config = v_tuple[-1]
          v_tuple = v_tuple[:-1]
          samples = union(samples, prod(prod_union({k_tuple:v_tuple}), prod_union(sub_sampling_config)))
        elif len(v_tuple) == len(k_tuple):
          if len(k_tuple) > 1:
            for i in range(len(k_tuple)):
              samples = prod(samples, prod_union({k_tuple[i]:v_tuple[i]}))
          elif len(k_tuple) == 1:
            samples = union(samples, [{k_tuple[0]:v_tuple[0]}])
        else:
          raise ValueError('value tuple should has the same length as key tuple.')
  return samples

def compile(sampling_config):
  return prod_union(sampling_config)

def param_sample_to_string(sample, key_alias = {}, include_key = True):
  sample_in_str = ''
  for k in sorted(sample.keys()):
    v = sample[k]
    if isinstance(v, V):
      v = v.value
    if include_key:
      if isinstance(key_alias, dict) and key_alias.get(k) is not None:
        sample_in_str += str(key_alias.get(k)) + '-'  + str(v) + '--'
      else:
        sample_in_str += str(k) + '-' + str(v) + '--'
    else:
      sample_in_str += str(v) + '--'
  return sample_in_str[:-2]
