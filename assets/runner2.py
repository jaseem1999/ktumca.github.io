import os
import json

def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir\
(path)]
    else:
        d['type'] = "file"
    return d

filedata = json.dumps(path_to_dict('./materials'))


with open("../app/filesystem/filesystem.component.ts", "r+") as f:
    d = f.readlines()
    f.seek(0)
    line = 1
    for i in d:
      print(str(line)+" "+i)
      if line == 10:
        f.write(" masterDirectory = "+str(filedata))
      else:
        f.write(i)
      line=line+1
    f.truncate()
