# jawiki2w2v
jawiki dumpのURLを渡せばText8とword2vecを生成してくれるツール

## 事前準備

### MeCabとneologdを入れる

```bash
git clone https://github.com/taku910/mecab && \
    cd mecab/mecab && \
    ./configure --enable-utf8-only && \
    make && \
    make check && \
    make install && \
    pip3 install --no-cache-dir mecab-python3 && \
    ldconfig && \
    cd ../mecab-ipadic && \
    ./configure --with-charset=utf8 && \
    make && \
    make install
```

```bash
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd && \
    pushd mecab-ipadic-neologd && \
    yes yes | ./bin/install-mecab-ipadic-neologd -n && \
    popd && \
    yes | rm -r mecab-ipadic-neologd
```

### pythonモジュールを入れる

```
pip3 install gensim tqdm beautifulsoup4 mecab-python3 lxml
```

## 使い方

```
Usage: ./wiki2w2v.sh <wiki dump url> [neologd path]
```

例:

```
./wiki2w2v.sh https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2
```
