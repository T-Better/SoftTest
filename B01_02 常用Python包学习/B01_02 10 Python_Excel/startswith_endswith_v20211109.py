import os

for t in os.scandir(os.getcwd()):
    if t.name.endswith('.xlxs'):
        print(e.name,e.path,e.is_dir())
    
