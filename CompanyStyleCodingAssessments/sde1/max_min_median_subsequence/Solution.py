# Function to find the minority and majority medians of a subarray of size k
def medians(values, k):
    # Sort the values to easily find medians
    values.sort()
    n = len(values)
    
    # Calculate the median position for an array of size k (1-based indexing)
    # For odd k: median at (k+1)//2, for even k: lower median at (k+1)//2
    t = (k + 1) // 2
    
    # Find the minimum median: the t-th smallest element in the first k elements
    min_median = values[t - 1]
    
    # Find the maximum median: the t-th smallest element in the last k elements
    # This is at position (n - k + t - 1) in the sorted array
    max_median = values[n - k + t - 1]
    
    # Return both medians as [majority_median, minority_median]
    return [max_median, min_median]
