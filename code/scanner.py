import os
import json
import hashlib
from datetime import datetime


class FScanner:

    def __init__(self,paths):
        self.root_lst = paths
        self.errors = []
        self.key_map = {}
        self.rm_list = []

    def calc_hash(self,filepath):
        data = open(filepath,"rb").read()
        hasher = hashlib.sha1(data)
        key = hasher.hexdigest()
        return key

    def check_key(self,key):
        if key in self.key_map:
            return True
        return False

    def checker(self,fpath):
        key = self.calc_hash(fpath)
        if self.check_key(key):
            self.key_map[key].append(fpath)
        else:
            self.key_map[key] = [fpath]
        return

    def iter_path(self,path):
        for item in os.listdir(path):
            full_path = os.path.join(path,item)
            yield full_path

    def walk_dir(self,path):
        for item in self.iter_path(path):
            if os.path.isfile(item):
                self.checker(item)
            else:
                self.walk_dir(item)
        print(path)

    def key_count(self):
        total = len(self.key_map.keys())
        print(total)
        return

    def scan(self):
        for root_dir in self.root_lst:
            self.walk_dir(root_dir)
        return self.key_map


    def get_remove_list(self):
        for path_lst in self.key_map.values():
            if len(path_lst) <= 1: continue
            sm_id, dcount = None,None
            for id,path in enumerate(path_lst):
                parent = os.path.dirname(path)
                p_size = len(os.listdir(parent))
                if not dcount or dcount > p_size:
                    sm_id, dcount = id, p_size
            for i in range(len(path_lst)):
                if i != sm_id: self.rm_list.append(path_lst[i])
        return self.rm_list





def get_remove_list(inp,rm_list=[]):
    for path_lst in inp.values():
        if len(path_lst) <= 1: continue
        sm_id, dcount = None,None
        for id,path in enumerate(path_lst):
            parent = os.path.dirname(path)
            p_size = len(os.listdir(parent))
            if not dcount or dcount > p_size:
                sm_id, dcount = id, p_size
        for i in range(len(path_lst)):
            if i != sm_id: rm_list.append(path_lst[i])
    return rm_list




ROOT_DIRS = ["A:\\Books","D:\\books"]

if __name__ == "__main__":
    scanner = FScanner(ROOT_DIRS)
    data = scanner.scan()
    out_filename = "A:\\scan_output." + str(datetime.now().toordinal()) + ".json"
    json.dump(data,open(out_filename,"wt"))
    print(len(data))
    rmlst = get_remove_list(data,[])
    txt = open("A:\\rmlst.txt","wt")
    for item in rmlst:
        txt.write(item + "\n")
    txt.close()






    # rm_lst = get_remove_list(k_map,[])
    # print(len(rm_lst))
    # rmf = open("rm_lst.txt","wt")
    # filled = [rmf.write(fp+"\n") for fp in rm_lst]
    # rmf.close()
    # k_map = json.load(open(fp,"rt"))


