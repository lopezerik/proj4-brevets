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
    print(max_dist)
    correct = "2017-01-01T05:53:00+00:00"
    print(max_dist == correct)
    assert (max_dist == correct)

