#Import Python Library
import pandas as pd


#Read csv file
data = pd.read_csv("Salaries.csv")

ranks = data["rank"]


#list the column names
data.columns


#return a tuplerepresenting the dimensionality
data.shape


#Check types for all the columns
data.dtypes


#List first 3 records
data.head(3)

#List last 3 records
data.tail(3)


#list the row labelsand column names
data.axes


#number of dimensions
data.ndim


#Numpy representation of the data
aa = data.values


"""
Data Frames: method loc
33
If we need to select a range of rows, using their labels 
we can use method loc
"""

data.loc[5:15,["rank","phd","sex"]].values


"""
Data Frames: method iloc

If we need to select a range of rows and/or columns, 
using their positions we can use method iloc
"""

data.iloc[5:15,[1,3,5]]

#return max values for all numeric columns

data["salary"].max()


#Return min values for all numeric columns
data.min()


#What are the mean values of the records in the dataset?
data.mean()


#generate descriptive statistics (for numeric columns only)
data.describe()


#returns a random sample of thedata frame
data.sample(5)


#Find how many values in the salarycolumn (use countmethod);
data.salary.count()


"""
Data Frames groupbymethod

Using "group by" method we can:
•Split the data into groups based on some criteria
•Calculate statistics (or apply a function) to each group

"""

a = data.groupby(["rank"])

a.count()


#Counting how many person's salary is more than 150000:
data["sex"][data["salary"]>150000].value_counts()

##Counting how many Phd scholers female's salary is more than 150000:
data["phd"][(data["salary"]>150000) & (data["sex"]=="Female")]

#We can sort the data using 2 or more columns:
data.sort_values(by=["phd",'rank'],ascending=[False,True])

data.sort_values(by=['phd','rank'], ascending = [True,True])


# Select the rows that have at least one missing value
data[data.isnull().any(axis=1)]


#There are a number of methods to deal with missing values in the data frame:
data.dropna()

df = data

# fill all the records having missing values, with mean of that column
for i in ["phd","salary"]:
    df[i] = data[i].fillna(data[i].mode()[0])
