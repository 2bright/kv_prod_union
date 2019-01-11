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

def compile(sampling_config):
  samples = []
  if not isinstance(sampling_config, list):
    sampling_config = [sampling_config]
  if len(sampling_config) > 1:
    for one_sampling_config in sampling_config:
      samples = union(samples, compile(one_sampling_config))
  elif len(sampling_config) == 1:
    one_sampling_config = sampling_config[0]
    if isinstance(one_sampling_config, list):
      samples = compile(one_sampling_config)
    elif isinstance(one_sampling_config, dict):
      if len(one_sampling_config) > 1:
        for k_tuple, v_list in one_sampling_config.items():
          samples = prod(samples, compile({k_tuple: v_list}))
      elif len(one_sampling_config) == 1:
        for k_tuple, v_list in one_sampling_config.items():
          if not isinstance(k_tuple, tuple):
            k_tuple = (k_tuple,)
          if not isinstance(v_list, list):
            v_list = [v_list]
          if len(v_list) > 1:
            for v_tuple in v_list:
              samples = union(samples, compile({k_tuple:v_tuple}))
          elif len(v_list) == 1:
            v_tuple = v_list[0]
            if not isinstance(v_tuple, tuple):
              v_tuple = (v_tuple,)
            if len(v_tuple) == 3 and v_tuple[1] == '::':
              sub_sampling_config = v_tuple[2]
              v_tuple = v_tuple[0]
              samples = union(samples, prod(compile({k_tuple:v_tuple}), compile(sub_sampling_config)))
            elif len(v_tuple) == len(k_tuple):
              if len(k_tuple) > 1:
                for i in range(len(k_tuple)):
                  samples = prod(samples, compile({k_tuple[i]:v_tuple[i]}))
              elif len(k_tuple) == 1:
                samples = union(samples, [{k_tuple[0]:v_tuple[0]}])
            else:
              raise ValueError('value tuple format error.')
    else:
      raise ValueError('format error.')
  return samples

def to_string(sample, key_alias = {}, include_key = True):
  sample_in_str = ''
  for k in sorted(sample.keys()):
    v = sample[k]
    if include_key:
      if isinstance(key_alias, dict) and key_alias.get(k) is not None:
        sample_in_str += str(key_alias.get(k)) + '-'  + str(v) + '--'
      else:
        sample_in_str += str(k) + '-' + str(v) + '--'
    else:
      sample_in_str += str(v) + '--'
  return sample_in_str[:-2]

def from_string(sample_in_str, key_alias = {}, value_types = {}):
  key_alias_r = {v: k for k, v in key_alias.items()}
  sample = {}
  kv_list = sample_in_str.split('--')
  for kv in kv_list:
    k,v = (e for e in kv.split('-'))
    if key_alias_r.get(k) is not None:
      k = key_alias_r.get(k)
    if value_types.get(k) is not None:
      v = value_types.get(k)(v)
    sample[k] = v
  return sample
