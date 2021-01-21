import json
import shutil
from pathlib import Path


temp_lib = "V:\\Temp_Library"
path_priority = ("C:", "A:\\Books""D:")
path = Path(__file__).resolve().parent

dic = json.load(open(path / "data.json","rt"))

def pick(data):
    lst = []
    for v in data.values():
        try:
            m = next(i for i in v if "A:\\Cal" not in i)
        except StopIteration:
            m = v[0]
        lst.append(shutil.copy(m,temp_lib))

pick(dic)

# def choose_path(path_lst):
#      next(p for p in path_lst if "A:\\Cal" not in p)

# def select_one(dic):
#     for hkey,path_lst in dic.items():
#         p = choose_path(path_lst)
#         shutil.copy(p,temp_lib)


# select_one(dic)



