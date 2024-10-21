from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/fetch-section', methods=['GET'])
def fetch_section():
    try:
        # Fetch the HTML content from the external website
        response = requests.get('https://join.hashtag.dance/ticket')
        response.raise_for_status()  # Check for request errors
        html_content = response.text

        # Parse the HTML and extract the desired section
        soup = BeautifulSoup(html_content, 'html.parser')
        section = soup.find(id='card-3')

        if section:
            return section.prettify()
        else:
            return 'Section not found', 404

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
