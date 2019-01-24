# -*- endcoding=utf-8 -*-
import subprocess
import sched
import time
import json
import logging

import daemon

# create logger with 'spam_application'
logger = logging.getLogger('timer')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('./run.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)


def period_task(sc, delay, priority, cmd_args):
    # do you stuff
    logger.info("do task...")
    subprocess.run(cmd_args)
    logger.info("do task end...")
    sc.enter(delay, priority, period_task, (sc, delay, priority, cmd_args,))


def load_task(s):
    with open('task.json') as f:
        json_data = json.load(f)
    for key, item in json_data.items():
        cmd_args = item['command'].split(" ")
        delay = item['delay']
        priority = item['priority']
        if item['is_period']:
            s.enter(delay, priority, period_task, (s, delay, priority, cmd_args,))


with daemon.DaemonContext():
    s = sched.scheduler(time.time, time.sleep)
    load_task(s)
    s.run()
