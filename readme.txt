TODO:
Final config settings
Complexity settings

Product
Lukasiewics
Godel
Combined

F1 vs F2
Which subset?

Constraints?
Root node (which subset)
Implications only have t-norm or conorm?

Compare against DSC on transformed dataset?

Data preparation
    Create working hours feature --DONE
    Test out possible log transformable columns --DONE --> 
    Add noise --DONE
    Fuzzyfying columns --DONE
    Fuzzy clustering --TODO

DSR
    Incorporate Product (Reichenbach) and Lukasiewics into DSR framework (functions.py) -- DONE
    Added to functions.py as protected_product_reichenbach and product_reichenbach  -- DONE
    Both are set as UNARY operators with a complexity of 1 similar to multiplication -- DONE
    These new operators can now be chosen in the config file by incorporating them into the function set -- DONE
    Reichenbach can not be a child because it should be the root node --DONE
    Reichenbach should always be included in the traversal / tokens --DONE

Data evaluate_expression  
    Create script to gather performance from formula and create understandable formula --DONE
    
Setup:
Install Python 3.6

python3 -m venv venv3 # Create a Python 3 virtual environment
source venv3/bin/activate # Activate the virtual environment

pip install --upgrade setuptools pip
pip install -e ./dso # Install DSO package and core dependencies

Running locally
Copy training data:
cp data/200k_train.csv deep-symbolic-optimization/dso/dso/task/regression/data
cp data/200k_test.csv deep-symbolic-optimization/dso/dso/task/regression/data

cd ..
cd ..
cp main/functions.py deep-symbolic-optimization/dso/dso
cp main/program.py deep-symbolic-optimization/dso/dso
cp main/regression.py deep-symbolic-optimization/dso/dso/task/regression/
cp main/config_logic.json deep-symbolic-optimization/dso/dso/config/

cd deep-symbolic-optimization/dso
python -m dso.run dso/config/config_logic.json --runs=1 --n_cores_task=1 --seed=42

Running on Snellius

Copy files from pc line by line (first copy them locally)
scp data/2m_train.csv wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/dso/task/regression/data
scp data/2m_test.csv wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/dso/task/regression/data

scp main/functions.py wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/dso
scp main/program.py wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/dso
scp main/regression.py wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/dso/task/regression/
scp main/config_logic.json wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/dso/config/

Login
ssh -Y wgerdes@snellius.surf.nl

Run:
source $HOME/venv3/bin/activate
cd $HOME/deep-symbolic-optimization/dso
nohup srun --time=72:00:00 --mem-per-cpu=4096 python -m dso.run dso/config/config_logic.json --runs=16 --n_cores_task=16 & disown

Copy log from server:   
scp -r wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/log/ /Users/wout/Documents/UvA/Thesis/

Evaluate expression: (alter test set in expression script)
python main/evaluate_expression.py --equation "lukasiewicz_norm(fuzzy_not(godel_conorm(godel_conorm(x6, product_norm(x3, x2)), x16)), x4)"