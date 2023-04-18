import random

import pandas as pd
from faker import Faker

fake = Faker()

defaultCommnetTypes = ["Product", "Communication", "Web Site", "Market Status", "Something Else"]

consultants = []
mails = []
orderDates = []
commnetTypes = []

df = pd.read_csv("train.csv")
fakeName = fake.name() + " " + fake.last_name()

counter = 0
for i in range(df.__len__()):
    if counter < 300:
        counter += 1
    else:
        fakeName = fake.name() + " " + fake.last_name()
        counter = 0

    consultants.append(fakeName)
    mails.append(fake.email())
    orderDates.append(fake.date())
    commnetTypes.append(random.choice(defaultCommnetTypes))

df = df.assign(Consultant=consultants, Mail=mails, OrderDate=orderDates, CommentType=commnetTypes)
df.to_csv('comment.csv', index=False)
