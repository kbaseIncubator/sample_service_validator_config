import yaml
from jsonschema import validate

_META_VAL_JSONSCHEMA = {
    'type': 'object',
    'definitions': {
        'validator_set': {
            'type': 'object',
            # validate values only
            'additionalProperties': {
                'type': 'object',
                'properties': {
                    'key_metadata': {
                        'type': 'object',
                        'additionalProperties': {
                            'type': ['number', 'boolean', 'string', 'null']
                        }
                    },
                    'validators': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'module': {'type': 'string'},
                                'callable_builder': {'type': 'string'},
                                'parameters': {'type': 'object'}
                            },
                            'additionalProperties': False,
                            'required': ['module', 'callable_builder']
                        }

                    }
                },
                'required': ['validators']
            }
        },
        'additionalProperties': False,
    },
    'properties': {
        'validators': {'$ref': '#/definitions/validator_set'},
        'prefix_validators': {'$ref': '#/definitions/validator_set'},
    },
    'additionalProperties': False
}
with open("metadata_validation.yml") as f:
    cfg = yaml.safe_load(f)
validate(instance=cfg, schema=_META_VAL_JSONSCHEMA)
