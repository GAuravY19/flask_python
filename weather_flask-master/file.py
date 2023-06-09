# importing os module  
import os 
    
# Directory 
directory = "GeeksForGeeks"
    
# Parent Directory path 
parent_dir = "D:/"
    
# Path 
path = os.path.join(parent_dir, directory) 
    
# Create the directory 
# 'GeeksForGeeks' in 
# '/home / User / Documents' 
os.mkdir(path) 