import nltk.tokenize
import spacy
import json
from pprint import pprint
import re
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize
import time
from app.requirement_improver import RequirementChecker
import codecs
import pandas as pd
import numpy as np
from glob import glob
import os

desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',25)

lexicons_all_files = glob("./app/lexicons/lex_*.json")
lexicons_all_files = ['/'.join(x.split('\\')) for x in lexicons_all_files]

defaultJsonDict = {
  "requirements": [
    {
      "id": "1",
      "text": "The system may respond within 5 seconds."
    },
    {
      "id": "2",
      "text": "As far as possible , inputs are checked for plausibility."
    },
    {
      "id": "3",
      "text": "The system must provide the signal in the highest resolution that is desired by the signal customer."
    }
  ],
  "config": {
    "algorithms": ["Lexical", "RegularExpressions", "POSRegularExpressions", "CompoundNouns", "Nominalization"]
  }
}

class Requirement:

    def __init__(self, *, id, text):
        # These attributes are a part of the OpenReq JSON Standard: <Link to OpenReq JSON Standard>

        ## Required by this API ##
        # The unique identifier of a Requirement. Not a null value or an empty string.
        self.id = id
        # The textual description or content of a Requirement.
        self.text = text

def get_reqs(json_data):
    reqs = json_data['requirements']
    reqs = [Requirement(id=req['id'], text=req['text']) for req in reqs]
    return reqs

def getLexiconJSONCombined(allfileslist):
    filesallDict = {}
    for f in allfileslist:
        with open(f, encoding='mbcs') as json_file:
            data = json.load(json_file)
            filesallDict.update(data)
    return  filesallDict

def getReSmellTypeList():
    alljsondata = getLexiconJSONCombined(lexicons_all_files)
    return list(set([x['language_construct'] for x in list(alljsondata.values())]))

def getReSmelltypeMappingDict():
    thelist = getReSmellTypeList()
    thelist = sorted(thelist)
    theMappingDict = {}
    for i in range(len(thelist)):
        theMappingDict[thelist[i]] = "res_"+str(i+1)
    return theMappingDict

reSmellDict = getReSmelltypeMappingDict()
df = pd.read_csv('NewFeature.csv')
keyList = df['key'].values.tolist()

#with open('testingConfig.json') as json_file:
#    thereqjson = json.load(json_file)
#theRE = RequirementChecker(get_reqs(defaultJsonDict))
#pprint(theRE.check_quality())

#print(df.loc[df['key']==keyList[0], 'description'].values[0])

#description_list = df.loc[:,'description'].values.tolist()
#df_nnan=df[df['summary'].notna()]
#print(df_nnan.head())
#print(df.shape)
#testingText = description_list[0]

#sentences = nltk.tokenize.sent_tokenize(testingText)

#load_grammar = nltk.data.load('english_grammer.cfg')
#file_input = codecs.open('english_input.txt', 'r')
#for sent in file_input:
#    print(sent)