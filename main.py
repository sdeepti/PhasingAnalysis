# file: main.py

import requests
import json

def list(arg):
    pass

def search(arg):

    # The requests object contains HTTP headers plus payload.
    # print r.headers
    # The remote service sets cookies. For now, we do not pass the cookie.
    # print headers['set-cookie']

    # The output may be ordered differently than the input.
    # In particular, the "sequence" tuple may be buried in the list.

    chrnum = arg['chrnum']
    win_beg = arg['win_beg']
    strand = arg['strand']

    # Expect JSON argument like this python command.
    # Example:
    # main.search({'chrnum':'chr','win_beg':'beg','strand':'str'})
    # That equates to this URL.
    # 'https://mpss.udel.edu/web/php/pages/PAinfo.php?SITE=at_sRNA&format=json&chrnum=6&win_beg=10&strand=w&list=phasing_window'
    # The remote service takes additional parameters that we will pass from input args
    url = ('http://mpss.udel.edu/web/php/pages/PAinfo.php?SITE=at_sRNA'
           '&chrnum={chr}&win_beg={beg}&strand={str}&format=json&list=phasing_window'
           .format(chr=chrnum, beg=win_beg, str=strand))

    print url
    rqst = requests.get(url)

    # If the response status is not 2xx, raise an exception with the
    # proper error message
    rqst.raise_for_status()

    # if we are here, it means the request was successful
    try:
        # try to decode the JSON response (it will succeed even if the
        # content type is not properly set, but the response is really
        # a JSON object)
        pw_payload = rqst.json()
    except ValueError:
        raise Exception('Could not decode the phasing_window JSON object')

    # Expect JSON argument like this python command.
    # Example:
    # main.search({'chrnum':'chr','win_beg':'beg','strand':'str'})
    # That equates to this URL.
    # 'https://mpss.udel.edu/web/php/pages/PAinfo.php?SITE=at_sRNA&format=json&chrnum=6&win_beg=10&strand=w&list=phasing_analysis'
    # The remote service takes additional parameters that we will pass from input args
    url = ('http://mpss.udel.edu/web/php/pages/PAinfo.php?SITE=at_sRNA'
           '&chrnum={chr}&win_beg={beg}&strand={str}&format=json&list=phasing_analysis'
           .format(chr=chrnum, beg=win_beg, str=strand))

    print url
    rqst = requests.get(url)

    # If the response status is not 2xx, raise an exception with the
    # proper error message
    rqst.raise_for_status()

    # if we are here, it means the request was successful
    try:
        # try to decode the JSON response (it will succeed even if the
        # content type is not properly set, but the response is really
        # a JSON object)
        pa_payload = rqst.json()
    except ValueError:
        raise Exception('Could not decode the phasing_window JSON object')

    final_payload_json = {'phasing_window': pw_payload['phasing_window'], 'phasing_analysis': pa_payload['phasing_analysis']}
    payload = json.dumps(final_payload_json)
    print payload
    print '---'
