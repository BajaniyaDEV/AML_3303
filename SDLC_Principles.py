## Step 1: Raw / Messy Code (Before Principles)

# Messy code – not modular, not reusable, hard to maintain
import random

numbers = [random.randint(1, 100) for _ in range(10)]
print("Generated numbers:", numbers)

# Calculate average
total = 0
for n in numbers:
    total += n
average = total / len(numbers)
print("Average:", average)

# Find max
max_num = numbers[0]
for n in numbers:
    if n > max_num:
        max_num = n
print("Max:", max_num)


"""
🔴 Problems:

No functions (not modular).

Can’t reuse logic elsewhere.

Hard to extend (e.g., adding min/median).

Not scalable (works only for small lists).

No error handling (reliability issue).

No comments/documentation.
"""

## Step 2: Refactored Code (With Principles)

import random
import importlib
from typing import List

def generate_numbers(count: int, lower: int = 1, upper: int = 100) -> List[int]:
    """Generate a list of random integers."""
    return [random.randint(lower, upper) for _ in range(count)]

def calculate_average(numbers: List[int]) -> float:
    """Return the average of a list of numbers."""
    if not numbers:
        raise ValueError("List of numbers cannot be empty")
    return sum(numbers) / len(numbers)

def find_max(numbers: List[int]) -> int:
    """Return the maximum number from a list."""
    if not numbers:
        raise ValueError("List of numbers cannot be empty")
    return max(numbers)

if __name__ == "__main__":
    # Example workflow (can be reused in other projects)
    nums = generate_numbers(10)
    print("Generated numbers:", nums)
    print("Average:", calculate_average(nums))
    print("Max:", find_max(nums))

"""
✅ Improvements:

Modularity: Code broken into functions.

Reusability: Functions can be used in any project.

Maintainability: Easy to add min/median later.

Scalability: Can handle larger datasets (just change count).

Reliability & Quality: Error handling included.

Security & Trust: Checks against empty input.

Collaboration: Docstrings/comments make it understandable for teams.
"""

def load_data(url):
    """Load data from a CSV file."""
    try:
        pd = importlib.import_module("pandas")
    except ImportError as error:
        raise ImportError(
            "pandas is required to load CSV data. Install it with 'pip install pandas'."
        ) from error
    return pd.read_csv(url)

def calculate_dataframe_average(df, column):
    """Calculate the average of a column."""
    return df[column].mean()

def find_dataframe_max(df, column):
    """Find the maximum value of a column."""
    return df[column].max()

def filter_data(df, column, value):
    """Filter rows based on a specific value."""
    return df[df[column] == value]

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    df = load_data(url)
    average = calculate_dataframe_average(df, "sepal_length")
    maximum = find_dataframe_max(df, "petal_width")
    setosa = filter_data(df, "species", "setosa")
    print("Average sepal length:", average)
    print("Max petal width:", maximum)
    print("\nSetosa flowers:")
    print(setosa.head())

"""
🔴 Problems:

All logic in one block → not modular.

Hard to reuse functions for other datasets.

No error handling → breaks if column names change.

Not scalable (imagine working on multiple CSVs).

No documentation → not good for collaboration.

"""
