import MeCab
import sys
import tqdm

if __name__ == "__main__":
    try:
        neologd_path = sys.argv[1]
    except:
        neologd_path = "/usr/local/lib/mecab/dic/mecab-ipadic-neologd"
    tagger = MeCab.Tagger("-Owakati -d {}".format(neologd_path))

    with open("wiki_fixed.text8", "w") as f1:
        with open("wiki.text8") as f2:
            for line in tqdm.tqdm(f2):
                f1.write(tagger.parse(line).strip()+"\n")
    
