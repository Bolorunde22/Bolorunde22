import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Gender': ['Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male',
               'Male', 'Male', 'Male', 'Female', 'Female', 'Female', 'Female',
               'Female', 'Female', 'Female', 'Female', 'Female', 'Female'],
    'BreathHoldTime': [60.75, 67.41, 42.19, 59.74, 52.64, 43.37, 73.27,
                       9.09, 51.15, 58.32, 22.22, 30.57, 17.47, 22.39,
                       26.90, 36.85, 27.33, 29.55, 13.87, 34.66],
    'Height': [184, 182, 180, 191, 189, 181, 180, 170, 176, 185, 175, 158,
               166, 175, 160, 165, 166, 170, 170, 172]
}

data_frame = pd.DataFrame(data)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(data_frame['BreathHoldTime'], bins=10, color='blue', edgecolor='black', alpha=0.7)
plt.title('Histogram of Breath-Holding Time')
plt.xlabel('Time for Breath Held (seconds)')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
males = data_frame[data_frame['Gender'] == 'Male']['BreathHoldTime']
females = data_frame[data_frame['Gender'] == 'Female']['BreathHoldTime']

plt.scatter(males, [0] * len(males), color='green', label='Male', alpha=0.6)
plt.scatter(females, [1] * len(females), color='red', label='Female', alpha=0.6)

plt.title('Side-by-Side Dot Plot of Breath-Holding Time')
plt.yticks([0, 1], ['Male', 'Female'])
plt.xlabel('Time for Breath Held (seconds)')
plt.legend()

plt.tight_layout()
plt.show()