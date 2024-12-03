"""
Show party wise seat share for following results of the Assembly Elections 2023 in
 
  (i) Two different pie charts on two different plots. Party with highest percentage should be shown as slightly detached ( show the percentage seat share on each wedge )
   
  (ii)Two pie charts as subplots on the same figure object
    
   As a bar chart with party name on X axis and seats won on y axis. Show results of both the states on the same bar plot. Give proper legends
   
Madhya Pradesh
BJP - Win (163) 
INC - Win (66) 
BSP – Win (0) 
Others – Win (1)

Rajasthan
INC - Win (69) 
BJP- Win (115) 
BSP- Win (2) 
Others-Win (13)


"""



import matplotlib.pyplot as plt

# Data for the pie charts
states_data = {
    "Madhya Pradesh": {
        "BJP": 163,
        "INC": 66,
        "BSP": 0,
        "Others": 1
    },
    "Rajasthan": {
        "BJP": 115,
        "INC": 69,
        "BSP": 2,
        "Others": 13
    }
}

# Colors for pie charts
colors = {
    "BJP": "#ff9933",
    "INC": "#00aaff",
    "BSP": "#0055aa",
    "Others": "#777777"
}

# Function to calculate the percentage share
def calculate_percentage(data):
    total = sum(data.values())
    return {party: (seats / total) * 100 for party, seats in data.items()}

# Create pie charts
fig, axes = plt.subplots(1, 2, figsize=(14, 7))
for i, (state, results) in enumerate(states_data.items()):
    # Calculate percentages and sort the data
    percentages = calculate_percentage(results)
    sorted_data = sorted(results.items(), key=lambda x: x[1], reverse=True)
    labels = [f"{party} ({seats})" for party, seats in sorted_data]
    values = [seats for _, seats in sorted_data]
    explode = [0.1 if seats == max(values) else 0 for seats in values]  # Detach largest segment
    wedge_colors = [colors[party] for party, _ in sorted_data]

    # Plot pie chart
    ax = axes[i]
    wedges, texts, autotexts = ax.pie(
        values,
        labels=labels,
        autopct=lambda p: f'{p:.1f}%',
        explode=explode,
        colors=wedge_colors,
        startangle=140,
        textprops={'color': "black"},
        wedgeprops={'edgecolor': 'black'}
    )
    ax.set_title(state)

# Adjust layout and show the plot
plt.tight_layout()
plt.show()

