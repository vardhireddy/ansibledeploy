HIDE ?= @
VENV ?=env
PIP ?= $(VENV)/bin/pip

prepare-venv:
	$(HIDE)virtualenv $(VENV) --always-copy
	$(HIDE)$(VENV)/bin/easy_install pip==18.1
	$(HIDE)$(PIP) install -r requirements.txt

clean:
	rm -rf env

