#!/bin/python3

import math
import os
import random
import re
import sys


def plusMinus(arr):
    """
    Calculate the ratios of positive, negative and zero values in the given array.

    Args:
    arr (list): List of integers.
    """
    
    # Initialize counters
    positive_count = 0
    negative_count = 0
    null_count = 0
    total = len(arr)

    # Iterate through the array and update counters
    for i in arr:
        if i > 0:
            positive_count += 1
        elif i < 0:
            negative_count += 1
        else:
            null_count += 1

    # Calculate and print the ratios
    print("{:.6f}".format(positive_count / total))  # Positive values ratio
    print("{:.6f}".format(negative_count / total))  # Negative values ratio
    print("{:.6f}".format(null_count / total))      # Zero values ratio
