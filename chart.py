import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('/home/poppie/Documents/my-todo/GBPJPY=X.csv')

# Convert the 'date' column to a datetime object
data['Date'] = pd.to_datetime(data['Date'])

# Sort the data by date
data = data.sort_values('Date')

# Plotting the graph
plt.plot(data['Date'], data['Open'], label='Open')
plt.plot(data['Date'], data['Close'], label='Close')
plt.plot(data['Date'], data['High'], label='High')
plt.plot(data['Date'], data['Low'], label='Low')

# Customize the graph
plt.title('Poppie')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

# Rotate the x-axis labels for better visibility
plt.xticks(rotation=45)

# Display the graph
plt.show()
