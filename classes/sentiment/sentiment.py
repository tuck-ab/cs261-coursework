from textblob import TextBlob
import math
import random

class Sentiment:

    def __init__(self,sentiment_sum,sentiment_sqr_sum, num_responses,average,last_sentiment,eventID=""):
        self.sentiment_sum = sentiment_sum
        self.sentiment_sqr_sum = sentiment_sqr_sum
        self.num_responses = num_responses
        self.average = average
        self.last_sentiment = last_sentiment
        
    def calculateSentiment(self, string): 
        textToAnalyse = TextBlob(string)
        self.last_sentiment = textToAnalyse.sentiment.polarity

    def getSentiment(self):
        return self.last_sentiment

    def setSentiment(self, string):
        self.calculateSentiment(string)

# Simply returns the current average sentiment of the event    
    def get_AverageSentiment(self):
        return self.average

# We plan to increment the response counter prior to calculating the new average
# The setAverage method updates the average sentiment value everytime a new Sentiment value is entered
# which is accessed via the lastSentiment variable 
    def set_AverageSentiment(self):
        return self.calculate_average(self.sentiment_sum, self.sentiment_sqr_sum, self.num_responses, self.last_sentiment)

# a value is a outlier if it's more than 2 standard deviations from the mean of the current data (extreme data unrepresentative)
    def calculate_average(self, sum, sqr_sum, n, single_sentiment):
        # test(t)_ is temporary values which will only be returned if the single_sentiment is NOT an outlier
        t_sum = sum + single_sentiment
        t_sqr_sum = sqr_sum + single_sentiment ** 2
        t_n = n + 1
        t_mean = t_sum / t_n
        sd = math.sqrt(t_sqr_sum / t_n - t_mean ** 2)  # standard_deviation calculation
        UB = t_mean + 2 * sd  # upper_outlier_indicator
        LB = t_mean - 2 * sd  # lower_outlier_indicator
        if single_sentiment > UB or single_sentiment < LB:
            print(str(round(single_sentiment, 3)) + " is a outlier")
            return sum / n, sum, sqr_sum, n
        else:
            print(str(round(single_sentiment, 3)) + " is a inlier")
            self.sentiment_sum = t_sum
            self.sentiment_sqr_sum = t_sqr_sum
            self.num_responses = t_n
            self.average = t_mean
            return t_mean, t_sum, t_sqr_sum, t_n

    def calculate_percentage(self, average):
        percent = (average + 1) * 50
        return round(percent, 1)

    def get_percentage(self):
        return self.calculate_percentage(self.average)


s = Sentiment(0,0,0,0,0)
s.setSentiment("The platform provides universal access to the world's best education, partnering with top universities and organizations to offer courses online.")
print(s.getSentiment())

print("Values after first sentiment: ", s.set_AverageSentiment())
print("AverAGE", s.get_AverageSentiment())  
print("Percentage: ", s.get_percentage())

s.setSentiment("wonderful")
print(s.getSentiment())
print("Values after second sentiment: ", s.set_AverageSentiment())
print("AverAGE", s.get_AverageSentiment())
print("Percentage: ", s.get_percentage())

