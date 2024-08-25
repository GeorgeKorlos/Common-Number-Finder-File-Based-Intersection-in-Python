# Common Number Finder: File-Based Intersection in Python

This repository contains a Python script that reads numbers from two text files, processes them into lists of integers, and finds the common numbers between these lists. This script is a practical example for those learning about file handling, list comprehensions, and basic set operations in Python.

## Description

The script performs the following operations:

1. **Reads numbers from two text files:** 
    - `file.txt`
    - `file2.txt`

2. **Processes the data:**
    - Strips any leading or trailing whitespace from each line.
    - Converts the valid numeric strings into integers.

3. **Finds the intersection:**
    - Compares the two lists to find numbers that are present in both files.

4. **Outputs the common numbers:** 
    - The final list of common numbers is printed to the console.

### How It Works

1. **File Reading:**
    - The script opens `file.txt` and `file2.txt` and reads the contents line by line.

2. **Data Processing:**
    - Each line is checked to ensure it contains a digit.
    - The lines that contain valid numbers are converted into integers and stored in separate lists.

3. **Finding Common Numbers:**
    - A list comprehension is used to identify numbers that are present in both lists.

4. **Output:**
    - The script prints the list of common numbers to the console.

### Example

Suppose `file.txt` contains:

