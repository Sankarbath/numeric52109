###
## Test file for the package simple_package
## Execute as 'python test_sp.py'
###

import simple_package as sp

if __name__ == '__main__':
    ## Define two numbers
    a = 1;
    b = 2;
    
    ## Print their sum with a nice message.
    print(f"The sum of {a} and {b} is {a + b}")

    ## Now do the same for the function in sp
    print(f"The product of {a} and {b} is {sp.multiply(a,b)}")

import simple_package.operations as op # We import the operations module directly

#if __name__ == '__main__':
    # Call the new interface function
    #op.calculator_interface()

if __name__ == '__main__':
    # ... (existing code to launch calculator_interface) ...
    
    # --- Test Statistics and Graphics Functions ---
    import numpy as np
    
    sample_data = np.random.normal(loc=10, scale=2, size=100) # Example data
    
    print("\nStarting statistics test...")
    
    mean_val, median_val, processed_data = sp.calculate_and_display_stats(sample_data)
    
    # Call the plotting function
    sp.plot_histogram(processed_data, mean_val, median_val)