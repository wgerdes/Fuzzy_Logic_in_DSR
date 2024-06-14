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

Copy files from pc to server
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
python main/evaluate_expression.py --equation "fuzzy_not(product_conorm(fuzzy_not(x14), product_conorm(product_conorm(product_conorm(product_s_implication(product_s_implication(x3, x4), product_s_implication(product_conorm(x14, x3), x3)), x9), x3), x2)))"