import matplotlib.pyplot as plt

x = [2, 4, 6]
y = [1, 3, 5]
plt.plot(x, y)
#plt.show()

import plotly
print(plotly.__version__)

from plotly.graph_objs import Scatter, Layout
plotly.offline.plot({
"data": [
    Scatter(x=[1, 2, 3, 4], y=[4, 1, 3, 7])
],
"layout": Layout(
    title="hello world"
)
})