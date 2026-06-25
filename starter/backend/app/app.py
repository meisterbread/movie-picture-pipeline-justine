from flask import Flask
from movies import movies_api

app = Flask(__name__)
app.register_blueprint(movies_api.movies_api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)