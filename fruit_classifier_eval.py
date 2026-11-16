import numpy as np

probs = np.array([
    [0.7, 0.2, 0.1],
    [0.1, 0.6, 0.3],
    [0.2, 0.2, 0.6],
    [0.5, 0.3, 0.2],
    [0.1, 0.3, 0.6]
])
y_test = np.array([0, 1, 2, 1, 2])
y_pred = np.argmax(probs, axis=1)
accuracy = np.mean(y_pred == y_test)
w_true = np.array([150.0, 120.0, 200.0, 180.0])
w_pred = np.array([140.0, 130.0, 210.0, 170.0])
mse = np.mean((w_true - w_pred) ** 2)

print("Predicted:", y_pred)
print("Accuracy:", accuracy)
print("MSE:", mse) 

wrong_samples = np.where(y_pred != y_test)[0]

print("Wrongly predicted sample indices:", wrong_samples)
