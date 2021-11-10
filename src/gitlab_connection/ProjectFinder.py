# Author: David Kuda
# Creation Date: 10. November 2021

from pprint import pprint

from .GitLabConnection import GitLabConnection


class ProjectFinder(GitLabConnection):
    def __init__(self, gitlab_access_token, api_base_url) -> None:
        super().__init__(gitlab_access_token, api_base_url)

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
