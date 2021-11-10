# Author: David Kuda
# Creation Date: 1. October 2021
#
# Description:
#
# Interacts with the GitLab api to create new variables
# that can be used in gitlab ci.
#
# Documentation:
#
# https://docs.gitlab.com/ee/api/project_level_variables.html
#

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
        self.check_authentication()

    def check_authentication(self):
        response = self._get('/version')
        if response.get('error') == 'invalid_token':
            print(response.get('error_description'))
            raise UnsuccessfulAuthentication(response.get('error_description'))
        else:
            return True

    def _get(self, api_endpoint: str):
        # Two examples:
        # projects = gitlab_client.get('/projects')
        # groups = gitlab_client.get('/groups')
        url = self.api_base_url + api_endpoint
        return requests.get(url=url, headers=self.headers).json()

    def _post(self, api_endpoint: str, body):
        url = self.api_base_url + api_endpoint
        print(url)
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

    def list_groups(self):
        groups = self._get('/groups')
        group_names_and_id = []
        # pprint(groups[0].keys())
        for group in groups:
            group_names_and_id.append({
                    "group_id": group.get('id'),
                    "group_name": group.get('name')
                })
        pprint(group_names_and_id)

    def list_projects_of_group(self, group_num):
        projects_of_group = self._get(f'/groups/{group_num}/projects?per_page=100')
        print(len(projects_of_group))
        project_names_and_ids = []
        for project in projects_of_group:
            project_names_and_ids.append({
                "project_id": project.get('id'),
                "project_name": project.get('name')
            })
        pprint(project_names_and_ids)

    def search_group(self, name: str):
        # Does not work, API has no search scope for group.
        response = self._get(f'/search?scope=groups&search={name}')
        pprint(response)

    def search_project(self, name: str):
        response = self._get(f'/search?scope=projects&search={name}')
        pprint(response)


if __name__ == '__main__':
    pass
