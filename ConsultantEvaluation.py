import os
import Graphic.bar as bar
from DataLoader import CsvLoader, DbLoader
import NlpProcess.KeyExtractor as KeyExt
from Utils import FileNameCreator, Texts, Dicts
from NlpProcess.Train import BertClassifier

baseFileName=""
consultant=""

def ToGraphic(datas, dataTitle, weekDays, weekDayTitle, months, monthsTitle, years, yearsTitle, commentTypes,
              commentTypesTitle, path, barColor):

    myKeyxtractor = KeyExt.KeyExtractor(comments=datas, maxKeyNumber=10)
    keyList,keyScoreList = myKeyxtractor.Resulter()
    del myKeyxtractor

    dayScores = []
    dayNames = []

    for weekday in weekDays:
        dayScores.append(weekDays[weekday])
        dayNames.append(weekday)

    monthScores = []
    monthNames = []

    for month in months:
        monthScores.append(months[month])
        monthNames.append(month)

    yearNames = []
    yearScors = []

    for year in years:
        yearScors.append(years[year])
        yearNames.append(year)

    for i in range(len(yearScors)):
        minimum = i

        for j in range(i + 1, len(yearScors)):
            if yearScors[j] < yearScors[minimum]:
                minimum = j

        yearScors[minimum], yearScors[i] = yearScors[i], yearScors[minimum]
        yearNames[minimum], yearNames[i] = yearNames[i], yearNames[minimum]

    typeNames = []
    typeScors = []

    for commentType in commentTypes:
        typeScors.append(commentTypes[commentType])
        typeNames.append(commentType)

    bar.bar(label=keyList, data=keyScoreList, title=dataTitle, path=path, fileName="keys.pdf", yLabel="Percentage",barColor=barColor)
    bar.bar(label=dayNames, data=dayScores, title=weekDayTitle, path=path, fileName="weekday.pdf",barColor=barColor)
    bar.bar(label=monthNames, data=monthScores, title=monthsTitle, path=path, fileName="month.pdf",barColor=barColor)
    bar.bar(label=yearNames, data=yearScors, title=yearsTitle, path=path, fileName="years.pdf",barColor=barColor)
    bar.bar(label=typeNames, data=typeScors, title=commentTypesTitle, path=path, fileName="types.pdf",barColor=barColor)


def PrepareToProcess(consultantComments):
    negatives = []
    negativeTypes = dict()
    negativeWeekdays = Dicts.weekDays.copy()
    negativeYears = dict()
    negativeMonths = Dicts.months.copy()

    neutrals = []
    neutralTypes = dict()
    neutralWeekdays = Dicts.weekDays.copy()
    neutralYears = dict()
    neutralMonths = Dicts.months.copy()

    positives = []
    positiveTypes = dict()
    positiveWeekdays = Dicts.weekDays.copy()
    positiveYears = dict()
    positiveMonths = Dicts.months.copy()

    for consultantComment in consultantComments:

        if consultantComment.commentSentimentLabel == 0:
            negatives.append(consultantComment.comment)
            negativeWeekdays[consultantComment.weekDayName] += 1
            negativeMonths[consultantComment.month] += 1

            try:
                negativeTypes[consultantComment.commentType] += 1
            except:
                negativeTypes[consultantComment.commentType] = 1

            try:
                negativeYears[consultantComment.orderYear] += 1
            except:
                negativeYears[consultantComment.orderYear] = 1

        elif consultantComment.commentSentimentLabel == 1:
            neutrals.append(consultantComment.comment)
            neutralWeekdays[consultantComment.weekDayName] += 1
            neutralMonths[consultantComment.month] += 1

            try:
                neutralTypes[consultantComment.commentType] += 1
            except:
                neutralTypes[consultantComment.commentType] = 1

            try:
                neutralYears[consultantComment.orderYear] += 1
            except:
                neutralYears[consultantComment.orderYear] = 1

        elif consultantComment.commentSentimentLabel == 2:
            positives.append(consultantComment.comment)
            positiveWeekdays[consultantComment.weekDayName] += 1
            positiveMonths[consultantComment.month] += 1

            try:
                positiveTypes[consultantComment.commentType] += 1
            except:
                positiveTypes[consultantComment.commentType] = 1

            try:
                positiveYears[consultantComment.orderYear] += 1
            except:
                positiveYears[consultantComment.orderYear] = 1

        else:
            print("Its Not have a any label!!!")

    negativePath = baseFileName + "/" + consultant + "/" + "Negative/"
    neutralPath = baseFileName + "/" + consultant + "/" + "Neutral/"
    positivePath = baseFileName + "/" + consultant + "/" + "Positive/"

    os.makedirs(negativePath)
    os.makedirs(neutralPath)
    os.makedirs(positivePath)

    ToGraphic(datas=negatives, dataTitle=(Texts.negativeCommentsTitle % {consultant}), weekDays=negativeWeekdays,
              weekDayTitle=(Texts.negativeConsultantDateTitle % {consultant}), months=negativeMonths,
              monthsTitle=(Texts.negativeConsultantMonthTitle % {consultant}),
              years=negativeYears, yearsTitle=(Texts.negativeConsultantYearTitle % {consultant}),
              commentTypes=negativeTypes,
              commentTypesTitle=(Texts.negativeConsultantCommentTypeTitle % {consultant}), path=negativePath,barColor="red")

    ToGraphic(datas=neutrals, dataTitle=(Texts.neutralCommentsTitle % {consultant}), weekDays=neutralWeekdays,
              weekDayTitle=(Texts.neutralConsultantDateTitle % {consultant}), months=neutralMonths,
              monthsTitle=(Texts.neutralConsultantMonthTitle % {consultant}),
              years=neutralYears, yearsTitle=(Texts.neutralConsultantYearTitle % {consultant}),
              commentTypes=neutralTypes,
              commentTypesTitle=(Texts.neutralConsultantCommentTypeTitle % {consultant}), path=neutralPath,barColor="yellow")

    ToGraphic(datas=positives, dataTitle=(Texts.positiveCommentsTitle % {consultant}), weekDays=positiveWeekdays,
              weekDayTitle=(Texts.positiveConsultantDateTitle % {consultant}), months=positiveMonths,
              monthsTitle=(Texts.positiveConsultantMonthTitle % {consultant}),
              years=positiveYears, yearsTitle=(Texts.positiveConsultantYearTitle % {consultant}),
              commentTypes=positiveTypes,
              commentTypesTitle=(Texts.positiveConsultantCommentTypeTitle % {consultant}), path=positivePath,barColor="green")


if __name__ == '__main__':
    csvPath = "comment.csv"
    dbPath = "DB/sqlite3.db"
    consultantWeekDays = Dicts.weekDays.copy()
    dataDict = {}

    if csvPath != "":
        dataDict = CsvLoader.consultantCsvLoader(csvPath=csvPath, dataDict=dataDict,
                                                 sentimentModelPath="NlpProcess/04.16.2023.Sentiment.pth",
                                                 stopWordPath="NlpProcess/Preprocess/TRStopWords.txt",maxRow=500)#you can remove the maxRow parameter if you wish

    if dbPath != "":
        dataDict = DbLoader.consultantDbLoader(dbPath=dbPath, dataDict=dataDict,
                                               sentimentModelPath="NlpProcess/04.16.2023.Sentiment.pth",
                                               stopWordPath="NlpProcess/Preprocess/TRStopWords.txt",maxRow=500)#you can remove the maxRow parameter if you wish


    for consultant in dataDict:
        comments = []
        commentSentimentLabels = []
        commentTypes = []
        commentLabels = []
        commentSentiments = []
        dates = []
        years = []

        baseFileName = "Outputs/"+FileNameCreator.GetFileName()

        os.makedirs(baseFileName)

        consultantWeekDays = dict()
        consultantMonths = dict()

        consultantWeekDays["Total"] = Dicts.weekDays.copy()
        consultantWeekDays[0] = Dicts.weekDays.copy()
        consultantWeekDays[1] = Dicts.weekDays.copy()
        consultantWeekDays[2] = Dicts.weekDays.copy()

        consultantMonths["Total"] = Dicts.months.copy()
        consultantMonths[0] = Dicts.months.copy()
        consultantMonths[1] = Dicts.months.copy()
        consultantMonths[2] = Dicts.months.copy()

        consultantComments = dataDict[consultant]
        PrepareToProcess(consultantComments)

    os.startfile("Outputs")