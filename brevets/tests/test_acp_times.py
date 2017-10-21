'''
Nose tests for acp_times.py

'''

from acp_times import open_time, close_time

import nose
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                           level=logging.WARNING)
log = logging.getLogger(__name__)


def test_200_over_brevet_open():
    max_dist = open_time(220, 200, '2017-01-01 00:00')
    correct = '2017-01-01T05:53:00+00:00'
    assert (max_dist == correct)

def test_200_over_brevet_close():
    max_dist = close_time(220, 200, '2017-01-01 00:00')
    correct = '2017-01-01T13:30:00+00:00'
    assert (max_dist == correct)

def test_200_at_brevet_open():
    equal_dist = open_time(200, 200, '2017-01-01 00:00')
    correct = '2017-01-01T05:53:00+00:00'
    assert (equal_dist == correct)

def test_200_at_brevet_close():
    equal_dist = close_time(200, 200, '2017-01-01 00:00')
    correct = '2017-01-01T13:30:00+00:00'
    assert (equal_dist == correct)

def test_200_under_brevet_open():
    under_dist = open_time(199, 200, '2017-01-01 00:00')
    correct = '2017-01-01T05:51:00+00:00'
    assert (under_dist == correct)

def test_200_under_brevet_close():
    under_dist = close_time(199, 200, '2017-01-01 00:00')
    correct = '2017-01-01T13:16:00+00:00'
    assert (under_dist == correct)

def test_300_over_brevet_close():
    max_dist = close_time(330, 300, '2017-01-01 00:00')
    correct = '2017-01-01T20:00:00+00:00'
    assert (max_dist == correct)

def test_400_over_brevet_close():
    max_dist = close_time(440, 400, '2017-01-01 00:00')
    correct = '2017-01-02T03:00:00+00:00'
    assert (max_dist == correct)

def test_600_over_brevet_open():
    max_dist = open_time(660, 600, '2017-01-01 00:00')
    correct = '2017-01-01T18:48:00+00:00'
    assert (max_dist == correct)

def test_600_over_brevet_close():
    max_dist = close_time(660, 600, '2017-01-01 00:00')
    correct = '2017-01-02T16:00:00+00:00'
    assert (max_dist == correct)

def test_1000_over_brevet_close():
    max_dist = close_time(1100, 1000, '2017-01-01 00:00')
    correct = '2017-01-04T03:00:00+00:00'
    assert (max_dist == correct)
