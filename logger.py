from flask import Flask, request, make_response
import datetime

app = Flask(__name__)
app.debug = True


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        app.logger.info(request.values)
        event = request.values.get('event')
        if event == 'newCall':
            resp = make_response('<?xml version="1.0" encoding="UTF-8"?><Response/>')
            resp.headers['Content-Type'] = 'application/xml'
            return resp

    return "This was not a post request"


if __name__ == "__main__":
    app.run()
