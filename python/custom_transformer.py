# load necessary modules ----
from sklearn.base import BaseEstimator
import pandas as pd


# create custom transformer class ----
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
        # create new column name
        new_col = self.col_name + "_missing"

        # make copy of X
        X_new = X.copy()

        # create new column whose value will flag if original value was NaN
        X_new[new_col] = X_new[self.col_name].apply(self._is_missing) 
        return X_new
