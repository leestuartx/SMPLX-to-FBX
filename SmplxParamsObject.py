import numpy as np
import glob
import pickle
import os
import joblib

from typing import Dict
from typing import Tuple

from PathFilter import PathFilter

class SmplxParamsObject(object):
    def __init__(self, read_path):
        self.data = {}

        filename = read_path.split("/")[-1]
        with open(read_path, "rb") as fp:
            self.data = joblib.load(fp)
        print('good')
        #self.params = {"smpl_poses":data["smpl_poses"],
        #                        "smpl_trans":data["smpl_trans"] }

