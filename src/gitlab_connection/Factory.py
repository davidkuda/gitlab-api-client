from .GitLabConnection import GitLabConnection
from .GitLabProjectVariables import GitLabProjectVariables


class ConnectionCreator(GitLabConnection):
    def __init__(self, gitlab_access_token, api_base_url) -> None:
        super().__init__(gitlab_access_token, api_base_url)
    
    def create_project_vars_obj(self, project_num: int):
        return GitLabProjectVariables(
            self.gitlab_access_token,
            self.api_base_url,
            project_num
        )
