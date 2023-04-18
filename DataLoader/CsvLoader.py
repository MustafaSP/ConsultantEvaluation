import pandas as pd
from DataClasses.ConsultantComment import ConsultantComment
from NlpProcess import SentimentLabeling
from NlpProcess.Preprocess import TextCleaning



def consultantCsvLoader(csvPath, dataDict, sentimentModelPath,stopWordPath,maxRow=None):
    df = pd.read_csv(csvPath)

    if maxRow!=None:
        df=df[:maxRow]

    comments = df.Comment.values.tolist()

    for index in range(len(comments)):
        comments[index]=TextCleaning.clean_text(comments[index],stopWordPath)

    commentSentimentLabels = SentimentLabeling.labeling(comments, sentimentModelPath)

    for index, row in df.iterrows():
        consultant = row["Consultant"]
        comment = comments[index]
        commentType = row["CommentType"]
        orderDate = row["OrderDate"]

        consultantComment = ConsultantComment(comment=comment, commentType=commentType, orderDate=orderDate,
                                              commentSentimentLabel=commentSentimentLabels[index])
        try:
            dataDict[consultant].append(consultantComment)
        except:
            dataDict[consultant] = [consultantComment]

    return dataDict
