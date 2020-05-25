import pandas as pd
import os
import gensim
from gensim import models, corpora
from gensim import similarities
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
import nltk
from pprint import pprint
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import brown
from nltk.stem.wordnet import WordNetLemmatizer
import string
import re #regex
import spacy
import en_core_web_sm
import tqdm
import numpy as np
from sklearn.utils import shuffle
import glob
import shutil

poems = pd.read_csv('/Users/admin/Documents/GitHub/ThirdYearProject/romanticCSV.csv')

poemnum = poems.shape[0]


for i in range(poemnum):
    forname = str(i)
    f = open('Poem'+forname+'.txt', 'a')
    f.write(" ")
    f.close()


outfilename = "combine.txt"
with open(outfilename, 'wb') as outfile:
    for filename in glob.glob('*.txt'):
        if filename == outfilename:
            # don't want to copy the output into the output
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)
