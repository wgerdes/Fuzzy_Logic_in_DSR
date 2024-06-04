Data preparation
    Create working hours feature --DONE
    Test out possible log transformable columns --DONE --> REMOVED AGAIN
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
python -m dso.run dso/config/config_logic.json --runs=8 --n_cores_task=8 --seed=42

Running on Snellius

Copy files from pc line by line (first copy them locally)
scp data/2m_train.csv wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/dso/task/regression/data
scp data/2m_test.csv wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/dso/task/regression/data

scp main/functions.py wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/dso
scp main/program.py wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/dso
scp main/regression.py wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/dso/task/regression/
scp main/config_logic.json wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/dso/config/

Login
ssh -X wgerdes@snellius.surf.nl
passw = key

Run:
source $HOME/venv3/bin/activate
cd $HOME/deep-symbolic-optimization/dso
srun -u --time=50:00:00 --mem-per-cpu=4096 python -m dso.run dso/config/config_logic.json --runs=20 --n_cores_task=20 --seed=42

Copy log from server:
scp -r wgerdes@snellius.surf.nl:deep-symbolic-optimization/dso/log/dso_task_regression_data_train_df_2024-06-03-212707 /Users/wout/Documents/UvA/Thesis/

Evaluate expression: (alter test set in expression script)
python main/evaluate_expression.py --equation "fuzzy_not(fuzzy_not(x1*fuzzy_and(fuzzy_and(x10, product_reichenbach(fuzzy_or(probabilistic_sum(x5, fuzzy_not(fuzzy_and(fuzzy_not(fuzzy_and(fuzzy_not(x9), x3)), x1))), x14), x14)), x13)))"