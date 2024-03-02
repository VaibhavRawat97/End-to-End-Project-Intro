import logging
import os
from datetime import datetime

# After importing these 3 modules above, we'll create the log file 
# Now, inside the root directory we'll have the log folder inside which will be the .log file
# '.log' is the extension of the file but what will be its name ? 
# Name will be Date/H/M/S.log
# H-Hour, M-Minute, S-Second. 
# For the next step go to research.ipynb file and catch up.

LOG_FILE=f"{datetime.now().strftime('%m_%d_%H_%M_%S')}.log"
# The above LOG_FILE will be available inside the log folder.
# So we'll create one more folder named 'logs'.
# Now we'll create the log path 
log_path=os.path.join(os.getcwd(),"logs")
# Now, we have to create the directory for the path we've just created
os.makedirs(log_path,exist_ok=True)
# Now inside this directory our files and folders will be available

# Now we'll join the folder(LOG_FILE) and the log file(log_path)
LOG_FILEPATH=os.path.join(log_path,LOG_FILE)

# After that we'll make our logging configuration, here we'll use a method called basicConfig.

logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
                    
)

# The 'format' will show the format of the message.
 
