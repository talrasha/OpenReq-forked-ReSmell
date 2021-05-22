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

#print(df.loc[:,['key','summary','description','res_1',  'res_2',  'res_3',  'res_4', 'res_5', 'res_6', 'res_7', 'res_8',  'res_9',  'sent_count', 'sent_smell']].head())

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

count = 0
with open('summaryReSmellcount.csv', 'a', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["key", "sres_1", "sres_2", "sres_3", "sres_4", "sres_5", "sres_6", "sres_7", "sres_8", "sres_9"])
for i in range(len(keyList)):
    resmld = fromKeyGetReSmellResultSpecifiedDictforSummary(keyList[i])
    dictkeysortedlist = sorted(resmld)
    thereturenFeatures = [keyList[i]]
    thereturenFeatures.extend(dictkeysortedlist)
    with open('summaryReSmellcount.csv', 'a', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([keyList[i]]+[resmld[x] for x in dictkeysortedlist])
    count +=1
    print(count)

dfs = pd.read_csv('summaryReS.csv')
temp = dfs.loc[:, 'sum'].values.tolist()
print(sum(temp)/len(temp))