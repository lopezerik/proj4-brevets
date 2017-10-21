"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request, flash
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")

    km = request.args.get('km', 9999, type=float)
    if(km == 9999):
        result = {"open": "", "close": ""}
        return flask.jsonify(result=result)

    brevet = request.args.get('brev', 200, type=int)
    start_date = request.args.get('dat', '1970-01-01 00:00', type=str)
    arr_date = arrow.get(start_date, 'YYYY-MM-DD HH:mm').isoformat()

    app.logger.debug("km={}".format(km))
    app.logger.debug("brevet={}".format(brevet))
    app.logger.debug("start_date={}".format(start_date))
    app.logger.debug("arr_date={}".format(arr_date))
    app.logger.debug("request.args: {}".format(request.args))
    open_time = acp_times.open_time(km, brevet, arr_date)
    close_time = acp_times.close_time(km, brevet, arr_date)
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)

@app.route("/_shift_one")
def _shift_one():
    day = request.args.get('day')
    arr_date = arrow.get(day)
    arr_date = arr_date.shift(hours=1).isoformat()
    result = {"close": arr_date}
    return flask.jsonify(result=result)

#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
