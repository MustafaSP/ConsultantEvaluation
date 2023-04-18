import sqlite3
from DataClasses.ConsultantComment import ConsultantComment
from NlpProcess import SentimentLabeling
from NlpProcess.Preprocess import TextCleaning


def consultantDbLoader(dbPath, dataDict, sentimentModelPath, stopWordPath, maxRow=None):
    consultants = []
    comments = []
    commentTypes = []
    orderDates = []

    conn = sqlite3.connect(dbPath)

    if maxRow != None:
        cursor = conn.execute("SELECT  Consultant,Comment,CommentType,OrderDate from Comment LIMIT ?", [maxRow])
    else:
        cursor = conn.execute("SELECT  Consultant,Comment,CommentType,OrderDate from Comment")

    for row in cursor:
        consultants.append(row[0])
        comments.append(TextCleaning.clean_text(row[1], stopWordPath))
        commentTypes.append(row[2])
        orderDates.append(row[3])

    conn.close()

    commentSentimentLabels = SentimentLabeling.labeling(comments, sentimentModelPath)

    for consultant, comment, commentType, orderDate, commentSentimentLabel in zip(consultants, comments, commentTypes,
                                                                                  orderDates, commentSentimentLabels):

        consultantComplaint = ConsultantComment(comment, commentType, orderDate, commentSentimentLabel)
        try:
            dataDict[consultant].append(consultantComplaint)
        except:
            dataDict[consultant] = [consultantComplaint]

    return dataDict
