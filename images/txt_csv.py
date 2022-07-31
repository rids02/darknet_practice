from os import renames
import json
import sys
def save_as_dict(f_):
  text = []
  with open(f_) as f:
    text = f.readlines()
  name_ = text[0].split(":")[0].split("/")[-1]
  res={name_:{}}
  for i in range(1, len(text)):
    if list(text[i].split(":"))[0] in res[name_]:
      res[name_][list(text[i].split(":"))[0]] += 1
    else:
      res[name_][list(text[i].split(":"))[0]] = 1
  json_object = json.dumps(res, indent = 4) 
  return json_object
print(save_as_dict(sys.argv[1]), end=',')