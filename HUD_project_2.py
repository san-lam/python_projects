###---Automate Repetitive Tasks in Python---###
# Now we will learn how to automate the same process for both the 2005 and 2007 datasets.

# Create 2 variables, housing_2007 and housing_2005, that contain the DataFrame objects associated with Hud_2007.csv and Hud_2005.csv, respectively.
# Remember from the previous lesson that we read in the 2013 data set in the following way: housing_2013 = pandas.read_csv("Hud_2013.csv")
import pandas
housing_2007 = pandas.read_csv("Hud_2007.csv")
housing_2005 = pandas.read_csv("Hud_2005.csv")

# List
# Now that we have read in both datasets into DataFrame objects, let's add them to a List.
# we can group a few objects into a List object, write the logic once, and apply it to every object in that List.
# A list is a data structure in Python that makes it easy to apply logic over many objects
# This line creats an empty list with no objects
data_frames_list = []

# Adding a year column to each DataFrame, so we can easily keep track easier later
housing_2005['year'] = '2005'
housing_2007['year'] = '2007'

# .append() adds the specified object to the end of the list
data_frames_list.append(housing_2005)
data_frames_list.append(housing_2007)

# the list now contains 2 objects, the respective DataFrames for 2005 and 2007
print(len(data_frames_list))

# Column Filtering
# Create a new DataFrame, filtered_housing_2007, that contains the column filtered version of housing_2007, with just the columns we are interested in.
# The columns we want are: ['AGE1', 'FMR', 'TOTSAL', 'year'].
# First, create a List variable, columns, that contains the names of all of the columns we are interested in.
# then, we use bracket notation on the DataFrame object to specify a filter. We want the filter to just contain the columns list.
columns = ["AGE1", "FMR", "TOTSAL", "year"]
filtered_housing_2007 = housing_2007[columns]

# define a function to filter each DataFrame down to only the columns we want.
# A function is a way to turn our commands into a module to be reused whenever we want
def filter_columns(data_frames_list):
    # Final list we want to return, starts out empty
    new_df_list = list()

    # Use a "for" loop to iterate through each DataFrame. For every DataFrame ("df") in the list: data_frames_list
    for df in data_frames_list:
        # Use a list to specify the columns we want
        columns = ['AGE1', 'FMR', 'TOTSAL', 'year']
        # Filter the current dataframe we are iterating through to have only the columns we want
        filtered_df = df[columns]
        # Add the filtered dataframe object to the empty list we created in the beginning on the function
        new_df_list.append(filtered_df)
    # Functions require a "return" value, which is the result of what happened inside
    return new_df_list

filtered_data_frames_list = filter_columns(data_frames_list)

# 6: Column Filtering Verification
# For every df, or DataFrame, in the list: filtered_data_frames_list
for df in filtered_data_frames_list:
    # print that DataFrame's columns
    print(df.columns)

# Now let's write a function that counts the number of rows in each DataFrame that have negative values for the AGE1 column.
for df in filtered_data_frames_list:
    # Get the year
    year = df['year'][0]
    # Only the rows with negative age values
    negative_age_count = df[df['AGE1'] < 0]
    # Custom print formatting
    print( str(year) + " - " + str(len( negative_age_count ) ) + " rows")

# Multiple Dataset Cleanup
# write a function that automates the clean up we did in the last mission so that we are left only with the rows that contain positive values for the AGE1 column.
def clean_rows(filtered_data_frames_list):
    # Create a new empty list
    cleaned_list = list()
    
    for df in filtered_data_frames_list:
        cleaned_df = df[ df ['AGE1'] > 0 ] 
        cleaned_list.append(cleaned_df)
    return cleaned_list

cleaned_data_frames_list = clean_rows(filtered_data_frames_list)
