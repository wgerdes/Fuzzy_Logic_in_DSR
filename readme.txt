TODO
Adding noise
Fix pickle ISSUES
Fix server ISSUES
    
!!! ISSUES
Lukas / Reichenbach both get:
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/multiprocessing/reduction.py", line 51, in dumps
    cls(buf, protocol).dump(obj)
_pickle.PicklingError: Can't pickle produch_reichenbach: produch_reichenbach lookup product_reichenbach on __main__ 

Error originates from multiprocessing, not when just using 1 core
!!!


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

Data preparation
    Create working hours feature --DONE
    Test out possible log transformable columns --DONE
    Why should we add noise? --Questions
    Fuzzyfying columns --DONE
        Fuzzy clustering --TODO

DSR
    Incorporate Product (Reichenbach) and Lukasiewics into DSR framework (functions.py) -- DONE
    Added to functions.py as protected_product_reichenbach and product_reichenbach  -- DONE
    Both are set as UNARY operators with a complexity of 1 similar to multiplication -- DONE
    These new operators can now be chosen in the config file by incorporating them into the function set -- DONE
    Reichenbach can not be a child because it should be the root node --DONE
    Reichenbach should always be included in the traversal / tokens --DONE
    Enable multiprocessing with logical formula --TODO

Data evaluate_expression  
    Create script to gather performance from formula and create understandable formula --DONE

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

Evaluate expressions
python main/evaluate_expression.py --equation "product_reichenbach(x2, -x10 + x21 - x3)"

Copy to DSO:
cd ..
cd ..
cp main/functions.py deep-symbolic-optimization/dso/dso
cp main/program.py deep-symbolic-optimization/dso/dso
cp main/regression.py deep-symbolic-optimization/dso/dso/task/regression/
cp main/config_logic.json deep-symbolic-optimization/dso/dso/config/

cd deep-symbolic-optimization/dso
python -m dso.run dso/config/config_logic.json --runs=4 --n_cores_task=4 --seed=42

!TO SNELLIUS
Login
ssh -X wgerdes@snellius.surf.nl

passw = key


Copy files from pc line by line (first copy them locally)

scp deep-symbolic-optimization/dso/dso/task/regression/data/train_df.csv wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/dso/task/regression/data

scp data/train_df.csv wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/dso/task/regression/data

scp main/functions.py wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/dso
scp main/program.py wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/dso
scp main/regression.py wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/dso/task/regression/
scp main/config_logic.json wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/dso/config/

Run
source $HOME/venv3/bin/activate
cd $HOME/deep-symbolic-optimization/dso
srun python -m dso.run dso/config/config_logic.json

srun python -m dso.run dso/config/config_regression.json --b Nguyen-7