"""
Functions used to clean train and test data set
"""
import numpy as np
import pandas as pd
import random
from typing import List, Optional
from sklearn.base import BaseEstimator
from sklearn.compose import ColumnTransformer
from sklearn.datasets import load_iris
from sklearn.metrics.classification import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier


def is_missing(x: float) -> int:
    """Identifies if an element is missing
    Args:
        - x (float): element from a series
    Returns:
        int: 1 if the element is missing; 0 otherwise
    """
    if np.isnan(x):
        return 1
    else:
        return 0
    
 

def make_missing_flags(df: pd.DataFrame, col_names: List[str]) -> pd.DataFrame:
    """Create a new column that flags which elements are missing
    Args:
        - df: train/test data frame
        - col_names: column name
    Returns:
        Data frame with the newly added missing flag columns
    """
    for col_name in col_names:
        df[f"{col_name}_missing"] = df[f"{col_name}"].apply(is_missing)
        
    return df
    
  
def impute_missing_values(df: pd.DataFrame, imp: SimpleImputer) -> pd.DataFrame:
    """Impute missing values with the median for a data frame
    Args:
        - df:  a data frame
        - imp: a SimpleImputer object
    Returns:
        Data frame with imputed values for those that were missing
    """
    imputed_df = pd.DataFrame(data=imp.transform(df),
                              columns=df.columns,
                              index=df.index)
    return imputed_df


class IsMissing(BaseEstimator):
    """Creates a new column flagging if any values from one column are missing
    
    Note: this class will be used inside a scikit-learn Pipeline
    
    Attributes:
        col_name (str): name of a column
        
    Methods:
        _is_missing(): returns 1 if record contains NaN value; 0 if else
        
        fit(): fit all the transformers one after the other 
               then fit the transformed data using the final estimator
               
        transform(): apply transformers, and transform with the final estimator
    """
    
    def __init__(self, col_name):
        self.col_name = col_name
    
    
    def fit(self, X, y=None):
        return self
    
    
    def _is_missing(self, X):
        """Flag if a record has a NaN value"""
        if pd.isna(X):
            return 1
        else:
            return 0
    
    
    def transform(self, X, y=None):
        """Copies X and creates a new column before returning X_new"""
        new_col = self.col_name + "_missing"
        X_new = X.copy()
        X_new[new_col] = X_new[self.col_name].apply(self._is_missing)
        return X_new
    
 