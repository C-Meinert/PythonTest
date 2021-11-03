import numpy as np

msg = "Hello World"
print(msg)

# returns a value between 0-2
def smape1(actual, forecast):
    return 1/len(actual) * np.sum(2 * np.abs(forecast - actual)/(np.abs(actual) + np.abs(forecast)))

# returns a value between 0-1
def smape2(actual, forecast):
    return 1/len(actual) * np.sum(np.abs(forecast - actual)/(np.abs(actual) + np.abs(forecast)))

actual = np.array([100])
forecast = np.array([110])

# smape1 will be twice the value of smape2 because of the range of values
print(smape1(actual,forecast)) # 0.0952 
print(smape2(actual,forecast)) # 0.0476
