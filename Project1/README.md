# Project 1: Comparison-based Sorting Algorithms

This repository contains a Jupyter notebook that analyzes differnet sorting algorithms on arrays of different sizes and conditions (random, sorted, and reversed).

## Prerequisites

To run the notebook, you need to have the following installed:

- Any recent version of Python (make sure to pick the version you want when selecting kernal)
- Jupyter Notebook
- Required Python packages: `matplotlib`, `numpy`

You can install the required Python packages using pip:

```bash
pip install matplotlib numpy

## Recursion Limit

I set the maximum number of recursions to 10^6 you can change thhis limit if you recieve a stackover flow error but the shorter the limit the more likely you will get a recursion depth error while sorting arrays with large input sizes. 

The limit is in the second cell and the line of code is sys.setrecursionlimit(10**6).

## Input Size 
The notebook will ask you to input the sizes as a comma-separated list. For example, to test with sizes 1000, 5000, and 10000, you would input 1000,5000,10000 and it will automatically generate a plot for you. The larger the input sizes the longer it will take to sort.

