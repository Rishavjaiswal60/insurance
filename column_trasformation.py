from data import load_dataset
from split import preprocess_data
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
# df=load_dataset()
model_train=preprocess_data()

def build_pipeline():

    trf=ColumnTransformer([
        (
        'categoical',OneHotEncoder(drop='first',sparse_output=False,handle_unknown='ignore'),['sex','smoker','region'] 
        )
    ],remainder='passthrough')
    poly=PolynomialFeatures(degree=2,include_bias=False)

    pipe=Pipeline(
        [
            ('trf',trf),
            ('poly',PolynomialFeatures(degree=2,include_bias=False)),
            ('model',LinearRegression())
        ]
    )

    return pipe


