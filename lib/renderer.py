from kiwisolver import strength
import nltk
from nltk.tokenize import sent_tokenize
from lib.classifier import classifier
nltk.download('punkt')

MAX_INPUT = 512


def render_tone(content: str):
    out = ""

    paragraphs = content.split("\n")
    for paragraph in paragraphs:
        sentences = sent_tokenize(paragraph)

        for sentence in sentences:
            data = sentence[:MAX_INPUT]

            if (len(data) > 3):
                prediction = classifier(data)
                class_name = get_class_name(prediction)

                out += f'<span class="{class_name}">{data}</span> '
            else:
                out += f"<span>{data}</span> "

        out += "<br>"

    print("output", out)
    return '<div class="tonality">' + out + '</div>'


def get_class_name(prediction):
    score = prediction[0]["score"]
    strength = "low"
    if score > 0.80:
        strength = "high"
    elif score > 0.40:
        strength = "medium"

    label = prediction[0]["label"]
    tone = "casual"
    if label == "LABEL_1":
        tone = "formal"

    return f"{tone} {strength}"