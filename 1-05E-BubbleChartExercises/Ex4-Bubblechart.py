#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv('../data/mpg.csv')
df['txt_cyl']=pd.Series(df['cylinders'],dtype=str)
df['txt_mpg']=pd.Series(df['mpg'],dtype=str)

df['label_txt'] = "'" + df['name'] + "'" + '\nCyl=' + df['txt_cyl'] + '\nmpg=' + df['txt_mpg']

# create data by choosing fields for x, y and marker size attributes
data =[go.Scatter(
    x = df['model_year'],
    y=df['horsepower'],
    mode='markers',
    text=df['label_txt'],
    marker=dict(size=0.005*df['weight'], 
                color=df['origin'],
                showscale=True)
)]

# create a layout with a title and axis labels
layout = go.Layout(
    title='horsepower over modelyear',
    hovermode='closest',
    xaxis=dict(title='model year'),
    yaxis=dict(title='horsepower'),
)

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble_exercise.html')
