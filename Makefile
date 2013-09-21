lint:

	~/.local/bin/pylint --output-format=parseable fec/version/v*

all:
	python e_filing_headers_all_versions.py
