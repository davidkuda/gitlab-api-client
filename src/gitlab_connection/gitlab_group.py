from typing import List
from pprint import pprint

from .gitlab_connection import GitLabConnection


class GitLabGroup(GitLabConnection):
    def __init__(self, gitlab_access_token, api_base_url, group_id) -> None:
        super().__init__(gitlab_access_token, api_base_url)
        self.group_id = group_id
        self._group_data = self._get(f"/groups/{group_id}/")
        self.group_name = self._group_data["name"]
        self.full_path = self._group_data["full_path"]
    
    def get_group_vars(self) -> List[dict]:
        endpoint = f'/groups/{self.group_id}/variables'
        return self._get(endpoint)
