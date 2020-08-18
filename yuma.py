import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


# Data
df = pd.read_csv('2010YumaAZ.csv')
days = ['TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'MONDAY']
print(df)

data = []

for day in days:
    trace = go.Scatter(x=df['LST_TIME'],
                       y=df[df['DAY'] == day]['T_HR_AVG'],
                       mode='lines',
                       name=day)
    data.append(trace)

#Layout
layout = go.Layout(title='Daily temp averages')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)

# lines and markers

