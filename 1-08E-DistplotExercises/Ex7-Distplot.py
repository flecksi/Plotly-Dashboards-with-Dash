#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv('../data/iris.csv')

# Define the traces
hist_data = [df[df['class']==classs]['petal_length'] for classs in df['class'].unique() ]
hist_labels = [classs for classs in df['class'].unique() ]

# HINT:
# This grabs the petal_length column for a particular flower
# df[df['class']=='Iris-some-flower-class']['petal_length']
# Define a data variable



# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(hist_data, hist_labels)
pyo.plot(fig, filename='DistPlot_Exercise.html')
