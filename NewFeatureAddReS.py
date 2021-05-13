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
  "requirements": [],
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
#df = df[df['description'].isna()]
keyList = df['key'].values.tolist()

def fromKeyGetSummaryAndDescriptionSentenceList(thekey):
    theSummaryText = df.loc[df['key']==thekey, 'summary'].values[0]
    if str(df.loc[df['key']==thekey, 'description'].values[0]) == 'nan':
        theDescriptionText = ""
    else:
        theDescriptionText = df.loc[df['key'] == thekey, 'description'].values[0]
        theDescriptionText = ' '.join([x for x in theDescriptionText.split('\n')])
    #STsentences = nltk.tokenize.sent_tokenize(theSummaryText)
    #DTsentences = nltk.tokenize.sent_tokenize(theDescriptionText)
    #sentences = STsentences + DTsentences
    sentences = nltk.tokenize.sent_tokenize(theDescriptionText)
    sentences.append(theSummaryText)
    sentences = [x.strip('\n') for x in sentences]
    return sentences

def fromKeyGetReSmellResultSpecifiedDict(thekey):
    sentenceList = fromKeyGetSummaryAndDescriptionSentenceList(thekey)
    defaultJsonDict = {
        "requirements": [],
        "config": {
            "algorithms": ["Lexical", "RegularExpressions", "POSRegularExpressions", "CompoundNouns", "Nominalization"]
        }
    }
    for i in range(len(sentenceList)):
        defaultJsonDict["requirements"].append({"id": thekey+"_"+str(i+1), "text": sentenceList[i]})
    theRE = RequirementChecker(get_reqs(defaultJsonDict))
    return theRE.check_quality()

def fromKeyGetSmellCount(thekey):
    resultDict = fromKeyGetReSmellResultSpecifiedDict(thekey)
    theSmellCountDict = {}
    for item in list(resultDict.keys()):
        if resultDict[item]:
            for smell in resultDict[item]:
                if reSmellDict[smell['language_construct']] in theSmellCountDict:
                    theSmellCountDict[reSmellDict[smell['language_construct']]] += 1
                else:
                    theSmellCountDict[reSmellDict[smell['language_construct']]] = 1
        else:
            continue
    for res in list(reSmellDict.values()):
        if res in theSmellCountDict:
            continue
        else:
            theSmellCountDict[res] = 0
    return theSmellCountDict

def fromKeyGet2AddFeatureDict(thekey):
    theAddFeatureDict = fromKeyGetSmellCount(thekey)
    theAddFeatureDict['sent_count'] = len(fromKeyGetSummaryAndDescriptionSentenceList(thekey))
    resultDict = fromKeyGetReSmellResultSpecifiedDict(thekey)
    resultkeys = list(resultDict.keys())
    theAddFeatureDict['sent_smell'] = len([x for x in resultkeys if resultDict[x]])
    return theAddFeatureDict

def getAddedSmellCSV(thedf, thenewfilename):
    resultdf = thedf.copy()
    thekeylist = resultdf['key'].values.tolist()
    theresultlistofdicts = [fromKeyGet2AddFeatureDict(x) for x in thekeylist]
    the2Addkeys = list(theresultlistofdicts[0].keys())
    for key in the2Addkeys:
        resultdf[key] = np.array([x[key] for x in theresultlistofdicts])
    resultdf.to_csv(thenewfilename, index=False)

getAddedSmellCSV(df, "NewFeature_plus.csv")

#print(len(fromKeyGetSummaryAndDescriptionSentenceList(keyList[2])))
#print(fromKeyGetSmellCount(keyList[2]))

# Check Long Multi-sentence Summaries
#summaryList = df['summary'].values.tolist()
#for item in summaryList:
#    tokenlist = sent_tokenize(item)
#    if len(tokenlist) == 1:
#        continue
#    else:
#        print(item)


#for i in range(len(summaryList)):
#    defaultJsonDict["requirements"].append({"id": str(i+1), "text": summaryList[i]})
#theRE = RequirementChecker(get_reqs(defaultJsonDict))
#pprint(theRE.check_quality())

#with open('testingConfig.json') as json_file:
#    thereqjson = json.load(json_file)
#theRE = RequirementChecker(get_reqs(defaultJsonDict))
#pprint(theRE.check_quality())



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