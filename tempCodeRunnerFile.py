print('r2score',r2_score(y_test,y_pred))
print('mse',mean_squared_error(y_test,y_pred))
print("mae",mean_absolute_error(y_test,y_pred))

plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.xlabel("Actual Charges")
plt.ylabel("Predicted Charges")
plt.title("Actual vs Predicted Charges")
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color="red",
    linestyle="--"
)
plt.show()