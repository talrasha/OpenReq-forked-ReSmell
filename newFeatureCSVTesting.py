import os
from pprint import pprint

import nltk.tokenize
import requests
import requests.auth
import pandas as pd
import numpy as np
import time
import csv, json
import itertools
from difflib import SequenceMatcher
import datetime
import matplotlib.pyplot as plt
import operator
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from bs4 import BeautifulSoup
import ssl
from urllib.request import urlopen
from app.requirement_improver import RequirementChecker

desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',25)

df = pd.read_csv('NewFeature.csv')
textlist = df.loc[:,'description'].values.tolist()
testingText = textlist[5]

reSmellDict = {
    "Compound Noun": "ReS_1",
    "Ambiguous Adverb or Adjective": "ReS_2",
    "Other / Misc": "ReS_3",
    "Subjective Language": "ReS_4",
    "Nominalization": "ReS_5",
    "Comparatives and Superlatives": "ReS_6",
    "Negative Statement": "ReS_7",
    "Vague Pronoun": "ReS_8",
    "Coordination": "ReS_8"
}

def getSentenceListfromText(textstring):
    try:
        textstring = ' '.join([x for x in textstring.split('\n')])
    except AttributeError:
        return []
    sentences = nltk.tokenize.sent_tokenize(textstring)
    print(len(sentences))
    for item in sentences:
        print(item.strip('\n'))

