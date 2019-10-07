# load necessary modules ----
import numpy as np
import pandas as pd
import random
from custom_transformer import IsMissing
from sklearn.compose import ColumnTransformer
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier

# load necessary data ----

# load iris data set
iris = load_iris()

# load feature matrix
X = iris["data"]
# load target vector
y = iris["target"]

# standardize feature names spelling and casing
feature_names = [col.replace(" ", "_").replace("_(cm)", "") 
                 for col in (iris["feature_names"] + ["species"])]

# transform X and y into data frame
iris_df = pd.DataFrame(np.column_stack((X, y.reshape(-1, 1)))
                       , columns=feature_names)

# convert species from numeric to categorical
class_names = {0.0: "setosa", 1.0: "versicolor", 2.0: "virginica"}
iris_df["species"] = iris_df["species"].map(class_names)

# replace a few valid values with NaN values ----

# initialize random number generator
random.seed(2019)

# generate list of random integers 
random_ints = [random.randrange(0, len(iris_df)) for _ in range(20)]

# for these random index values, replace their real values with NaN
iris_df.loc[random_ints, "sepal_length"] = np.nan
iris_df.loc[random_ints, "sepal_width"] = np.nan

# manually force the first "sepal_width" value to also be NaN
iris_df.loc[0, "sepal_width"] = np.nan

# split iris_df into training and testing sets ----
X_train, X_test, y_train, y_test = train_test_split(iris_df.drop("species", 
                                                                 axis=1),
                                                    iris_df["species"],
                                                    test_size=0.3,
                                                    random_state=2019)

# create first pipeline ----
missing_mapper = Pipeline(steps=[
    ("missing_sl", IsMissing(col_name="sepal_length")),
    ("missing_sw", IsMissing(col_name="sepal_width"))
])

# create pipeline to impute missing values ----
impute_mapper = ColumnTransformer(
    transformers=[
        ("impute",
         SimpleImputer(missing_values=np.nan, strategy="median"),
         ['sepal_length', 'sepal_width'])
     ],
     remainder="passthrough")

# combine the two pieplines into one ----
data_prep_mapper = Pipeline(steps=[
    ("missing", missing_mapper),
    ("impute", impute_mapper)
])

# build decision tree classifier ----
dt_clf = DecisionTreeClassifier(random_state=2019,
                                min_samples_leaf=30,
                                criterion="gini",
                                min_samples_split=2)

# create final pipeline object that combines preprocessing with modeling ----
pipe = Pipeline(steps=[
    ("dataprep", data_prep_mapper),
    ("model", dt_clf)
])
