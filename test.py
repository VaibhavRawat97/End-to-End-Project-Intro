import os

path = "notebooks/research.ipynb"

# As we can see that 'notebooks' is a folder but research.ipynb is clearly a file 
# So its a combination of file and folder. Moving on...

# print(os.path.split(path))

# We can execute till this part by typing 'python test.py' 
# In the output we're getting ('notebooks', 'research.ipynb')
# So we can see that we're getting two separate values i.e, notebooks(directory) and research.ipynb
# Now, if we're getting the directory, can we keep the directory ? Yes we can, lets see how 

dir,file=os.path.split(path)

os.makedirs(dir,exist_ok=True)
# Here we've created the directory and file as well
with open(file,"w") as f:
    pass 

# We'll have "w" b/c we want to open our file in the writing mode 

# We're getting an error in the terminal as following:
# FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'notebooks'
# In order to avoid this in line 17 we'll change "os.makedirs(dir)" into 
# os.makedirs(dir,exist_ok=True)
# This will help incase the directory is already present, now lets execute the code 

