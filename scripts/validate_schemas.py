import sys
import yaml
from jsonschema import validate


if len(sys.argv) != 4:
    raise RuntimeError(f'Please provide validation file, json schema file, and environment as arguments to validate_schemas.py')
merged_file = sys.argv[1]
json_schema_file = sys.argv[2]
env = sys.argv[3]

with open(json_schema_file) as f:
    _META_VAL_JSONSCHEMA = yaml.safe_load(f)

# _META_VAL_JSONSCHEMA = {
#     'type': 'object',
#     'definitions': {
#         'validator_set': {
#             'type': 'object',
#             # validate values only
#             'additionalProperties': {
#                 'type': 'object',
#                 'properties': {
#                     'key_metadata': {
#                         'type': 'object',
#                         'additionalProperties': {
#                             'type': ['number', 'boolean', 'string', 'null']
#                         }
#                     },
#                     'validators': {
#                         'type': 'array',
#                         'items': {
#                             'type': 'object',
#                             'properties': {
#                                 'module': {'type': 'string'},
#                                 'callable_builder': {'type': 'string'},
#                                 'parameters': {'type': 'object'}
#                             },
#                             'additionalProperties': False,
#                             'required': ['module', 'callable_builder']
#                         }

#                     }
#                 },
#                 'required': ['validators']
#             }
#         },
#         'additionalProperties': False,
#     },
#     'properties': {
#         'validators': {'$ref': '#/definitions/validator_set'},
#         'prefix_validators': {'$ref': '#/definitions/validator_set'},
#     },
#     'additionalProperties': False
# }

files = [
    "validation_files/ENIGMA-noops.yml",
    "validation_files/SESAR-noops.yml",
    "validation_files/SESAR.yml",
    "validation_files/ENIGMA.yml",
    "validation_files/miscellaneous.yml",
    merged_file,
    f"{env}_metadata_validation.yml"
]

for file in files:
    with open(file) as f:
        cfg = yaml.safe_load(f)
    validate(instance=cfg, schema=_META_VAL_JSONSCHEMA)
