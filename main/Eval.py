import pandas as pd
import numpy as np
from sklearn.metrics import log_loss, accuracy_score, precision_score, recall_score, f1_score
import re
from functions import *
from datetime import datetime

def equation(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, func):
    func = func.replace("sqrt", "np.sqrt")
    func = func.replace("exp", "np.exp")
    func = func.replace("log", "np.log")
    func = func.replace("sin", "np.sin")
    func = func.replace("cos", "np.cos")
    func = func.replace("product_s_implication", "product_s_implication")
    func = func.replace("product_r_implication", "product_r_implication")
    func = func.replace("product_norm", "product_norm")
    func = func.replace("product_conorm", "product_conorm")
    func = func.replace("lukasiewicz_s_implication", "lukasiewicz_s_implication")
    func = func.replace("lukasiewicz_r_implication", "lukasiewicz_r_implication")
    func = func.replace("lukasiewicz_norm", "lukasiewicz_norm")
    func = func.replace("lukasiewicz_conorm", "lukasiewicz_conorm")
    func = func.replace("godel_s_implication", "godel_s_implication")
    func = func.replace("godel_r_implication", "godel_r_implication")
    func = func.replace("godel_norm", "godel_norm")
    func = func.replace("godel_conorm", "godel_conorm")
    func = func.replace("fuzzy_and", "fuzzy_and")
    func = func.replace("fuzzy_or", "fuzzy_or")
    func = func.replace("fuzzy_not", "fuzzy_not")
    func = eval(func)
    return func

def replace_variable_names(equation, var_mapping):
    # Sort variable names by length in descending order to prevent partial replacements
    sorted_vars = sorted(var_mapping.keys(), key=len, reverse=True)
    for var in sorted_vars:
        equation = re.sub(r'\b' + re.escape(var) + r'\b', var_mapping[var], equation)
    return equation

def main():
    start_time = datetime.now()
    print(f"Script started at: {start_time}")

    threshold = 0.55

    # Create a dictionary mapping variable names to column names
    var_mapping = {
        'x1': 'oldbalanceOrig', 'x2': 'newbalanceOrig', 'x3': 'oldbalanceDest', 'x4': 'newbalanceDest', 
        'x5': 'is_workday', 'x6': 'meanDest3', 'x7': 'meanDest7', 'x8': 'maxDest3',
        'x9': 'maxDest7', 'x10': 'type_CASH_IN', 'x11': 'type_CASH_OUT', 'x12': 'type_DEBIT', 'x13': 'type_PAYMENT',
        'x14': 'type_TRANSFER'
    }

    results = []

    # Load the test dataset once
    data_filename = 'data/2m_test.csv'
    df = pd.read_csv(data_filename, header=None, names=list(var_mapping.values()) + ['y'])

    for seed in range(16):
        seed_start = datetime.now()
        print(f"Processing seed {seed} started at: {seed_start}")

        filename = f'Results/Lukasiewicz/dso_dso_task_regression_data_2m_train_{seed}_pf.csv'
        df_seed = pd.read_csv(filename)

        # Extract the expression and complexity
        for index, row in df_seed.iterrows():
            func = row['expression']
            complexity = row['complexity']

            # Replace variable names with column names in the equation
            readable_equation = replace_variable_names(func, var_mapping)

            df['eq'] = df.apply(lambda x: equation(
                x['oldbalanceOrig'], x['newbalanceOrig'], x['oldbalanceDest'], x['newbalanceDest'], x['is_workday'],
                x['meanDest3'], x['meanDest7'], x['maxDest3'], x['maxDest7'], x['type_CASH_IN'],
                x['type_CASH_OUT'], x['type_DEBIT'], x['type_PAYMENT'], x['type_TRANSFER'],
                func=func
            ), axis=1)

            df['sigmoid'] = df.apply(lambda x: 1 / (1 + np.exp(-x['eq'])), axis=1)
            df['pred'] = (df['sigmoid'] > threshold).astype(int)

            # Calculate performance scores
            logloss = log_loss(df['y'], df['pred'])
            accuracy = accuracy_score(df['y'], df['pred'])
            precision = precision_score(df['y'], df['pred'])
            recall = recall_score(df['y'], df['pred'])
            f1 = f1_score(df['y'], df['pred'])

            results.append({
                'Evaluated expression': readable_equation,
                'complexity': complexity,
                'seed': seed,
                'F1 score': f1,
                'accuracy': accuracy,
                'precision': precision,
                'recall': recall
            })

        seed_end = datetime.now()
        print(f"Processing seed {seed} ended at: {seed_end}, duration: {seed_end - seed_start}")


    results_df = pd.DataFrame(results)
    print(results_df)

    results_df.to_csv('Lukasiewic_summary.csv', index=False)

    end_time = datetime.now()
    print(f"Script ended at: {end_time}, total duration: {end_time - start_time}")


if __name__ == "__main__":
    main()
