import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
data = pd.read_csv('data.csv')

# Display unique values in 'Indicator'
unique_indicators = data['Indicator'].unique()
print("Unique values in 'Indicator':")
for i, indicator in enumerate(unique_indicators):
    print(f"{i + 1}. {indicator}")

# Prompt user to select up to 2 values by number with space separation
selected_indicator_indices = input("Select up to 2 'Indicator' values by number (space separated): ").split()
selected_indicators = [unique_indicators[int(index) - 1] for index in selected_indicator_indices]

# Display unique values in 'Group'
unique_groups = data['Group'].unique()
print("\nUnique values in 'Group':")
for i, group in enumerate(unique_groups):
    print(f"{i + 1}. {group}")

# Prompt user to select up to 2 values by number with space separation
selected_group_indices = input("Select up to 2 'Group' values by number (space separated): ").split()
selected_groups = [unique_groups[int(index) - 1] for index in selected_group_indices]

# Filter the data based on the selected values
filtered_data = data[(data['Indicator'].isin(selected_indicators)) & (data['Group'].isin(selected_groups))]

# Check if 'Group' value is "By Age" or "By Sex"
if "By Age" in selected_groups:
    unique_subgroups = filtered_data['Subgroup'].unique()
    print("\nUnique values in 'Subgroup':")
    for i, subgroup in enumerate(unique_subgroups):
        print(f"{i + 1}. {subgroup}")
    
    # Prompt user to select up to 4 values by number with space separation
    selected_subgroup_indices = input("Select up to 4 'Subgroup' values by number (space separated): ").split()
    selected_subgroups = [unique_subgroups[int(index) - 1] for index in selected_subgroup_indices]
elif "By Sex" in selected_groups:
    selected_subgroups = ["Male", "Female"]

# Plot the graph
plt.figure(figsize=(10, 6))

linestyles = ['-', '--', '-.', ':']
linewidths = [1, 2]
line_count = 0

for indicator in selected_indicators:
    for subgroup in selected_subgroups:
        subset = filtered_data[(filtered_data['Indicator'] == indicator) & (filtered_data['Subgroup'] == subgroup)]
        plt.plot(subset['Time Period Start Date'], subset['Value'], linestyle=linestyles[line_count % 4], linewidth=linewidths[line_count // 4], color='black', label=f'{indicator} - {subgroup}')
        line_count += 1

# Locate legends outside the graph
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlabel('Time Period')
plt.ylabel('Rate')
plt.title('Depression or Anxiety by sex or by age')
plt.grid(True)

# Set X-ticks up to 15 with 90-degree rotation, ensuring equal line space and time
x_values = filtered_data['Time Period Start Date'].unique()
x_ticks = np.linspace(0, len(x_values) - 1, min(len(x_values), 15), dtype=int)
plt.xticks(x_ticks, x_values[x_ticks], rotation=90)

# Adjust layout to ensure everything fits well
plt.tight_layout()

# Save the plot as a PNG file with the selected 'Indicator' and 'Group' values in the filename
filename = f"{'_'.join(selected_indicators)}_{'_'.join(selected_groups)}.png"
plt.savefig(filename,dpi=300)

plt.show()

