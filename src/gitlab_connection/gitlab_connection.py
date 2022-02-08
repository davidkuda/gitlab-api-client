# Author: David Kuda
# Creation Date: 1. October 2021

from pprint import pprint

import requests

from .custom_exceptions import UnsuccessfulAuthentication


class GitLabConnection:
    def __init__(self, gitlab_access_token, api_base_url) -> None:
        self.gitlab_access_token = gitlab_access_token
        self.api_base_url = api_base_url
        self.headers = {
            'PRIVATE-TOKEN': gitlab_access_token
        }
        self._check_authentication()

    def _check_authentication(self):
        response = self._get('/version')
        if (
            response.get('error') == 'invalid_token'
            or response.get('message') == '401 Unauthorized'
        ):
            print(response.get('error_description'))
            raise UnsuccessfulAuthentication("Failed Authentication to GitLab")
        else:
            return True

    def _get(self, api_endpoint: str, params=None):
        # Two examples:
        # projects = gitlab_client.get('/projects')
        # groups = gitlab_client.get('/groups')
        url = self.api_base_url + api_endpoint
        return requests.get(url=url, params=params, headers=self.headers).json()

    def _post(self, api_endpoint: str, body):
        url = self.api_base_url + api_endpoint
        return requests.post(url=url,
                             headers=self.headers,
                             json=body).json()

    def _put(self, api_endpoint: str, body):
        url = self.api_base_url + api_endpoint
        return requests.put(url=url,
                            headers=self.headers,
                            json=body).json()

    def _request(self, method: str, api_endpoint: str):
        url = self.api_base_url + api_endpoint
        return requests.request(method=method,
                                url=url,
                                headers=self.headers).status_code


if __name__ == '__main__':
    pass
