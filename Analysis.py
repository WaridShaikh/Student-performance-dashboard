import pandas as pd
import matplotlib.pyplot as plt

# Student data
data = {
  'Name': ['Ali', 'Ahmed', 'Sara', 'Ayesha', 'Warid'],
  'Math': [85, 78, 92, 88, 95],
  'Science': [80, 82, 89, 90, 93]
}

df = pd.DataFrame(data)
print(df)

# Average marks
print("Average Math:", df['Math'].mean())

# Simple Graph
df.plot(x='Name', y=['Math', 'Science'], kind='bar')
plt.title("Student Performance Dashboard")
plt.show()
