TODO
Adding noise

FB 30/04
Add noise
Fuzzy to correspond to percentiles
Try to release some constraints and test output
    
!!! USE LOGIC_FORMULA AS ROOT OPERATOR, WITH a TO LEFT SIDE AND b TO RIGHT SIDE --DONE
program.py --> lines 150 + 151 --> added token (18) to pos[0] in traversal --> which 
LINE108: program.py - from_tokens(tokens, skip_cache=False, on_policy=True, finish_tokens=True, add_logic = True):

LINE149 if add_logic:
LINE150   if 18 not in tokens:
LINE151     tokens[0] = 18

"relational" : {
         "targets" : ["LOGIC_FORMULA"],
         "effectors" : ["add", "sub", "div", "mul"], !!! ALL OTHER FUNCTIONS, DOES NOT HAVE TO INCLUDE LOGIC_FORMULA DUE TO MAX CONSTRAINT
         "relationship" : "child",
         "on" : true
      },
      "repeat" : { 
         "tokens" : "LOGIC_FORMULA",
         "min_" : null,
         "max_" : 1, 
         "on" : true
      },


!!! ISSUES
Lukas / Reichenbach both get:
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/multiprocessing/reduction.py", line 51, in dumps
    cls(buf, protocol).dump(obj)
_pickle.PicklingError: Can't pickle lukas: attribute lookup lukas on __main__ 

Error originates from multiprocessing, not when just using 1 core
!!!


Todo
Data preparation
    Create working hours feature --DONE
    Test out possible log transformable columns --DONE
    Why should we add noise? --Questions
    Check weekly / 24h lag to see if we need to transform --IRRELEVANT
    Fuzzyfying columns --DONE
        Currently just based on percentile
    Used columns:
        log_amount', 'step', 'oldbalanceOrig', 'newbalanceOrig',
       'oldbalanceDest', 'newbalanceDest', 'is_workday', 'meanDest3',
       'meanDest7', 'maxDest3', 'maxDest7', 'type_CASH_IN', 'type_CASH_OUT',
       'type_DEBIT', 'type_PAYMENT', 'type_TRANSFER', 'type2_CC', 'type2_CM',
       'isFraud'
    Fuzzified columns:
        'log_amount', 'oldbalanceOrig', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'is_workday', 'meanDest3', 'meanDest7', 'maxDest3', 'maxDest7'


DSR
    Incorporate Product (Reichenbach) and Lukasiewics into DSR framework (functions.py) -- DONE
    Added to functions.py as protected_product_reichenbach and product_reichenbach  -- DONE
    Both are set as UNARY operators with a complexity of 1 similar to multiplication -- DONE
    These new operators can now be chosen in the config file by incorporating them into the function set -- DONE
    Reichenbach can not be a child because it should be the root node --DONE
    Reichenbach should always be included in the traversal / tokens --DONE
    Enable multiprocessing with logical formula --TODO

Data evaluate_expression  
    Create script to gather performance from formula and create understandable formula --TODO

Tweakable parameters:
    Sigmoid treshold (config)
    Function set (config)
    poly token (config)
    training hyperparameters (config)
    policy optimizer parameters (config)
    prior parameters (config)

    mean / max dest rolling window (data prep)
    log transform (data prep)
    train/val/test split (data prep)
    under / oversampling (data prep)

    neural-guided GP meld (config) see https://github.com/dso-org/deep-symbolic-optimization

    policy optimizers
        risk seeking
        vanilla
        priority queue
        proximal policy
    


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
cp main/program.py deep-symbolic-optimization/dso/dso
cp main/regression.py deep-symbolic-optimization/dso/dso/task/regression/
cp main/config_logic.json deep-symbolic-optimization/dso/dso/config/

cd deep-symbolic-optimization/dso
python -m dso.run dso/config/config_logic.json --runs=1 --n_cores_task=4




python -m dso.run dso/config/config_logic.json