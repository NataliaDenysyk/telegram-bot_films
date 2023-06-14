from typing import Dict
import requests


def _make_response(method: str, url: str, headers: Dict,
                   params: Dict, timeout: int = 5, success=200):
    response = requests.request(
        method,
        url,
        headers=headers,
        params=params,
        timeout=timeout
    )

    status_code = response.status_code

    if status_code == success:
        return response

    return status_code


def _get_querystring(method: str, url: str, headers: Dict, params: Dict,
                     genre: str = 'comedy', start_year: str = 1998,
                     end_year: str = 2020,
                     timeout: int = 5, func=_make_response):
    params['genre'] = genre
    params['start_year'] = start_year
    params['end_year'] = end_year

    response = func(method, url, headers=headers, params=params, timeout=timeout)

    return response


class SiteApiInterface():
    """"
    Отправляет запрос на сайт
    """
    @staticmethod
    def get_params():
        return _get_querystring


with open('readme.md', 'w', encoding='utf-8') as file:
    result = '\nclass SiteApiInterface' + SiteApiInterface.__doc__
    file.write(result)


if __name__ == '__main__':
    _make_response()
    _get_querystring()
    SiteApiInterface()



