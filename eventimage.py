#!/usr/bin/env python3

from flask import Flask, request, make_response
from flask_restful import Resource, Api
from template import svg_tmpl

app = Flask(__name__)
api = Api(app)

class EventImage(Resource):
    def get(self):
        (date, time) = request.args.get('dt').split(' ')
        svg = svg_tmpl % (time, date)

        resp = make_response(svg, 201)
        resp.mimetype = 'image/svg+xml'
        return resp

api.add_resource(EventImage, '/getimage')

if __name__ == '__main__':
    app.run()
