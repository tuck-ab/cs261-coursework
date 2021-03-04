import math
import random

class EmojiSentiment :

    def __init__(self, emoji_sum, num_responses, average, last_emoji_sentiment, eventID="") :
        self.emoji_sum = emoji_sum
        self.num_responses = num_responses
        self.average = average
        self.last_emoji_sentiment = last_emoji_sentiment


    def getEmojiSentiment(self):
        return self.last_emoji_sentiment

    def setEmojiSentiment(self, num):
        self.last_emoji_sentiment = num

    def get_AverageEmojiSentiment(self):
        return self.average

    def set_AverageEmojiSentiment(self):
        self.calculate_average(self.emoji_sum, self.num_responses, self.last_emoji_sentiment)

# Simply calculates the average sentiment based on the previous sentiments.
# Note : we are NOT pruning the values to be included in the average at all. 
    def calculate_average(self, emoji_sum, num_responses, last_emoji_sentiment):
        self.emoji_sum += last_emoji_sentiment
        self.num_responses += 1
        self.average = self.emoji_sum / self.num_responses


    def calculate_percentage(self, average):
        percent = (average + 1) * 50
        return round(percent, 1)

    def get_percentage(self):
        return self.calculate_percentage(self.average)
