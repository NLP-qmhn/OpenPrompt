# split train.tsv into train.tsv and valid.tsv
import os
import random
import argparse

def split_train_valid_test(data_dir, split_ratio=[0.8, 0.2], random_seed=42):
    random.seed(random_seed)
    
    train_file = os.path.join(data_dir, "train.tsv")
    valid_file = os.path.join(data_dir, "valid.tsv")
    
    with open(train_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    header = lines[0]
    lines = lines[1:]
        
    total = len(lines)
    train_num = int(total * split_ratio[0])
    
    lines = random.sample(lines, total)
    
    with open(train_file, "w", encoding="utf-8") as f:
        f.write(header)
        f.writelines(lines[:train_num])
        
    with open(valid_file, "w", encoding="utf-8") as f:
        f.write(header)
        f.writelines(lines[train_num:])
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, default="data", help="data directory")
    parser.add_argument("--split_ratio", type=float, nargs="+", default=[0.8, 0.2], help="split ratio of train and valid")
    parser.add_argument("--random_seed", type=int, default=42, help="random seed")
    args = parser.parse_args()
    split_train_valid_test(args.data_dir, args.split_ratio, args.random_seed)
    
if __name__ == "__main__":
    main()
    