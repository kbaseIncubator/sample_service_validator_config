import os
import sys
import yaml


def validator_key_format(key):
    return key

# only argument should be output_file name

if len(sys.argv) != 2:
    raise RuntimeError(f'Please provide output file path as sole argument to merge_validators.py')
output_file = sys.argv[1]

if not output_file.endswith('.yml') and not output_file.endswith('.yaml') :
    output_file = output_file + '.yml'

files = os.listdir('validation_files')
files = ['validation_files/' + f for f in files]

validators = {}
prefix_validators = {}


for f in files:
    with open(f) as f_in:
        origin_file = f.split('.')[0]
        data = yaml.load(f_in, Loader=yaml.SafeLoader)
        for val_type, val_data in [('validators', validators), ('prefix_validators', prefix_validators)]:
            if data.get(val_type):
                for key, val in data[val_type].items():
                    if val_data.get(key):
                        # update auxilliary fields
                        for data_field in ['static_mappings', 'key_metadata']:
                            if data[val_type][key].get(data_field):
                                if val_data[key].get(data_field):
                                    for sub_key, sub_val in data[val_type][key][data_field].items():
                                        val_data[key][data_field][sub_key] = sub_val
                                else:
                                    val_data[key][data_field][sub_key] = data[val_type][key][data_field]
                    else:
                        val_data[key] = val

v_keys = sorted(list(validators.keys()))
pv_keys = sorted(list(prefix_validators.keys()))

data = {}
if validators:
    data['validators'] = validators
if prefix_validators:
    data['prefix_validators'] = prefix_validators

with open(output_file, 'w') as f:
    yaml.dump(data, f)

print(f"    Validators merged, written to {output_file}")
