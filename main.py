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

    i_chr = arg['chr']
    i_beg = arg['beg']
    i_str = arg['str']

    # Expect JSON argument like this python command.
    # Example:
    # main.search({'chrnum':'chr','win_beg':'beg','strand':'str'})
    # That equates to this URL.
    # 'https://mpss.udel.edu/web/php/pages/PAinfo.php?SITE=at_sRNA&format=json&chrnum=6&win_beg=10&strand=w&list=phasing_window'
    # The remote service takes additional parameters that we will pass from input args
    pw_url = ('http://mpss.udel.edu/web/php/pages/PAinfo.php?SITE=at_sRNA'
           '&chrnum={chr}&win_beg={beg}&strand={str}&format=json&list=phasing_window'
           .format(chr=i_chr, beg=i_beg, str=i_str))

    print pw_url
    rqst = requests.get(pw_url)

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
    pa_url = ('http://mpss.udel.edu/web/php/pages/PAinfo.php?SITE=at_sRNA'
           '&chrnum={chr}&win_beg={beg}&strand={str}&format=json&list=phasing_analysis'
           .format(chr=i_chr, beg=i_beg, str=i_str))

    print pa_url
    rqst = requests.get(pa_url)

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

    final_payload_json = {'phasing_window_url': pw_url,
			'phasing_window': pw_payload['phasing_window'], 
			'phasing_analysis_url': pa_url,
			'phasing_analysis': pa_payload['phasing_analysis']}

    payload = json.dumps(final_payload_json)
    print payload
    print '---'
