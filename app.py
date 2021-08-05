from datetime import datetime

from flask import Flask
    
app = Flask(__name__)

@app.route("/")
def home():
    date = datetime.now()
    return str(date)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)