import pandas as pd


class ConsultantComment:
    def __init__(self,comment,commentType,orderDate,commentSentimentLabel=None):

        self.comment=comment
        self.commentType=commentType
        self.orderYear=orderDate.split("-")[0]
        self.commentSentimentLabel = commentSentimentLabel

        day=pd.Timestamp(orderDate)
        self.weekDayName=day.day_name()
        self.month = day.month_name()

