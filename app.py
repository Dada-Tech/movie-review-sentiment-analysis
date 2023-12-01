from flask import Flask, request, jsonify, render_template

import text_classifier


def load_model():
    model = text_classifier.load_model("movie_sentiment_model_parameters.json")
    logprior = model['logprior']
    loglikelihood = model['loglikelihood']
    return logprior, loglikelihood


def create_app():
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


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
