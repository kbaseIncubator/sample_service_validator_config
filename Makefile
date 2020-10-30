.PHONY: test

VALIDATION_FILE=merged_validators.yml

test:
	python3 -c "import yaml, sys; yaml.safe_load(sys.stdin)" < sample_uploader_mappings.yml
	python3 scripts/validate_schemas.py

update:

	python3 scripts/merge_validators.py $(VALIDATION_FILE)
	python3 scripts/create_tsv.py $(VALIDATION_FILE)