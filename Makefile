BASE_DIR=goblin

.PHONY: install
.PHONY: uninstall
install:
	pip install -U .
	
uninstall:
	pip uninstall .

.PHONY: test
test:
	./runtests.sh $(BASE_DIR)

migrations:
	django-admin.py make migrations --settings=goblin.test.settings_test

.PHONY: clean
clean:
	for f in $(shell find -iname '*.pyc'); do \
		rm -fr $$f; \
	done;
