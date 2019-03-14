#!/bin/bash
if [ -z $1 ]; then
    echo "Usage: wiki2w2v.sh <wiki dump url> <neologd path>"
else
    if [ -z $2 ]; then
	npath=$2
    else
	npath="/usr/local/lib/mecab/dic/mecab-ipadic-neologd/"
    fi
    wget $1 -O dump.bz2
    tar xjf dump.bz2
    git clone https://github.com/attardi/wikiextractor
    cd wikiextractor
    python WikiExtractor.py -o extracted ../dump.bz2
    cd ..
    python dump2txt.py
    python preprocess.py $npath
    python txt2model.py
fi
