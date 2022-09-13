import json
import pandas as pd
from io import StringIO

from generics import BasicORM

""" 
Generic Data Entry: 
Enter values for fields dynamically read in by the program from a csv upload.
"""

# Prompt user for path to file
# Example: ./file/upload2.csv
file = input("Enter directory and file to upload: ")
df = pd.read_csv(file)


# Get the Column Headers from CSV file
header_attributes =[]
for header in df.columns:
    header_attributes.append(header)

# Prints the existing list of tuples in the CSV file 
# after initializing a generic class instance.
generic = BasicORM()
data_list = []
for value in df.itertuples():
    for x, header in enumerate(header_attributes):
        setattr(generic, header, value[x+1])
    data_list.append(vars(generic))
print(data_list)

# Creates a new generic item prompting user for inputs
new_generic = BasicORM()
for header in header_attributes:
    value = input(f'Enter {header}: ')
    setattr(new_generic, header, value)


# prints the new_generic class attributes and values as a dictionary
generic_obj = vars(new_generic)
print(vars(new_generic))

# Converts the object into a pandas DataFrame, Appends the new obj to the CSV file
obj = pd.DataFrame(generic_obj, index=[0])
obj.to_csv(file, mode='a', index=False, header=False)



