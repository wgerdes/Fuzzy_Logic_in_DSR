import pandas as pd
import numpy as np
from sklearn.metrics import log_loss, accuracy_score, precision_score, recall_score, f1_score
import argparse
import time
from functions import *
import re


def equation(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, 
             x14, x15, func):
    
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
    for var, col_name in var_mapping.items():
        equation = equation.replace(var, col_name)
    return equation


def main(args):

    # print summary
    print('\n')
    print('equation: ', args.equation)
    print('threshold: ', args.threshold)
    print('dataset: ', args.dataset)

    # save results in file
    filename = "main/evaluation_output/evaluation_" + args.dataset + str(time.strftime("_%Y%m%d-%H%M%S.txt"))
    f = open(filename, "a")
    f.write('equation: ' + str(args.equation))
    f.write('\nthreshold: ' + str(args.threshold))
    f.write('\ndataset: ' + str(args.dataset))

    dataset = 'data/' + args.dataset + '.csv'
    threshold = args.threshold
    func = args.equation

    # Sort variable names by length in descending order to prevent partial replacements
    def replace_variable_names(equation, var_mapping):
        # Sort variable names by length in descending order to prevent partial replacements
        sorted_vars = sorted(var_mapping.keys(), key=len, reverse=True)
        for var in sorted_vars:
            equation = re.sub(r'\b' + re.escape(var) + r'\b', var_mapping[var], equation)
        return equation

    # Create a dictionary mapping variable names to column names

    #TODO: fix at the end
    var_mapping = {
        'x1': 'oldbalanceOrig', 'x2': 'newbalanceOrig', 'x3': 'oldbalanceDest', 'x4': 'newbalanceDest', 
        'x6': 'is_workday', 'x7': 'meanDest3', 'x8': 'meanDest7', 'x9': 'maxDest3',
        'x10': 'maxDest7', 'x11': 'type_CASH_IN', 'x12': 'type_CASH_OUT', 'x13': 'type_DEBIT', 'x14': 'type_PAYMENT',
        'x15': 'type_TRANSFER'
    }

    # Replace variable names with column names in the equation
    readable_equation = replace_variable_names(func, var_mapping)
    print('Evaluated equation: ', readable_equation)
    f.write('\nEvaluated equation: ' + readable_equation)
    
    # make predictions based on given equation
    df = pd.read_csv(dataset, header=None, names=['x1', 'x2', 'x3', 'x4', 'x5', 'x6',
                                                  'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 
                                                  'x13', 'x14', 'x15', 'y'])

    df['eq']=df.apply(lambda x: equation(x['x1'], x['x2'], x['x3'], x['x4'], x['x5'], 
                                         x['x6'], x['x7'], x['x8'], x['x9'], x['x10'], 
                                         x['x11'], x['x12'],x['x13'], x['x14'], x['x15'], func=func), axis=1)
    df['sigmoid']=df.apply(lambda x: 1 / (1 + np.exp(-x['eq'])), axis=1)
    df.loc[df['sigmoid'] <= threshold, 'pred'] = 0
    df.loc[df['sigmoid'] > threshold, 'pred'] = 1

    # calculate performance scores
    logloss = log_loss(df['y'], df['pred'])
    accuracy = accuracy_score(df['y'], df['pred'])
    precision = precision_score(df['y'], df['pred'])
    recall = recall_score(df['y'], df['pred'])
    f1 = f1_score(df['y'], df['pred'])

    # save and print performance scores
    f.write('\n')
    f.write('\nlog_loss = ' + str(logloss))
    f.write('\naccuracy = ' + str(accuracy))
    f.write('\nprecision_score = ' + str(precision))
    f.write('\nrecall_score = ' + str(recall))
    f.write('\nf1_score = ' + str(f1))

    print('\nlog_loss = ', logloss)
    print('accuracy = ', accuracy)
    print('precision_score = ', precision)
    print('recall_score = ', recall)
    print('f1_score = ', f1)

    f.close()


if __name__ == "__main__":

    # Instantiate the parser
    parser = argparse.ArgumentParser()

    # Required arguments
    parser.add_argument('--equation', type=str, default="sqrt(x17 + x20)*(-x14 + x2 + x23)",
                        help='string of equation, e.g. "sqrt(x17 + x20)*(-x14 + x2 + x23)"')

    parser.add_argument('--threshold', type=float, default=0.55,
                        help='sigmoid threshold between 0.0 and 1.0')

    parser.add_argument('--dataset', type=str, default="2m_test",
                        help='"train_df", "val_df", or "test_df"')

    args = parser.parse_args()

    if type(args.threshold) != float and type(args.threshold) != int:
        parser.error("threshold must have int or float value between 0 and 1")

    if args.threshold < 0 or args.threshold > 1:
        parser.error("threshold must have value between 0 and 1")
    
    # if args.dataset not in ["train_df", "val_df", "test_df"]:
    #     parser.error('Please enter "train_df", "val_df", or "test_df"')

    main(args)