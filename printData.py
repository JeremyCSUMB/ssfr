#This is our app that accesses the flask application
from redAPI import * #import everything that we have from redAPI
from flask import Flask #import some items from flask as well as flask and the os
from flask import request #Import requests here for the use of flask
from flask import render_template
import flask
import os

app = flask.Flask(__name__)
searchReddit = redditSearch()

titleOutputList = []
scoreOutputList = []
idOutputList = []
urlOutputList = []
authorOutputList = []
commentAuthorList = []
commentBodyList = []

@app.route("/")
def testtemp():
    return render_template("testtemp.html")

@app.route('/contact') #made a search bar that we can use in the future
def contact():
    return render_template("contact.html")

@app.route('/comments', methods = ['POST']) #made a search bar that we can use in the future
def comment():
    del searchReddit.submissionPostBodyList[:]
    del searchReddit.submissionPostAuthorsList[:]
    postNum = request.form['postIDNum']
    searchReddit.read_comments(postNum)
    commentAuthorList = searchReddit.submissionPostAuthorsList[:]
    commentBodyList = searchReddit.submissionPostBodyList[:]
    tableSize = len(commentAuthorList)
    return render_template("comments.html", commentAuthorList = commentAuthorList[:], commentBodyList = commentBodyList[:], tableSize =  tableSize)

@app.route('/results', methods=['POST'])
def my_form_post():
    searchReddit.clear_lists()
    text = request.form['text']
    postCount = int(request.form['count'])
    radioChoice = int(request.form['userChoice'])
    searchReddit.sub_data(text, radioChoice, postCount)

    titleOutputList = searchReddit.submissionTitleList[:]
    scoreOutputList = searchReddit.submissionScoreList[:]
    idOutputList = searchReddit.submissionIDList[:]
    urlOutputList = searchReddit.submissionURLList[:]
    authorOutputList = searchReddit.submissionAuthorList[:]
    tableRows = len(titleOutputList)
    
    return render_template(
    "index.html",
    titleOutputList = titleOutputList[:],
    scoreOutputList = scoreOutputList[:],
    idOutputList = idOutputList[:],
    urlOutputList = urlOutputList[:],
    authorOutputList = authorOutputList[:],
    tableRows = tableRows
    )

app.run(
        port = int(os.getenv("PORT", 8080)),
        host = os.getenv("IP","0.0.0.0")
    )
