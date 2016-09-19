#!/usr/bin/env python
import json
from functools import partial

import requests


class Log(object):

    def __init__(self):
        self.headers = {'content-type': 'application/json'}

        self.debug_method = partial(self._log, level='debug')
        self.error_method = partial(self._log, level='error')

    def _log(self, app_identifier, msg, level):
        payload = {'app_identifier': str(app_identifier),
                   'log_level': level,
                   'message': msg}
        try:
            requests.post(
                url='http://localhost:3332',
                data=json.dumps(payload),
                headers=self.headers,
                auth=('myuser', 'mypassword'))
        except requests.exceptions.ConnectionError:
            print('Elastic search is down: ' + str(payload))

    def debug(self, app_identifier, msg):
        """Debug function to send data with loglevel debug."""
        self.debug_method(app_identifier, msg)

    def error(self, app_identifier, msg):
        """Error function to send data with loglevel error."""
        self.error_method(app_identifier, msg)


log = Log()
log.debug(app_identifier='MyApplication1', msg='its a debug message')
log.error(app_identifier='MyApplication2', msg='its an error message')
