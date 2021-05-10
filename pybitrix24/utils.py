import json
import logging

import requests
from pybitrix24 import exceptions


logger = logging.getLogger(__name__)


def resolve_response(response):
    if response is None:
        logger.warning('resolve_response empty')
        result = {'error': 'Empty response!'}
    else:
        try:
            result = response.json()
        except json.decoder.JSONDecodeError:
            logger.exception(f'resolve_response JSONDecodeError {response.status_code} | {response.text}')
            result = {'error': response.status_code, 'error_description': response.text}
        except AttributeError:
            logger.exception('resolve_response AttributeError {} | {}'.format(response, type(response)))
            result = {'error': 'ReadError', 'error_description': response}

    return result


def http_build_query(params, topkey=''):
    from urllib.parse import quote

    if not isinstance(params, (int, bool)):
        if len(params) == 0:
            return ""

    result = ""

    # is a dictionary?
    if type(params) is dict:
        for key, value in params.items():
            newkey = quote(str(key))
            if topkey != '':
                newkey = str(topkey) + quote('[' + str(key) + ']')

            if type(value) is dict:
                res = http_build_query(value, newkey)
                result += res

            elif type(value) is list:
                i = 0
                for val in value:
                    res = http_build_query(val, newkey + quote('[' + str(i) + ']'))
                    result += res
                    i = i + 1

            # boolean should have special treatment as well
            elif type(value) is bool:
                res = newkey + "=" + quote(str(int(value))) + "&"
                result += res

            # assume string (integers and floats work well)
            else:
                res = newkey + "=" + quote(str(value)) + "&"
                result += res

    elif type(params) is list:
        if topkey != '':
            i = 0
            for val in params:
                res = http_build_query(val, topkey + quote('[' + str(i) + ']'))
                result += res
                i = i + 1

    elif type(params) is bool:
        res = topkey + "=" + quote(str(int(params))) + "&"
        result += res

    # assume string (integers and floats work well)
    else:
        res = topkey + "=" + quote(str(params)) + "&"
        result += res

    # remove the last '&'
    if result and (topkey == '') and (result[-1] == '&'):
        result = result[:-1]

    return result


def prepare_batch(calls):
    commands = {}
    for name, call in calls.items():
        if isinstance(call, str):
            command = call
        elif isinstance(call, tuple):
            try:
                command = '{}?{}'.format(call[0], http_build_query(call[1]))
            except IndexError:
                raise exceptions.BatchIndexError(name)
        elif isinstance(call, dict):
            try:
                command = '{}?{}'.format(call['method'], http_build_query(call['params']))
            except KeyError:
                raise exceptions.BatchKeyError(name)
        else:
            if isinstance(call, list):
                raise exceptions.BatchInstanceError(name, [tuple])
            else:
                raise exceptions.BatchInstanceError(name, [str, tuple, dict])
        commands[name] = command
    return commands


def bitrix_refresh_tokens(refresh_token, client_id, client_secret):
    oauth_url = 'https://oauth.bitrix.info/oauth/token/'
    r = {}
    result = {}

    try:
        # Make call to oauth server
        r = requests.post(
            oauth_url,
            params={
                'grant_type': 'refresh_token',
                'client_id': client_id,
                'client_secret': client_secret,
                'refresh_token': refresh_token
            }
        )
        res = json.loads(r.text)
        # Renew access tokens
        result['success'] = True
        result['access_token'] = res['access_token']
        result['refresh_token'] = res['refresh_token']
        logger.info(['Tokens', result['access_token'], result['refresh_token']])
        return result
    except (ValueError, KeyError):
        result['error'] = dict(error='Error on decode oauth response [' + r.text + ']')
        result['success'] = False
        return result