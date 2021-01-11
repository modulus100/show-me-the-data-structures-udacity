import os

# Let us print the files in the directory in which you are running this script
print(os.listdir("./testdir"))

# Let us check if this file is indeed a file!
print(os.path.isfile("./ex.py"))

# Does the file end with .py?
print("./ex.py".endswith(".py"))
