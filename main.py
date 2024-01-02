from textblob import TextBlob
from dataclasses import dataclass


@dataclass
class Mood:
    emoji: str
    sentiment: float


def get_mood(input_text: str, *, sensitivity: float) -> Mood:
    polarity: float = TextBlob(input_text).sentiment.polarity

    friendly_threshold : float = sensitivity
    hostile_threshole: float = -sensitivity
    if polarity>=friendly_threshold:
        return Mood("Good", polarity)
    elif polarity <=hostile_threshole:
        return Mood("angry",polarity)
    else:
        return Mood("ok",polarity)

def run_bot():
    print("Enter some text to get the sentiment")
    while True:
        user_input : str = input()
        mood: Mood = get_mood(user_input,sensitivity= 0.6)
        print(f'Bot: {mood.sentiment}')

if __name__ == '__main__':
    run_bot()

