"""Flask server for emotion detection web application."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    """Endpoint to analyze emotions in the provided text.
    Returns formatted string with emotion scores and dominant emotion,
    or error message for invalid input.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    # Format the output as requested
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    output = (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']}, and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return output

@app.route("/")
def render_index_page():
    """Renders the main HTML index page for the web application."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
