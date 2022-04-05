pip uninstall -y ukbsearch
rm -rf build
rm -rf ./dist/*
python3 setup.py sdist bdist_wheel
pip install ./dist/ukbsearch-0.2.2-py3-none-any.whl
# twine upload dist/*
# ukbsearch -s age smoking
# ukbsearch -s age smoking -l and
# ukbsearch -s 'ag*' 'rep*' -l and 
# ukbsearch -s 'ag*' 'rep*' -l and -t udi
# ukbsearch -s 'ag*' 'rep*' -l and

# ukbsearch -s 'ag*' 'rep*' -l and -o test_data -t csv
# ukbsearch -s 'ag*' 'rep*' -l and -o test_data -t console udi csv
# ukbsearch -u ukb26086 20161-0.0 21003-1.0 20009-1.30 -d csv rdata -o test_data3
# ukbsearch -s age --savedata csv rdata --out test_data
# ukbsearch -i ../ukbsearchdata/ukbtest.tab
# ukbsearch -i ../ukbsearchdata/ukb26086.tab

# ukbsearch -u ukb26086 20161-0.0 21003-1.0 20009-1.30 -d csv rdata -o test_data3 -p ../ukbsearchdata
# ukbsearch -u ukbtest 23-0.0 42-2.0 41146-0.0 -d csv rdata -o test_data3 -p ../ukbsearchdata

# ukbsearch -u ukb39003 3536-0.0 3536-1.0 ukb26086 20161-0.0 -d csv rdata -o t01 -p ../ukbsearchdata

# ukbsearch -u ukb26086 20161-0.0 21003-1.0 20009-1.30 f.40005.21.0 f.40005.29.0 f.22152.0.0 f.22817.0.0 f.54.1.0 f.54.2.0 f.84.0.0 f.84.0.1 f.84.0.2 f.84.0.3 f.84.0.4 f.84.0.5 f.84.1.0 f.84.1.1 f.84.1.2 f.84.1.3 f.84.1.4 f.84.1.5 f.84.2.0 f.84.2.1 f.84.2.2 f.84.2.3 f.84.2.4 f.84.2.5 f.191.0.0 f.1239.0.0 f.1239.1.0 f.1239.2.0 f.1249.0.0 f.1249.1.0 f.1249.2.0 f.1269.0.0 f.1269.1.0 f.1269.2.0 f.1279.0.0 f.1279.1.0 f.1279.2.0 f.2644.0.0 f.2644.1.0 f.2644.2.0 f.2867.0.0 f.2867.1.0 f.2867.2.0 f.2877.0.0 f.2877.1.0 f.2877.2.0 f.2887.0.0 f.2887.1.0 f.2887.2.0 f.2897.0.0 f.2897.1.0 f.2897.2.0 f.3062.0.0 f.3062.0.1 f.3062.0.2 f.3062.1.0 f.3062.1.1 f.3062.1.2 f.3062.2.0 f.3062.2.1 f.3062.2.2 f.3063.0.0 f.3063.0.1 f.3063.0.2 f.3063.1.0 f.3063.1.1 f.3063.1.2 f.3063.2.0 f.3063.2.1 f.3063.2.2 f.3064.0.0 f.3064.0.1 f.3064.0.2 f.3064.1.0 f.3064.1.1 f.3064.1.2 f.3064.2.0 f.3064.2.1 f.3064.2.2 f.3090.0.0 f.3090.1.0 f.3090.2.0 f.3137.0.0 f.3137.1.0 f.3137.2.0 f.3159.0.0 f.3159.1.0 f.3159.2.0 f.3436.0.0 f.3436.1.0 f.3436.2.0 f.3456.0.0 f.3456.1.0 f.3456.2.0 f.3486.0.0 f.3486.1.0 f.3486.2.0 f.3786.0.0 f.3786.1.0 f.3786.2.0 f.3992.0.0 f.3992.1.0 f.3992.2.0 f.4022.0.0 f.4022.1.0 f.4022.2.0 f.6157.0.0 f.6157.0.1 f.6157.0.2 f.6157.0.3 f.6157.1.0 f.6157.1.1 f.6157.1.2 f.6157.1.3 f.6157.2.0 f.6157.2.1 f.6157.2.2 f.6157.2.3 f.6183.0.0 f.6183.1.0 f.6183.2.0 f.6194.0.0 f.6194.1.0 f.6194.2.0 f.10691.0.1 f.10691.0.2 f.10691.0.3 f.10691.0.4 f.10694.0.1 f.10694.0.2 f.10694.0.3 f.10694.0.4 f.10695.0.1 f.10695.0.2 f.10695.0.3 f.10695.0.4 f.12144.2.0 f.20001.0.0 -d csv rdata -o test_data4 -p ../ukbsearchdata