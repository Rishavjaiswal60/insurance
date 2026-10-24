from column_trasformation import build_pipeline
import pandas as pd
from split import preprocess_data
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
import matplotlib.pyplot as plt
import pickle

pipe=build_pipeline()
x_train,x_test,y_train,y_test=preprocess_data()
pipe.fit(x_train,y_train)

y_pred=pipe.predict(x_test)
# print('r2score',r2_score(y_test,y_pred))
# print('mse',mean_squared_error(y_test,y_pred))
# print("mae",mean_absolute_error(y_test,y_pred))

# plt.figure(figsize=(6,6))
# plt.scatter(y_test, y_pred, alpha=0.6)
# plt.xlabel("Actual Charges")
# plt.ylabel("Predicted Charges")
# plt.title("Actual vs Predicted Charges")
# plt.plot(
#     [y_test.min(), y_test.max()],
#     [y_test.min(), y_test.max()],
#     color="red",
#     linestyle="--"
# )
# plt.show()

# df=pd.DataFrame(
#     {
#         'actual':y_test,
#         'predicted':y_pred
#     }
# )
# print(df.head(5))
""" to check overfitting"""
print(pipe.score(x_train, y_train))
print(pipe.score(x_test, y_test))

"""to save the model"""

with open('model.pkl','wb') as file:
    pickle.dump(pipe,file)

print('model saved successfully')

