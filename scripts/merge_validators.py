import os
import sys
import yaml


def validator_key_format(key):
    return key

# only argument should be output_file name

if len(sys.argv) < 3:
    raise RuntimeError(f'Please provide both output file and ontology file paths as arguments to merge_validators.py')
if len(sys.argv) > 3:
    raise RuntimeError(f"Too many arguments for merge_validators.py")

output_file = sys.argv[1]
ontology_file = sys.argv[2]

if not output_file.endswith('.yml') and not output_file.endswith('.yaml'):
    output_file = output_file + '.yml'

if not ontology_file.endswith('.yml') and not ontology_file.endswith('.yaml'):
    ontology_file = ontology_file + '.yml'


files = os.listdir('validation_files')
files = ['validation_files/' + f for f in files]

validators = {}
prefix_validators = {}
 
ontology_validators = {}

for f in files:
    with open(f) as f_in:
        origin_file = f.split('.')[0]
        data = yaml.load(f_in, Loader=yaml.SafeLoader)
        for val_type, val_data in [('validators', validators), ('prefix_validators', prefix_validators)]:
            if data.get(val_type):
                for key, val in data[val_type].items():
                    if data[val_type][key].get('validators'):
                        for validator in data[val_type][key]['validators']:
                            if validator['callable_builder'] == 'ontology_has_ancestor':
                                ontology_validators[key] = val

                    if val_data.get(key):
                        # update auxilliary fields and not the 'validators'
                        for data_field in ['static_mappings', 'key_metadata']:
                            if data[val_type][key].get(data_field):
                                if val_data[key].get(data_field):
                                    for sub_key, sub_val in data[val_type][key][data_field].items():
                                        val_data[key][data_field][sub_key] = sub_val
                                else:
                                    val_data[key][data_field] = data[val_type][key][data_field]
                    else:
                        val_data[key] = val

v_keys = sorted(list(validators.keys()))
pv_keys = sorted(list(prefix_validators.keys()))

data = {}
if validators:
    data['validators'] = validators
if prefix_validators:
    data['prefix_validators'] = prefix_validators

# try default_style with quotes here.
with open(output_file, 'w') as f:
    yaml.dump(data, f)  #, default_style='"')

# save ontology_file
with open(ontology_file, 'w') as f:
    yaml.dump(ontology_validators, f)  # , default_stype='"')

print(f"    Validators merged, written to {output_file}")
