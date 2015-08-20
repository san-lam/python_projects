# Plotting the Rise of Computers
# For this lesson, we have specifically downloaded the historical stock data of Microsoft, Inc. and Apple Computer, Inc. 
# from the dates they each went public (which are March 13, 1986 and December 12, 1980, respectively) to July 1, 2015.

# Let's first read both datasets into Pandas DataFrame objects and take a quick look at Microsoft's stock.
import pandas

apple_stock = pandas.read_csv("AAPL_historical_stock.csv")
microsoft_stock = pandas.read_csv("MSFT_historical_stock.csv")

# First 10 rows of Microsoft Stock data
microsoft_stock.head(10)

# 2: Columns
# Yahoo! Finance gave us the following fields of information for each day:
# Open - the price the stock opened at
# High - the highest price the stock hit
# Low - the lowest price the stock dropped to
# Close - the final price the stock settled at
# Volume - the trading volume, or amount of stock traded
# Adj Close - the adjusted Close price
# To easily slice and filter these dates and timestamps, we need to specify using Pandas that we want the Date column to be treated as a datetime64 data type.
# The datetime64 data type, or dtype, is highly optimized for querying and interacting with dates like the ones we have in both datasets.
# Let's use Pandas to convert the Date columns of both DataFrame objects to datetime64 dtypes, using the Pandas' to_datetime() function,
# and then print the dtypes of both DataFrame objects to confirm.
# Using pandas.to_datetime() to convert both datasets' Date columns
microsoft_stock['Date'] = pandas.to_datetime(microsoft_stock['Date'])
apple_stock['Date'] = pandas.to_datetime(apple_stock['Date'])

# Use .dtypes and filter to info on ['Date'] column
microsoft_date_datatype = microsoft_stock.dtypes['Date']
apple_date_datatype = apple_stock.dtypes['Date']

print("Microsoft Date Datatype:  " + str(microsoft_date_datatype))
print("Apple Date Datatype:  " + str(apple_date_datatype))

# Plotting Columns
# We will learn about a library called Matplotlib, which makes it easy to plot all kinds of graphs just by specifying the data we want visualized.
# Let's first plot the full time series of the closing stock prices.
# Importing the pyplot sub-library from matplotlib library and referring to it as "plt"
import matplotlib.pyplot as plt

# plt.plot() tells Python to create a new plot and what the X (first argument) and Y (second argument) axes are
plt.plot(microsoft_stock['Date'], microsoft_stock['Close'])
# plt.title() details how we want the current plot to be titled
plt.title("Microsoft: Historical Closing Stock Price Until Jul 1, 2015")
# plt.show() reveals the plot we've been specifying
plt.show()

# New plot, repeat for Apple as we did with Microsoft
plt.plot(apple_stock['Date'], apple_stock['Close'])
plt.title("Apple: Historical Closing Stock Price Until Jul 1, 2015")
plt.show()

# 5: Trading Volume
# Let's now visualize the historical time series of the trading volume for both companies.
# The trading volume is measured by the number of shares that were exchanged in trades made that day.
# Plotting trading volumes for the respective stocks helps us identify rare and important events in the market or in the company,
# because investors will be more likely to buy or sell shares at that time.
# Here we use "color=___" to specify color
plt.plot(microsoft_stock['Date'], microsoft_stock['Volume'], color="blue")
plt.title("Microsoft: Trading Volume")
plt.show()

# Repeat for Apple!
plt.plot(apple_stock['Date'], apple_stock['Volume'], color="green")
plt.title("Apple: Trading Volume")
plt.show()

# Filtering and Plotting
# Let's now take advantage of Pandas' filtering capabilities, that we explored in previous lessons, 
# to zoom in to the peak of the Dot Com bubble (1999 - 2002) for both companies and plot the results.
import matplotlib.dates as mdates

# Filter dates to be greater than Jan 1, 1999 but less than Jan 1, 2002
microsoft_bubble = microsoft_stock[(microsoft_stock['Date'] > '1999-01-01') & (microsoft_stock['Date'] < '2002-01-01')]
plt.plot(microsoft_bubble['Date'], microsoft_bubble['Volume'])

# .gcf() - returns the current figure (or plot)
fig_msft = plt.gcf()
# autofmt_xdate():  auto-format X-axis to look nice
plt.gcf().autofmt_xdate()
plt.title("Microsoft Stock: Dot Com Crash")
plt.show()

# Repeat for Apple!
apple_bubble = apple_stock[(apple_stock['Date'] > '1999-01-01') & (apple_stock['Date'] < '2002-01-01')]
plt.plot(apple_bubble['Date'], apple_bubble['Volume'])

# .gcf() - returns the current figure (or plot)
fig_aapl = plt.gcf()
# autofmt_xdate():  auto-format X-axis to look nice
fig_aapl.autofmt_xdate()
plt.title("Apple Stock: Dot Com Crash")
plt.show()


