import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import sys

# Function to load and preprocess data with dynamic thresholding and trailing window smoothing
def load_data_updated(file_path):
    df = pd.read_csv(file_path, engine='python')
    df.dropna(how="all", inplace=True)  # Drop rows with all NaN values
    
    # Fix the timestamp format inconsistency
    try:
        initial_timestamp = datetime.strptime(df["Time"].iloc[0], '%b-%d-%Y %H-%M-%S.%f')
    except ValueError:
        initial_timestamp = datetime.strptime(df["Time"].iloc[0], '%d-%b-%Y %H-%M-%S.%f')
    
    # Invert the optical read values
    df["Inverted Optical Read"] = df["Optical Read"].max() - df["Optical Read"]
    
    # Smooth the Inverted Optical Read values using a rolling window (trailing window)
    window_size = 3  # this can be adjusted as needed
    df["Smoothed Inverted Optical Read"] = df["Inverted Optical Read"].rolling(window=window_size).mean().fillna(df["Inverted Optical Read"])
    
    # Calculate the first derivative of the smoothed inverted optical read
    df["Smoothed Derivative"] = df["Smoothed Inverted Optical Read"].diff().fillna(0)
    
    # Removing the first 20 rows
    df = df.iloc[20:]
    
    return df, initial_timestamp

# Function to parse timestamp with two different formats
def parse_timestamp(timestamp):
    try:
        return datetime.strptime(timestamp, '%b-%d-%Y %H-%M-%S.%f')
    except ValueError:
        return datetime.strptime(timestamp, '%d-%b-%Y %H-%M-%S.%f')

# Parameters for dynamic thresholding
initial_cycles = 20  # Initial cycles to compute baseline 20
multiplier = 3  # Multiplier for standard deviation to set threshold 3

# Load and process the data using the modified function with trailing window
file_path = sys.argv[1]
df_trailing, initial_timestamp_trailing = load_data_updated(file_path)

# Compute the baseline using the first few cycles
baseline_mean = df_trailing["Smoothed Derivative"].iloc[:initial_cycles].mean()
baseline_std = df_trailing["Smoothed Derivative"].iloc[:initial_cycles].std()

# Calculate dynamic threshold
dynamic_threshold = baseline_mean + multiplier * baseline_std

# Find the first cycle where the POSITIVE derivative exceeds the dynamic threshold
exceeding_cycles = df_trailing[(df_trailing["Smoothed Derivative"] > dynamic_threshold) & (df_trailing["Smoothed Derivative"] > 0)]["Cycle Number"].values

# Check if there are any cycles exceeding the threshold
if len(exceeding_cycles) == 0:
    start_cycle_dynamic = None
    result_dynamic = "Negative (never exceeded threshold)"
    ttp_result_dynamic = "NA"
    max_derivative_dynamic = "NA"
else:
    start_cycle_dynamic = exceeding_cycles[0]
    
    # Calculate the time to positive using the dynamic threshold
    timestamp_at_TTP_dynamic = parse_timestamp(df_trailing[df_trailing['Cycle Number'] == start_cycle_dynamic]["Time"].values[0])
    time_difference_dynamic = (timestamp_at_TTP_dynamic - initial_timestamp_trailing).seconds / 60  # in minutes

    # Determine the result based on the maximum smoothed derivative value
    max_derivative_dynamic = df_trailing['Smoothed Derivative'].max()
    if max_derivative_dynamic >= dynamic_threshold:
        result_dynamic = "Positive"
        ttp_result_dynamic = time_difference_dynamic
    else:
        result_dynamic = "Negative"
        ttp_result_dynamic = "NA"

# Plot the results
fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.set_xlabel('Cycle Number')
ax1.set_ylabel('Inverted Optical Read', color='tab:blue')
ax1.plot(df_trailing["Cycle Number"], df_trailing["Inverted Optical Read"], color='tab:blue', label='Inverted Optical Read')
if start_cycle_dynamic:
    ax1.axvline(x=start_cycle_dynamic, color='r', linestyle='--', label='TTP (Dynamic Threshold) at cycle {:.2f}'.format(start_cycle_dynamic))
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Smoothed Derivative', color='tab:green')
ax2.plot(df_trailing["Cycle Number"], df_trailing["Smoothed Derivative"], color='tab:green', label='Smoothed First Derivative (Trailing Window)')
ax2.axhline(y=dynamic_threshold, color='orange', linestyle='-.', label='Dynamic Threshold')
ax2.tick_params(axis='y', labelcolor='tab:green')

# Integrated legend for both y-axes
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=0)

plt.title('Optical Read vs. Cycle Number with TTP Indicated (Dynamic Threshold)')
plt.show()

print("Result:", result_dynamic)
print("Time to Positive (TTP) in minutes:", ttp_result_dynamic)
print("Maximum Smoothed Derivative Value:", max_derivative_dynamic)
