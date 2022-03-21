pip uninstall -y ukbsearch
rm -rf build
rm -rf ./dist/*
python3 setup.py sdist bdist_wheel
pip install ./dist/ukbsearch-0.0.1-py3-none-any.whl
# twine upload dist/*
ukbsearch -s age smoking
ukbsearch -s age smoking -l and
ukbsearch -s 'ag*' 'rep*' -l and 
ukbsearch -s 'ag*' 'rep*' -l and -t udi
# ukbsearch -s 'ag*' 'rep*' -l and
ukbsearch -u ukb39003 3536-0.0 3536-1.0 3536-2.0 -d csv -o test_data