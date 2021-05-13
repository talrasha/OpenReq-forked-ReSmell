#getAddedSmellCSV(df, 'NewFeature_plus.csv')

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

#print(df.head())
#print(fromKeyGet2AddFeatureDict("EXEC-107"))
#print(fromKeyGet2AddFeatureDict("EXEC-88"))
#print(fromKeyGet2AddFeatureDict("EXEC-84"))
#print(fromKeyGet2AddFeatureDict("EXEC-70"))
#print(fromKeyGet2AddFeatureDict("ACCUMULO-4852"))

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