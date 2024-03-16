.PHONY: setup_venv virtualenv uninstall install_latest install_latest_pre install_latest_test install_latest_test_pre run_all help

PYTHON=python3

setup_venv:
	@echo "Setting up virtual environment..."
	@$(PYTHON) -m venv env
	@. env/bin/activate && $(PYTHON) -m pip install --upgrade pip wheel setuptools
	@. env/bin/activate && $(PYTHON) -m pip install -r requirements.txt
	@. env/bin/activate && $(PYTHON) -m pip -V
	@echo "Virtual environment is ready."

virtualenv:
	@if [ -d "env" ]; then \
		echo "Virtual environment already exists."; \
		read -p "Do you want to delete it and create a new one? [y/N] " answer; \
		case $$answer in \
			[Yy]* ) \
				echo "Deleting and recreating the virtual environment..."; \
				rm -rf env; \
				$(MAKE) setup_venv;; \
			* ) \
				echo "Using the existing virtual environment.";; \
		esac \
	else \
		$(MAKE) setup_venv; \
	fi

uninstall:
	@echo "Uninstalling pybgs package..."
	@. env/bin/activate && $(PYTHON) -m pip uninstall -y pybgs
	@echo "pybgs package uninstalled."

install_latest: uninstall
	@echo "Installing the latest release of pybgs..."
	@. env/bin/activate && $(PYTHON) -m pip install pybgs
	@echo "Latest release of pybgs installed."

install_latest_pre: uninstall
	@echo "Installing the latest pre-release of pybgs..."
	@. env/bin/activate && $(PYTHON) -m pip install --pre pybgs
	@echo "Latest pre-release of pybgs installed."

install_latest_test: uninstall
	@echo "Installing the latest release test version of pybgs from TestPyPI..."
	@. env/bin/activate && $(PYTHON) -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple pybgs
	@echo "Latest test release version of pybgs installed."

install_latest_test_pre: uninstall
	@echo "Installing the latest pre-release test version of pybgs from TestPyPI..."
	@. env/bin/activate && $(PYTHON) -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --pre pybgs
	@echo "Latest pre-release test version of pybgs installed."

run_all:
	@echo "Running all Python scripts..."
	@. env/bin/activate && for file in *.py; do \
		echo "Running $$file..."; \
		$(PYTHON) $$file; \
	done
	@echo "All Python scripts have been run."

help:
	@cat Makefile
