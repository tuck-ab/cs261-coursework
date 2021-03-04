import math
import random

class EmojiSentiment :

    def __init__(self, emoji_sum, emoji_sqr_sum, num_responses, average, last_emoji_sentiment, eventID="") :
        self.emoji_sum = emoji_sum
        self.emoji_sqr_sum = emoji_sqr_sum
        self.num_responses = num_responses
        self.average = average
        self.last_emoji = last_emoji


    def getEmojiSentiment(self):
        return self.last_emoji_sentiment

    def setEmojiSentiment(self, num):
        self.last_emoji_sentiment = num

    def get_AverageEmojiSentiment(self):
        return self.average

    def set_AverageEmojiSentiment(self):
        return self.calculate_average(self.emoji_sum, self.emoji_sqr_sum, self.num_responses, self.last_emoji_sentiment)


# a value is a outlier if it's more than 2 standard deviations from the mean of the current data (extreme data unrepresentative)
    def calculate_average(self, emoji_sum, emoji_sqr_sum, num_responses, last_emoji_sentiment):
        # test(t)_ is temporary values which will only be returned if the single_sentiment is NOT an outlier
        t_sum = emoji_sum + last_emoji_sentiment
        t_sqr_sum = emoji_sqr_sum + last_emoji_sentiment ** 2
        t_n = num_responses + 1
        t_mean = t_sum / t_n
        sd = math.sqrt(t_sqr_sum / t_n - t_mean ** 2)  # standard_deviation calculation
        UB = t_mean + 2 * sd  # upper_outlier_indicator
        LB = t_mean - 2 * sd  # lower_outlier_indicator
        if last_emoji_sentiment > UB or last_emoji_sentiment < LB:
            print(str(round(last_emoji_sentiment, 3)) + " is a outlier")
            return emoji_sum / num_responses, emoji_sum, emoji_sqr_sum, num_responses
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
