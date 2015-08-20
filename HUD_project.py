# 1: Intro to Housing Affordability Data
# We are going to explore how to use the programming language, Python, and the Python toolkit, Pandas, to analyze, clean, 
# and visualize housing affordability data from HUD.gov.
# This dataset is derived from an annual survey conducted by the US Department of Housing & Urban Development (HUD) 
# and has detailed information on the affordability of housing as it relates to income and other personal economic indicators.

# We want to import the library, Pandas, into our environment. We use lowercase for most things in Python
import pandas

# read_csv() is the function (or feature) from pandas we want to use to load the file into memory
# housing_2013 is the variable we will use to refer to the loaded dataset
housing_2013 = pandas.read_csv("Hud_2013.csv")

# .head(num_of_rows) is a method that displays the first few (num_of_rows) rows, not counting column headers
housing_2013.head(5)

# Let's learn how to use Pandas to verify the number of columns.
num_columns = len(housing_2013.columns)
# print() is the function we use to output, or display, contents
print("Number of columns:  " + str(num_columns))

# Of the 6 columns, let's filter the dataset down to just 3 columns that looks especially interesting: AGE1, TOTSAL, and FMR.
# the bracket notation [ ] is how we specify the the list of columns we want to select
filtered_housing_2013 = housing_2013[[ 'AGE1', 'FMR','TOTSAL' ]]

# Pandas also has wonderful plotting and visualization capabilities built in and we'll explore how easy it is to create a histogram of any column we want.
# Histograms are used often in the data exploration phase, when you want to get a better feel for how spread out the data is 
# and the range of values in a a column.
# Histograms separate a specific column into bins, each containing a sub-range of values within the total range,
# and visually demonstrate the number of rows in that bin.
# The bins are displayed on the X-axis while the number of rows in that bin are displayed on the Y-axis.
# Let's use the .hist() Pandas feature to quickly plot a histogram of the FMR, or Fair Market Rate, column.
# Histogram of just the FMR, or fair market rate, and AGE1 columns, using 20 bins
filtered_housing_2013.hist(column='FMR', bins=20)
filtered_housing_2013.hist(column='AGE1', bins=20)

# Introduction to Conditional Filtering
# Conditional filtering is a way to filter our DataFrame by specifying criteria that can be evaluated to True or False.
# We can use conditional filtering to select the rows in a DataFrame that meet a certain criteria and those that don't.
# In this case, we only want to select rows that contain a postive value for AGE1.
# Therefore, our filter should evaluate to True whenever the AGE1 value for a row is greater than 0, and False whenever it's less than 0.
# We can express that criteria in Python:
filtered_housing_2013['AGE1'] > 0
evaluated_row_numbers = filtered_housing_2013['AGE1'] > 0
print(evaluated_row_numbers)

# Applying the Conditional Filter
# As you can see, we now have a list evaluated_row_numbers that has a value, True or False, for every row number.
# We can now use this list to select just the rows where the filter criteria is True through bracket notation.
# Bracket notation is the primary way to filter either rows or columns.
cleaned_housing_2013 = filtered_housing_2013[evaluated_row_numbers]
# Preview the first 10 rows
cleaned_housing_2013.head(10)

# Calculating the Difference in DataFrames
# Let's quickly count the number of rows in filtered_housing_2013, the number of rows in cleaned_housing_2013, and the difference between both.
# Remember that we use len() to count the length of objects in Python. 
filtered_count = len(filtered_housing_2013)
cleaned_count = len(cleaned_housing_2013)
print(filtered_count - cleaned_count)