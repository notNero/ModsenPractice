from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = 'your API_KEY'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        return jsonify({
            'status_code': response.status_code,
            'data': response.json()
        })
    else:
        return handle_api_error(response)


def handle_api_error(response):
    if response.status_code == 400:
        message = 'Bad Request'
    elif response.status_code == 401:
        message = 'Unauthorized'
    elif response.status_code == 403:
        message = 'Forbidden'
    elif response.status_code == 404:
        message = 'Not Found'
    elif response.status_code == 500:
        message = 'Internal Server Error'
    else:
        message = 'An unexpected error occurred'

    return jsonify({
        'status_code': response.status_code,
        'error': message
    }), response.status_code


@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request'}), 400


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({'error': 'Unauthorized'}), 401


@app.errorhandler(403)
def forbidden(error):
    return jsonify({'error': 'Forbidden'}), 403


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500


if __name__ == '__main__':
    app.run(debug=True)
