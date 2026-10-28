import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error 
from sklearn.model_selection import cross_val_score


# file opening
housing = pd.read_csv("housing.csv")

housing["cat_income"] = pd.cut(housing["median_income"],
                               bins=[0,1.5,3.0,4.5,6.0,np.inf],
                               labels=[1,2,3,4,5])

# Creating Train and Test set for ML model
split = StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)

for train_index,train_index in split.split(housing,housing["cat_income"]):
    train_set = housing.loc[train_index].drop("cat_income",axis=1)
    test_set = housing.loc[train_index].drop("cat_income",axis=1)

df = train_set.copy()

# Creating Fratures and labels for traing the model
housing_features = df.drop("median_house_value",axis=1).copy()
housing_labels = df["median_house_value"].copy()

num_attributes = housing_features.drop("ocean_proximity",axis=1).columns.tolist()
cat_attributes = ["ocean_proximity"]

# Cleaning the num_attribute
num_pipeline = Pipeline([
    ("impute",SimpleImputer(strategy="median")),
    ("scaler",MinMaxScaler(feature_range=(-1,1)))
])

# Converting the cat_attributes to the numerical data
cat_pipeline = Pipeline([
    ("cat",OneHotEncoder(handle_unknown="ignore"))
])

# Creating full pipeline
full_pipeline = ColumnTransformer([
    ("num",num_pipeline,num_attributes),
    ("cat",cat_pipeline,cat_attributes)
])

housing = full_pipeline.fit_transform(housing_features)

print(housing.shape)

# Checking which model is perform well on the this dataset

# 1. linearregression
lin_re = LinearRegression()
lin_re.fit(housing,housing_labels)
lin_pred = lin_re.predict(housing)
lin_rmse = root_mean_squared_error(housing_labels,lin_pred)
lin_cros = -cross_val_score(lin_re,housing,housing_labels,scoring="neg_root_mean_squared_error",cv=10)
print(pd.Series(lin_cros).describe())

# 2. Decisontreeregressor
dec_re = DecisionTreeRegressor()
dec_re.fit(housing,housing_labels)
dec_pred = lin_re.predict(housing)
dec_rmse = root_mean_squared_error(housing_labels,dec_pred)
dec_cros = -cross_val_score(dec_re,housing,housing_labels,scoring="neg_root_mean_squared_error",cv=10)
print(pd.Series(dec_cros).describe())

# 3. Randomforestregressor
ran_re = RandomForestRegressor()
ran_re.fit(housing,housing_labels)
ran_pred = ran_re.predict(housing)
ran_rmse = root_mean_squared_error(housing_labels,dec_pred)
ran_cros = -cross_val_score(ran_re,housing,housing_labels,scoring="neg_root_mean_squared_error",cv=10)
print(pd.Series(ran_cros).describe())