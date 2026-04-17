REQ = requirements.txt

all: build

build: 
	@if [ ! -d .venv ] ; then python3 -m venv .venv ; fi

install: ${REQ}
	. .venv/bin/activate && pip install -r requirements.txt

norm: build
	. .venv/bin/activate && flake8 $$(find ex0* -name "*.py" ! -name "tester*")

clean:
	@rm -rf $$(find ex0* -type d -name __pycache__)
	@rm -rf $$(find ex0* -type f -name "tester*")
	@rm -rf .venv

freeze: 
	. .venv/bin/activate && pip freeze >| ${REQ}

.PHONY : all clean norm build