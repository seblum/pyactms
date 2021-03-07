python setup.py bdist_wheel sdist

python3 -m twine upload dist/*

python3 -mtwine upload --skip-existing dist/*