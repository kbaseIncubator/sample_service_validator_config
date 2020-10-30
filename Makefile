VALIDATION_FILE=merged_validators.yml
TEMP_FILE=temp_file.yml

test:
	python3 -c "import yaml, sys; yaml.safe_load(sys.stdin)" < sample_uploader_mappings.yml
	python3 scripts/validate_schemas.py $(VALIDATION_FILE)
	python3 scripts/merge_validators.py $(TEMP_FILE)
	python3 scripts/check_if_updated.py $(VALIDATION_FILE) $(TEMP_FILE)
	rm $(TEMP_FILE)

update:
	python3 scripts/merge_validators.py $(VALIDATION_FILE)
	python3 scripts/create_tsv.py $(VALIDATION_FILE)
