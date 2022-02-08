# Author: David Kuda
# Creation Date: 10. November 2021

from pprint import pprint
import json

from .gitlab_connection import GitLabConnection


class ProjectFinder(GitLabConnection):
    def __init__(self, gitlab_access_token, api_base_url) -> None:
        super().__init__(gitlab_access_token, api_base_url)

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
        params = {
            "per_page": 100,
            "search": name,
        }
        groups = self._get('/groups', params)
        group_names_and_id = []
        pprint(groups[0].keys())
        pprint(groups[3])
        for group in groups:
            group_names_and_id.append({
                    "group_id": group.get('id'),
                    "group_name": group.get('name'),
                    "full_path": group.get('full_path'),
                })
        pprint(group_names_and_id)

    def search_project(self, name: str):
        response = self._get(f'/search?scope=projects&search={name}')
        print(json.dumps(response, indent=2))
        return response
