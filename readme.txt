Questions
Computing possibilities / necessities
Determining fuzzyness of classes --> just do smth
Adding noise


ISSUES:
!!! USE REICHENBACH AS ROOT OPERATOR, WITH a TO LEFT SIDE AND b TO RIGHT SIDE
!!! ATTEMPTS TO INCORPORATE THIS:
Program.library.names.index('product_reichenbach')
Min constraint in --> BUT! Product reichenbach not ALWAYS in the traversal      
"relational" : {
         "targets" : ["product_reichenbach"],
         "effectors" : ["product_reichenbach", "add", "sub", "div", "mul"],
         "relationship" : "child",
         "on" : true
      },
      "repeat" : {
         "tokens" : "product_reichenbach",
         "min_" : 1,
         "max_" : 1,
         "on" : true
      },

ADDED min TO prior.py

OTHER ATTEMPTS:
In program.py --> seems like there is some sort of version check to create errors when it is not correct
- Adding directly to traversal creates ISSUES
- Adding directly to tokens creates ISSUES

!!!
Lukas / Reichenbach both get:
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/multiprocessing/reduction.py", line 51, in dumps
    cls(buf, protocol).dump(obj)
_pickle.PicklingError: Can't pickle lukas: attribute lookup lukas on __main__ 

Error originates from multiprocessing
!!!

Todo
Data preparation
    Create working hours feature --DONE
    Test out possible log transformable columns
    Why should we add noise? --Questions
    Check weekly / 24h lag to see if we need to transform -- IRRELEVANT
    python evaluate_expression.py --"sqrt(x2 + x3)*(-x5 + x7 + 18)" --0.7 --"train_df" 

DSR
    Incorporate Product (Reichenbach) and Lukasiewics into DSR framework (functions.py) -- DONE
    Added to functions.py as protected_product_reichenbach and product_reichenbach  -- DONE
    Both are set as UNARY operators with a complexity of 1 similar to multiplication -- DONE
    These new operators can now be chosen in the config file by incorporating them into the function set -- DONE
    Reichenbach can not be a child because it should be the root node -- DONE
    Reichenbach should always be included in the traversal / tokens -- TODO
        - Created min constraint in config file -- Reichenbach can not be duplicate but sometimes is not in traversal


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
cp main/prior.py deep-symbolic-optimization/dso/dso
cp main/program.py deep-symbolic-optimization/dso/dso

cd deep-symbolic-optimization/dso
python -m dso.run dso/config/config_logic.json