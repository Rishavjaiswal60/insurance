from data import load_dataset
from sklearn.model_selection import train_test_split


def preprocess_data():
    df=load_dataset()

    x_train,x_test,y_train,y_test=train_test_split(df.drop(['charges'],axis=1),df['charges'],test_size=0.2,random_state=42)
    return x_train,x_test,y_train,y_test