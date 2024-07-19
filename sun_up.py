import datetime
from suntime import Sun, SunTimeException
import time
import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action="store_true", default=False, help="Debug")

LATITUDE = 51.38
LONGITUDE = 0.24

START_TIME = 23
END_TIME = 4

SUN = Sun(LATITUDE, LONGITUDE)

logger = logging.getLogger(__name__)

if parser.parse_args().verbose:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

# logger.setLevel(logging.INFO)

while True:

    now = datetime.datetime.now().replace(microsecond=0)
    # Get today's sunrise and sunset in Local time
    abd_sr = SUN.get_sunrise_time(now).replace(microsecond=0)
    abd_ss = SUN.get_sunset_time(now).replace(microsecond=0)

    abd_ss += datetime.timedelta(days=1)

    logger.debug('Today in Worcester Park the sun rose at {} and set at {} Local time'.format(abd_sr.strftime('%H:%M'), abd_ss.strftime('%H:%M')))
    logger.debug('Current time {} Local London time'.format(now.strftime('%H:%M')))
    if (abd_sr.replace(tzinfo=None) < now < abd_ss.replace(tzinfo=None)) or (END_TIME <= int(datetime.datetime.now().strftime("%H")) >= START_TIME):
        logger.info('The sun is up')
        # put white LED off when sun is up


    elif now > abd_ss.replace(tzinfo=None) or now < abd_sr.replace(tzinfo=None) :
        logger.info('The sun is down')
        # put white LED on when sun is up

    time.sleep(2)