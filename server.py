# coding: utf-8

import json
import datetime
import numpy as np

from flask import Flask, render_template
from flask_cors import cross_origin


class NumpyDateEncoder(json.JSONEncoder):
    """ Decoder for the JSON"""
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


APP = Flask(__name__)


@APP.route('/points/')
@cross_origin()
def points():
    dates = np.arange('2016-12-16T00:00:00', '2016-12-16T00:01:00', dtype='datetime64[s]')

    size = len(dates)
    signal_1 = np.random.rand(size) * 10
    signal_2 = np.random.rand(size) * 10
    signal_3 = np.random.rand(size) * 10

    return json.dumps(
        {
            'dates': dates.tolist(),
            'signals': [
                {
                    'name': 'Signal 1',
                    'values': signal_1.tolist()
                },
                {
                    'name': 'Signal 2',
                    'values': signal_2.tolist()
                },
                {
                    'name': 'Signal 3',
                    'values':  signal_3.tolist()
                }
            ]

        }, cls=NumpyDateEncoder
    )

@APP.route('/')
def main():
    """ Retrieve app template """
    return render_template('index.html')

if __name__ == '__main__':
    APP.run(debug=True)
