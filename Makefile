.PHONY: clean fmt

# Adapted from: https://earthly.dev/blog/python-makefile/

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	rm -rf __pycache__
	rm -rf $(VENV)

fmt: $(VENV)/bin/activate
	$(PYTHON) -m black solutions/*.py
