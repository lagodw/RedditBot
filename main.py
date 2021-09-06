from flask import Flask
from flask import request
from flask import render_template
import requests

app = Flask(__name__)

@app.route("/", methods = ['POST', "GET"])
def home():

    if request.method == "POST":
        subreddit = request.form['subreddit']
        title = request.form['title']
        prompt = request.form['prompt']

        data = {'subreddit': subreddit,
                'title': title,
                'prompt': prompt
                }
        
        receive = requests.post("https://api.ubiops.com/v2.1/projects/redditbot/deployments/redditbot/versions/v1/requests", 
        json = data, 
        headers={'Authorization':'Token 6f01efb1d2ffe93703e952d604b03862fccdcdc9'})

        length_title = len(subreddit + '. ' + title + '. ')

        output = receive.json()['result']['thread'][length_title:]

    else:
        subreddit = 'askreddit'
        title = 'how does this seem?'
        prompt = 'its a test'
        output = 'blank'

    return render_template('index.html', subreddit = subreddit, title = title, prompt = prompt, output = output)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)