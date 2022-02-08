# Author: David Kuda
# Creation Date: 10. November 2021

from .gitlab_connection import GitLabConnection
from .gitlab_project import GitLabProject
from .gitlab_group import GitLabGroup
from .project_finder import ProjectFinder


class ConnectionCreator(GitLabConnection):
    def __init__(self, gitlab_access_token, api_base_url) -> None:
        super().__init__(gitlab_access_token, api_base_url)
    
    def create_project_connection(self, project_id: int):
        return GitLabProject(
            self.gitlab_access_token,
            self.api_base_url,
            project_id)
    
    def create_group_connection(self, group_id: int):
        return GitLabGroup(
            self.gitlab_access_token,
            self.api_base_url,
            group_id)

    def create_project_finder(self):
        return ProjectFinder(
            self.gitlab_access_token,
            self.api_base_url)
