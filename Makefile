VALIDATION_FILE=metadata_validation.yml
ONTOLOGY_FILE=ontology_validators.yml
TEMP_FILE=temp_file.yml
TEMP_FILE_2=temp_file2.yml
SAMPLE_SERVICE_SCHEMA = test_data/validator_schema.json
MACRO_SCHEMA = test_data/validator_macro_schema.json

test:
	python3 -c "import yaml, sys; yaml.safe_load(sys.stdin)" < sample_uploader_mappings.yml
	python3 scripts/validate_schemas.py $(SAMPLE_SERVICE_SCHEMA) $(VALIDATION_FILE)
	python3 scripts/validate_schemas.py $(MACRO_SCHEMA) validation_files/*yml
	python3 scripts/merge_validators.py $(TEMP_FILE) $(TEMP_FILE_2)
	python3 scripts/check_if_updated.py $(VALIDATION_FILE) $(TEMP_FILE)
	python3 scripts/check_if_updated.py $(ONTOLOGY_FILE) $(TEMP_FILE_2)
	rm $(TEMP_FILE)
	rm $(TEMP_FILE_2)

update:
	python3 scripts/merge_validators.py $(VALIDATION_FILE) $(ONTOLOGY_FILE)
	python3 scripts/create_tsv.py $(VALIDATION_FILE)
