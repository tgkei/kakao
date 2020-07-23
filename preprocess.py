import fire
import numpy as np
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
from scipy.sparse import *
from collections import Counter
import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
TRAIN_DATA = DATA_DIR/"train.json"
VAL_DATA = DATA_DIR/"val.json"

org_train = pd.read_json("data/train.json")
org_val = pd.read_json("data/val.json")

class Preprocess:
    TAG_OR_SONG={
        "tag" : 0,
        "song" : 1
    }

    def __calc_portion_x(cols,x):
        all_cols = []
        for col in cols:
            all_cols += col
            
        cols_cnt = dict(Counter(all_cols))
        
        cols_cnt_list = sorted(cols_cnt.items(), key=lambda t: -t[1])
        
        x_cnt = sum(x[1] for x in cols_cnt_list[:x])
        total = sum(x[1] for x in cols_cnt_list)
        return x_cnt/total

    def __count_col(data):
        tmp = dict()
        ret = 0

        for row in (data):
            for song in row:
                if song not in tmp:
                    tmp[song] = 0
                    ret +=1 
        return ret

    def json_to_csr(song_col):
        
    # def check_portion(self, column: str, portion:float = 1.0):
    #     print("Reading data...\n")
    #     playlists = load_json(TRAIN_DATA)
    #     print(f"Total playlists: {len(playlists)}")

    #     print("Calculating...")
    #     if TAG_OR_SONG[column]:
    #         self.col = raw_train.tags.tolist()
    #     else:
    #         self.col = raw_train.songs.tolist()
    #     
    #     print("Number of {}% for column : {}".format(total_num = __count_col(col)))

if __name__ == "__main__":
    f
