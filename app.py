from flask import Flask, request, render_template

import text_classifier

def create_app():
    """
    App Creation factor
    :return: flask app ready to be deployed
    """
    app = Flask(__name__)

    logprior, loglikelihood = load_model()

    @app.route('/', methods=['GET'])
    def main():
        return render_template('index.html')

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/predict', methods=['POST'])
    def predict_review():
        # Get the review from the form data
        review_text = request.form.get('review')

        prediction = text_classifier.naive_bayes_predict(
            review_text, logprior, loglikelihood, categoricalLabel=True)

        return render_template('index.html', prediction=prediction)

    return app


def load_model():
    """
    Load model and return the values needed nicely
    :return: logprior and loglikelihood
    """
    model = text_classifier.load_model("movie_sentiment_model_parameters.json")
    logprior = model['logprior']
    loglikelihood = model['loglikelihood']
    return logprior, loglikelihood
