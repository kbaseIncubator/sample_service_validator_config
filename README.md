This repo stores the metadata validator configuration for the [KBase Sample Service](https://github.com/kbaseIncubator/sample_service).

See that repo for more documentation on the configuration.

# Samples validation configurations

This repository is for configuration files for the validation functions of the SampleService and related applications, including the samples_uploader

## Metadata key field conventions
	- All fields are lower case
	- spaces are replaced with "_".

## Metadata validation
	the "key_metadata" field in each validator contains information about the field.
	all fields must contain a `display-name` field which should be used when a human-readable version of the field is necessary. A field `description` can be optionally provided with any clarifying information, including expected units.

## Tokens
	To update this repository you must have a kbase developer token. Put the dev token in a file called {env}_TOKEN where {env} is the environment where you'd like to update the sample service (ci, appdev, narrative).
