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
        
    def getSentimentCount(self):
        return self.num_responses

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
        if single_sentiment > UB:
            print(str(round(single_sentiment, 3)) + " is aN outlier")
            if UB > 0:
                percent_dif = (single_sentiment - UB)/UB  # how far away is the outlier, percent in decimal form
            elif UB < 0:
                percent_dif = (UB - single_sentiment)/UB  
            # if percent difference is less than 1, add outlier to the average, else outlier is too far from the average - remove it
            if percent_dif < 1:
                # calculate new sentiment value where outlier has less of an impact 
                new_sentiment_value = single_sentiment*(1-percent_dif) + (sum/n)*percent_dif # only worth percent dif
                # that % dif will be the % of the original sum that we use 
                t_sum = sum + new_sentiment_value
                t_sqr_sum = sqr_sum + new_sentiment_value ** 2
                t_n = n + 1
                t_mean = t_sum / t_n
            else: 
                # keep the original values (without adding last_sentiment)
                t_sum = sum
                t_sqr_sum = sqr_sum
                t_mean = sum / n
        elif single_sentiment < LB:
            print(str(round(single_sentiment, 3)) + " is aN outlier")
            if LB < 0:
                percent_dif = (single_sentiment - LB)/LB # how far away is the outlier, percent in decimal form
            elif LB > 0:
                percent_dif = (LB - single_sentiment)/LB 
             # if percent difference is less than 1, add outlier to the average, else outlier is too far from the average - remove it
            if percent_dif < 1:
                new_sentiment_value = single_sentiment*(1-percent_dif) + (sum/n)*percent_dif
                t_sum = sum + new_sentiment_value
                t_sqr_sum = sqr_sum + new_sentiment_value ** 2
                t_n = n + 1
                t_mean = t_sum / t_n
            else: 
                t_sum = sum
                t_sqr_sum = sqr_sum
                t_mean = sum / n
        else:
            print(str(round(single_sentiment, 3)) + " is aN inlier")
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

