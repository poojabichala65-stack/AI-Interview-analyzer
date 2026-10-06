import re


def analyze_text(text):

    words = text.split()

    word_count = len(words)

    filler_words = [
        "um",
        "uh",
        "like",
        "actually",
        "basically"
    ]

    filler_count = 0

    lower_text = text.lower()

    for word in filler_words:

        filler_count += lower_text.count(word)

    if word_count > 0:

        filler_percentage = (
            filler_count / word_count
        ) * 100

    else:

        filler_percentage = 0

    return {
        "word_count": word_count,
        "filler_words": filler_count,
        "filler_percentage": round(
            filler_percentage,
            2
        )
    }