# coding: utf-8
import os
import tqdm
from bs4 import BeautifulSoup

if __name__ == "__main__":
    filepathes = []
    for root, dirs, files in os.walk("./wikiextractor/extracted/"):
        if files and "wiki" in files[0]:
            filepathes += [os.path.join(root,file)for file in files]

    for path in tqdm.tqdm(filepathes):
        with open(path) as f:
            soup = BeautifulSoup(f.read(), "lxml")
        tmp = soup.get_text()
        tmp = [x for x in tmp.split("\n") if x != ""]
        with open("wiki.txt", "a") as f:
            f.write("\n".join(tmp))

