import yaml


def validator_key_format(key):
    return key

files = [
    "ENIGMA.yml",
    "SESAR.yml",
    "SESAR-noops.yml",
    "miscellaneous.yml"
]
files = ["validation_files/" + f for f in files]
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
                    # collission!
                    continue
                    # validators[key] = val
                else:
                    validators[key] = val
        # append all 
        if data.get('prefix_validators'):
            for key, val in data['prefix_validators'].items():
                if prefix_validators.get(key):
                    # collission!
                    continue
                    # prefix_validators[key] = val
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


