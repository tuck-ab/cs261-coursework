import math
import random

class EmojiSentiment:

    def __init__(self, emoji_sum, num_responses, average, last_emoji_sentiment, eventID="") :
        self.emoji_sum = emoji_sum
        self.num_responses = num_responses
        self.average = average
        self.last_emoji_sentiment = last_emoji_sentiment

    def get_emoji_sentiment(self):
        return self.last_emoji_sentiment

    def set_emoji_sentiment(self, num):
        self.last_emoji_sentiment = num

    def get_average_emoji_sentiment(self):
        return self.average

    def set_average_emoji_sentiment(self):
        self.calculate_average(self.emoji_sum, self.num_responses, self.last_emoji_sentiment)

    def calculate_average(self, emoji_sum, num_responses, last_emoji_sentiment):
        self.emoji_sum += last_emoji_sentiment
        self.num_responses += 1
        self.average = self.emoji_sum / self.num_responses

    def calculate_percentage(self, average):
        percent = (average + 1) * 50
        return round(percent, 1)

    def get_percentage(self):
        return self.calculate_percentage(self.average)
