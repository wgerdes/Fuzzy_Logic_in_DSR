Questions
Computing possibilities / necessities
Determining fuzzyness of classes
Adding 

Lukas / Reichenbach both get:
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/multiprocessing/reduction.py", line 51, in dumps
    cls(buf, protocol).dump(obj)
_pickle.PicklingError: Can't pickle lukas: attribute lookup lukas on __main__ 

Error occurs when:
We use protected Versions
We use different batch sizes
We use different amount of samples
!We use >1 core! Not yet occured with 1 core --> Error originates from multiprocessing

Todo
Data preparation
    Create working hours feature  #
    Test out possible log transformable columns
    Why should we add noise?
    Check weekly / 24h lag to see if we need to transform
    python evaluate_expression.py --"sqrt(x2 + x3)*(-x5 + x7 + 18)" --0.7 --"train_df"

DSR
    Incorporate Product (Reichenbach) and Lukasiewics into DSR framework (functions.py) #
    Added to functions.py as protected_product_reichenbach and product_reichenbach #
    Both are set as UNARY operators with a complexity of 1 similar to multiplication
    These new operators can now be chosen in the config file by incorporating them into the function set
    ! Make sure product reichenbach can only use single operators

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
cd ..
cd ..
cp main/functions.py deep-symbolic-optimization/dso/dso
cp main/regression.py deep-symbolic-optimization/dso/dso/task/regression/
cp main/config_logic.json deep-symbolic-optimization/dso/dso/config/

cd deep-symbolic-optimization/dso
python -m dso.run dso/config/config_logic.json