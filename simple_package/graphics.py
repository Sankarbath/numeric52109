# simple_package/graphics.py

# Task 5: Dependency check for matplotlib
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Warning: Matplotlib is not installed. Plotting functions are unavailable.")
    plt = None

def plot_histogram(data, mean_val, median_val):
    """Plots a histogram of the data with mean and median marked."""
    if plt is None:
        print("Error: Cannot plot. Matplotlib is not available.")
        return
    
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=10, edgecolor='black', alpha=0.7)
    
    # Mark mean and median
    plt.axvline(mean_val, color='r', linestyle='dashed', linewidth=2, label=f'Mean ({mean_val:.2f})')
    plt.axvline(median_val, color='g', linestyle='dashed', linewidth=2, label=f'Median ({median_val:.2f})')
    
    plt.title('Data Histogram with Central Tendencies')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()