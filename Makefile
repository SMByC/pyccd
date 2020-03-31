.PHONY: build tests deploy docs test-deploy clean profile

# LCMAP standardized Makefile targets.  Do not remove.

build:
	@pip install -e .[test,docs,deploy]
	@python setup.py sdist bdist_wheel

tests:
	@pytest

deploy:
	@twine upload --username $(TWINE_USERNAME) \
                      --password $(TWINE_PASSWORD) \
                      dist/*

docs:
	@python setup.py build_sphinx \
                         --source-dir sphinx \
                         --build-dir sphinx-docs 

# Extra Makefile targets.  Alter at will.

profile:
	kernprof -v -l pytest

test-deploy:
	@twine upload --username $(TWINE_USERNAME) \
                      --password $(TWINE_PASSWORD) \
                      --repository-url https://test.pypi.org/legacy/ \
                      dist/*

clean:
	@rm -rf build dist *egg-info* sphinx-docs;
	@find . -type d -name "*pycache*" -exec rm -rf {} \;
	@find . -type f -name "*~" -exec rm -rf {} \;
