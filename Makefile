.PHONY: test


test:
	python3 -c "import yaml, sys; yaml.safe_load(sys.stdin)" < sample_uploader_mappings.yml
	python3 validate_schemas.py

update:
	python3 merge_validators.py