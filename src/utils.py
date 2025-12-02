# stores common fucntionalities that used across the project
import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import pickle
import dill

def save_object(file_path: str, obj: object) -> None:
    """
    Save an object to a file using dill.

    Args:
        file_path (str): The path to the file where the object will be saved.
        obj (object): The object to be saved.
    """
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)