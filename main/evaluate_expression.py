import pandas as pd
import numpy as np
from sklearn.metrics import log_loss, accuracy_score, precision_score, recall_score, f1_score
import argparse
import time


def equation(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, 
             x14, x15,x16, x17, x18, x19, x20, x21, x22, x23, func):
    
    func = func.replace("sqrt", "np.sqrt")
    func = func.replace("exp", "np.exp")
    func = func.replace("log", "np.log")
    func = func.replace("sin", "np.sin")
    func = func.replace("cos", "np.cos")
    func = eval(func)

    return func


def main(args):

    # print summary
    print('\n')
    print('equation: ', args.equation)
    print('threshold: ', args.threshold)
    print('dataset: ', args.dataset)

    # save results in file
    filename = "./evaluation_output/evaluation_" + args.dataset + str(time.strftime("_%Y%m%d-%H%M%S.txt"))
    f = open(filename, "a")
    f.write('equation: ' + str(args.equation))
    f.write('\nthreshold: ' + str(args.threshold))
    f.write('\ndataset: ' + str(args.dataset))

    dataset = './code/deep-symbolic-optimization-master/dso/dso/task/regression/data/' + args.dataset + '.csv'
    threshold = args.threshold
    func = args.equation

    # make predictions based on given equation
    df = pd.read_csv(dataset, header=None, names=['x1', 'x2', 'x3', 'x4', 'x5', 'x6',
                                                  'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 
                                                  'x13', 'x14', 'x15', 'x16', 'x17', 'x18', 
                                                  'x19', 'x20', 'x21', 'x22', 'x23', 'y'])
    df['eq']=df.apply(lambda x: equation(x['x1'], x['x2'], x['x3'], x['x4'], x['x5'], 
                                         x['x6'], x['x7'], x['x8'], x['x9'], x['x10'], 
                                         x['x11'], x['x12'],x['x13'], x['x14'], x['x15'], 
                                         x['x16'], x['x17'], x['x18'], x['x19'], x['x20'], 
                                         x['x21'], x['x22'], x['x23'], func=func), axis=1)
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

    parser.add_argument('--threshold', type=float, default=0.7,
                        help='sigmoid threshold between 0.0 and 1.0')

    parser.add_argument('--dataset', type=str, default="val_df",
                        help='"train_df", "val_df", or "test_df"')

    args = parser.parse_args()

    if type(args.threshold) != float and type(args.threshold) != int:
        parser.error("threshold must have int or float value between 0 and 1")

    if args.threshold < 0 or args.threshold > 1:
        parser.error("threshold must have value between 0 and 1")
    
    if args.dataset not in ["train_df", "val_df", "test_df"]:
        parser.error('Please enter "train_df", "val_df", or "test_df"')

    main(args)
