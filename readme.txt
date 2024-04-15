Questions
Computing possibilities / necessities
Determining fuzzyness of classes

Todo
Data preparation
    Create working hours feature  #
    Test out possible log transformable columns
    Why should we add noise?
    Check weekly / 24h lag to see if we need to transform

DSR
    Incorporate Product (Reichenbach) and Lukasiewics into DSR framework (functions.py) #
    Added to functions.py as protected_product_reichenbach and product_reichenbach
    Both are set as UNARY operators with a complexity of 1 similar to multiplication
    These new operators can now be chosen in the config file by incorporating them into the function set

Remarks

Setup:
Install Python 3.6

python3 -m venv venv3 # Create a Python 3 virtual environment
source venv3/bin/activate # Activate the virtual environment

Install pip
pip install numpy == 1.19

pip install --upgrade setuptools pip
export CFLAGS="-I $(python -c "import numpy; print(numpy.get_include())") $CFLAGS" # Needed on Mac to prevent fatal error: 'numpy/arrayobject.h' file not found
pip install -e ./dso # Install DSO package and core dependencies


Copy to DSO:
cp functions.py ./deep-symbolic-optimization/dso/dso
cp regression.py ./deep-symbolic-optimization/dso/dso/task/regression/
cp config_classification_paysim.json ./deep-symbolic-optimization/dso/dso/config/
cp train, val, test ./deep-symbolic-optimization/dso/dso/task/regression/data

Run:
cd ./code/deep-symbolic-optimization/dso
python -m dso.run dso/config/config_logic.json
