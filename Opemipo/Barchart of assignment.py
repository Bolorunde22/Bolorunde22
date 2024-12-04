import matplotlib.pyplot as plt

# Define the foods and their corresponding values
foods = ['Mushroom', 'Pineapple', 'Prawns', 'Sausage', 'Spinach']
proportions = [0.176, 0.3, 0.085, 0.185, 0.3]

# Create a horizontal bar chart
plt.barh(foods, proportions, color='red')

# Set the title and labels
plt.title('Bar Chart of foods')
plt.xlabel('Proportion of Total')

# Display the chart
plt.show()