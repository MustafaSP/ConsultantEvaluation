from flask import Flask, render_template, request
import random

from faker import Faker

fake = Faker()

from DB.CommentAdder import CommentAdder

app = Flask(__name__)

uid = random.randint(1, 100000)
name = fake.name()
surname = fake.last_name()
mail = fake.email()
consultant = fake.name() + " " + fake.last_name()
orderDate = fake.date()


@app.route('/', methods=["GET", "POST"])
def start():
    return render_template("index.html", name=name, surname=surname, mail=mail, consultant=consultant, date=orderDate,
                           uid=uid)


@app.route("/comment", methods=["POST"])
def comment():
    mail = request.form['mail']
    consultant = request.form['consultant']
    commentType = request.form['commentType']
    commentText = request.form['commentText']

    newcomment = CommentAdder(name=name, surname=surname, mail=mail, consultant=consultant,
                                  commentType=commentType, commentText=commentText, orderDate=orderDate,
                                  uid=uid,dbPath="../../DB/Remax.db")
    newcomment.commentAppend()
    del newcomment

    return render_template("feedback.html")


if __name__ == '__main__':
    app.run()
