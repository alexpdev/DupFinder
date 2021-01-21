import os, json
from time import time
from pathlib import Path
import hashlib


INFO = {}
FTYPES = (".pdf",".epub",".mobi",".azw",".azw3")
locations = ["A:\\torrents\\ebooks-audiobooks","A:\\Calibre(library)","A:\\Calibre(library)2","A:\\Doranwen","A:\\C\Documents\\My Kindle Content","A:\\Books","D:\\books","D:\\Documents","D:\\ebooks-audiobooks","C:\\Users\\asp\\Documents\\My Kindle Content","C:\\Users\\asp\\Documents\\My Digital Editions","C:\\Users\\asp\\BOOKS"]
# {hash:[path1,path2]}

class Finder:

    def __init__(self,folders,types):
        self.paths = folders
        self.filetypes = types
        self.data = {}

    def find1(self):
        last = self.paths.pop(-1)
        self.scan_files(last)

    def find(self):
        for fp in self.paths:
            print(str(fp))
            self.scan_files(fp)
            print(len(self.data.keys()))

    def scan_files(self,path):
        for fpath in path.iterdir():
            if fpath.is_dir(): self.scan_files(fpath)
            elif fpath.is_file() and fpath.suffix in self.filetypes:
                self.hash_calc(fpath)



    def hash_calc(self,flike):
        fp = open(flike,"rb").read()
        byts = hashlib.sha1(fp)
        hkey = byts.hexdigest()
        if hkey not in self.data:
            self.data[hkey] = [str(flike)]
        else:
            self.data[hkey] += [str(flike)]
        return

if __name__ == '__main__':
    here = Path(__file__).resolve().parent
    dfpath = here / "data.json"
    locs = [Path(i).resolve() for i in locations]
    finder = Finder(locs,FTYPES)
    finder.find()
    data_file = open(dfpath,"wt")
    json.dump(finder.data,data_file)
    data_file.close()
