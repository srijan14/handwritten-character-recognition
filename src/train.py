import os
import argparse
from src.model import Model

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Training on the EMNIST dataset')
    parser.add_argument('--data', type=str, default='./data/emnist-byclass.mat', help="Trainnig data pickle file path")
    args = parser.parse_args()

    if not os.path.exists(args.data):
        print("Invalid training data path provided")
        exit()

    train_model = Model()
    train_model.load_data(args.data)
    train_model.character_model()
    train_model.train()
    train_model.test()