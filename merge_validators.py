import os
import yaml


def validator_key_format(key):
    return key

files = os.listdir('validation_files')
files = ['validation_files/' + f for f in files]

validators = {}
prefix_validators = {}


for f in files:
    with open(f) as f_in:
        origin_file = f.split('.')[0]
        data = yaml.load(f_in)
        # append all validators
        if data.get('validators'):
            for key, val in data['validators'].items():
                if validators.get(key):
                    # update static_mappings
                    if data['validators'][key].get('static_mappings'):
                        if validators[key].get('static_mappings'):
                            for sub_key, sub_val in data['validators'][key]['static_mappings'].items():
                                validators[key]['static_mappings'][sub_key] = sub_val
                        else:
                            validators[key]['static_mappings'] = data['validators'][key]['static_mappings']
                else:
                    validators[key] = val
        # append all 
        if data.get('prefix_validators'):
            for key, val in data['prefix_validators'].items():
                if prefix_validators.get(key):
                    # update static_mappings
                    if data['prefix_validators'][key].get('static_mappings'):
                        if prefix_validators[key].get('static_mappings'):
                            for sub_key, sub_val in data['prefix_validators'][key]['static_mappings'].items():
                                prefix_validators[key]['static_mappings'][sub_key] = sub_val
                        else:
                            prefix_validators[key]['static_mappings'] = data['prefix_validators'][key]['static_mappings']
                else:
                    prefix_validators[key] = val

v_keys = sorted(list(validators.keys()))
pv_keys = sorted(list(prefix_validators.keys()))

data = {}
if validators:
    data['validators'] = validators
if prefix_validators:
    data['prefix_validators'] = prefix_validators

with open('merged_validators.yml', 'w') as f:
    yaml.dump(data, f)

