test:
	./run_tests.sh

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	find ./test_data -name 'output.json' -delete
