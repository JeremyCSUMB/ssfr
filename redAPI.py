import praw

from keyforreddit import reddit




class redditSearch:
    def __init__(self):

        self.search_again = True
        self.postid = []
        self.submissionTitleList = []
        self.submissionScoreList = []
        self.submissionIDList = []
        self.submissionURLList = []
        self.submissionAuthorList = []
        self.submissionPostBodyList = []
        self.submissionPostAuthorsList = []
        # initalizes the lists and sets the bool to true
    def try_again(self):

        prompt_user = raw_input("Would you like search again (y/n) ")

        if (prompt_user == 'n'):
            self.search_again = False
            exit(0)
        else:
            self.search_again = True


    def sub_data(self, text, userChoice, count):
        sub = text
        posts = count
        choice = userChoice
        
        if (choice == 1):

            threadnumber=0

            for submission in reddit.subreddit(sub).controversial(limit=posts):
                subreddit = reddit.subreddit(sub)

            for submission in subreddit.controversial(limit=posts):
                self.submissionTitleList.append(submission.title)
                self.submissionScoreList.append(submission.score)
                self.submissionIDList.append(submission.id)
                self.submissionURLList.append(submission.url)
                self.submissionAuthorList.append(submission.author)
                threadnumber=threadnumber+1
                self.postid.append(submission.id)



        elif (choice == 2):

            threadnumber=0

            for submission in reddit.subreddit(sub).hot(limit=posts):
                subreddit = reddit.subreddit(sub)

            for submission in subreddit.hot(limit=posts):
                self.submissionTitleList.append(submission.title)
                self.submissionScoreList.append(submission.score)
                self.submissionIDList.append(submission.id)
                self.submissionURLList.append(submission.url)
                self.submissionAuthorList.append(submission.author)
                threadnumber=threadnumber+1
                self.postid.append(submission.id)


        elif (choice == 3):

            threadnumber=0

            for submission in reddit.subreddit(sub).new(limit=posts):
                subreddit = reddit.subreddit(sub)

            for submission in subreddit.new(limit=posts):
                self.submissionTitleList.append(submission.title)
                self.submissionScoreList.append(submission.score)
                self.submissionIDList.append(submission.id)
                self.submissionURLList.append(submission.url)
                self.submissionAuthorList.append(submission.author)
                threadnumber=threadnumber+1
                self.postid.append(submission.id)


        elif (choice == 4):

            threadnumber=0

            for submission in reddit.subreddit(sub).rising(limit=posts):
                subreddit = reddit.subreddit(sub)

            for submission in subreddit.rising(limit=posts):
                self.submissionTitleList.append(submission.title)
                self.submissionScoreList.append(submission.score)
                self.submissionIDList.append(submission.id)
                self.submissionURLList.append(submission.url)
                self.submissionAuthorList.append(submission.author)
                threadnumber=threadnumber+1
                self.postid.append(submission.id)


        elif (choice == 5):

            threadnumber=0

            for submission in reddit.subreddit(sub).top(limit=posts):
                subreddit = reddit.subreddit(sub)

            for submission in subreddit.top(limit=posts):
                self.submissionTitleList.append(submission.title)
                self.submissionScoreList.append(submission.score)
                self.submissionIDList.append(submission.id)
                self.submissionURLList.append(submission.url)
                self.submissionAuthorList.append(submission.author)
                threadnumber=threadnumber+1
                self.postid.append(submission.id)


    def read_comments(self, postIDNum):
        find = postIDNum
        submission = reddit.submission(id=find)
        submission.comment_sort = 'top'
        top_level_comments = list(submission.comments)
        for top_level_comment in submission.comments:
            self.submissionPostBodyList.append(top_level_comment.body)
            self.submissionPostAuthorsList.append(top_level_comment.author)


    def clear_lists(self):
        del self.postid[:]
        del self.submissionTitleList[:]
        del self.submissionScoreList[:]
        del self.submissionIDList[:]
        del self.submissionURLList[:]
        del self.submissionAuthorList[:]
        del self.submissionPostBodyList[:]
        del self.submissionPostAuthorsList[:]
