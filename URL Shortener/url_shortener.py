import random 
import json
from flask import Flask, render_template, request, redirect 

app = Flask(__name__)
char_pool = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
file = 'links.json'

# Initial Data Load
try:
    with open(file) as f:
        url_db = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    url_db = {}

@app.route('/', methods=['GET', 'POST']) # Fixed the 'map' typo here
def index():
    new_short_url = None 

    if request.method == 'POST':
        long_url = request.form.get('url_input')

        # Logic to ensure the URL starts with http so the redirect works
        if not long_url.startswith(('http://', 'https://')):
            long_url = 'https://' + long_url

        while True:
            url_short = ""
            for i in range(6):
                url_short += random.choice(char_pool)

            if url_short not in url_db:
                url_db[url_short] = long_url

                with open(file, 'w') as f:
                    json.dump(url_db, f)

                new_short_url = f"http://127.0.0.1:5000/{url_short}"
                break

    return render_template('index.html', database=url_db, result=new_short_url)

@app.route('/<short_code>')
def url_redirect(short_code):
    if short_code in url_db:
        return redirect(url_db[short_code])
    else:
        return "<h1>ERROR: Short code not found</h1>", 404

if __name__ == "__main__":
    app.run(debug=True)