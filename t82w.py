import logging
from gensim.models import word2vec
import multiprocessing


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.Text8Corpus('./wiki_fixed.text8')
    model = word2vec.Word2Vec(sentences, size=200)
    model.save("word2vec.model", size=200, workers=multiprocessing.cpu_count())
