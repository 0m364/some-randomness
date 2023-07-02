import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Assuming you have a CSV file of your data
data = pd.read_csv('lottery_data.csv')

# Let's say 'factor1', 'factor2', etc. are the factors influencing the lottery draw
X = data[['factor1', 'factor2', 'factor3', 'factor4']]
y = data['lottery_number']

# Split the data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Apply linear regression
regressor = LinearRegression()  
regressor.fit(X_train, y_train)

# To predict on the test data
y_pred = regressor.predict(X_test)

# To see the difference between the actual value and predicted value
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)

# For statistical details
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
