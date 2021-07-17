from flask import Flask
import json
from flickrapi import FlickrAPI



api_key = u'3b95b86ce2ee0cb6babbe9b00ce7d341'
api_secret = u'fdc27a36bc400666'


app = Flask(__name__)
flickr = FlickrAPI(api_key, api_secret, format='parsed-json')


@app.route('/', methods=['GET'])
def home():
        return 'http://127.0.0.1:5000/popular'


@app.route('/popular', methods=['GET'])
def popular():
        photos = flickr.photos.getPopular(user_id='73509078@N00',per_page = 50)
        return json.dumps(photos, indent=4)


if __name__ =="__main__":
        PORT = 5000
        app.run(port=PORT)

