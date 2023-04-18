from keybert import KeyBERT
from sentence_transformers import SentenceTransformer,util

minLevel = 0.70


class KeyExtractor:
    def __init__(self, comments, maxKeyNumber):
        self.maxKeyNumber = maxKeyNumber
        self.model = SentenceTransformer('dbmdz/bert-base-turkish-128k-uncased')
        self.kw_model = KeyBERT(model=self.model)
        self.dataDict = dict()

        self.dataDict = {"dataList": comments,
                         "keyList": [], "keyScoreList": []}

        self.KeyExtractorLineByLine()

    def KeywordsFunction(self, full_text, ngram_range):
        return self.kw_model.extract_keywords(full_text,
                                              use_mmr=True,
                                              diversity=0.7,
                                              keyphrase_ngram_range=(ngram_range, ngram_range),
                                              highlight=False,
                                              top_n=3)

    def SimilarityExtractor(self):

        keyList = self.dataDict["keyList"]
        self.totalScore=0
        self.similarityScoreList = [0]*len(keyList)
        encodeKeyList = []

        for key in keyList:
            encodeKeyList.append(self.model.encode(key[0]))

        for index in range(len(encodeKeyList)):
            for index2 in range(len(encodeKeyList)):
                if index!=index2:
                    encode1=encodeKeyList[index]
                    encode2=encodeKeyList[index2]

                    cos_score = util.cos_sim(encode1, encode2)[0]

                    if cos_score >= 0.90:
                        self.similarityScoreList[index]+=cos_score
                        self.totalScore+=cos_score

    def Resulter(self):

        resultScores=[]
        keyList = self.dataDict["keyList"]
        try:
            percentageRange=100/self.totalScore
        except:
            percentageRange=0

        removes=[]
        for index in range(len(keyList)):
            if float(self.similarityScoreList[index]*percentageRange)>0:
                resultScores.append(float(self.similarityScoreList[index]*percentageRange))
            else:
                removes.append(keyList[index])

        keyList = [delete for delete in keyList if delete not in removes]

        return keyList, resultScores

    def KeyExtractorLineByLine(self):
        dataList = self.dataDict["dataList"]

        for answerText in dataList:
            answerTextLen = len(answerText.split(" "))
            if answerTextLen > 4:
                for ngram_range in range(1, 4):

                    keywords = self.KeywordsFunction(answerText, ngram_range)

                    mostScore = 0
                    secondScore = 0
                    mostScoredKey = ""
                    secondScoredKey = ""

                    for key in keywords:
                        if key[1] >= minLevel and (key[1] > mostScore or key[1] > secondScore):
                            if key[1] > mostScore:
                                mostScore = key[1]
                                mostScoredKey = key[0]
                            else:
                                secondScore = key[1]
                                secondScoredKey = key[0]

                    if mostScoredKey != "":
                        self.dataDict["keyList"].append(mostScoredKey)
                        self.dataDict["keyScoreList"].append(mostScore)

                    if secondScoredKey != "":
                        self.dataDict["keyList"].append(secondScoredKey)
                        self.dataDict["keyScoreList"].append(secondScore)

        self.SimilarityExtractor()