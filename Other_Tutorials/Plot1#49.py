#Using matplot lib plot a graph with the following values
#x = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9] y = [0.1 ,0.2 ,0.3 ,0.4 ,0.5 ,0.6 ,0.7 ,0.8 ,0.9] -display the plot in grid view -set the label for the horizontal axis to 'new york' -set the label for the vertical axis to 'Team Ai'

import matplotlib.pyplot as plt

x = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
y = [0.1 ,0.2 ,0.3 ,0.4 ,0.5 ,0.6 ,0.7 ,0.8 ,0.9]

plt.plot(x,y)

plt.xlabel('new york')
plt.ylabel('Team Ai')

plt.title('A simple graph')

plt.show()
