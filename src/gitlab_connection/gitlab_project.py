# Author: David Kuda
# Creation Date: 10. November 2021
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

from typing import List

from .gitlab_connection import GitLabConnection


class GitLabProject(GitLabConnection):
    def __init__(self, gitlab_access_token, api_base_url, project_num) -> None:
        super().__init__(gitlab_access_token, api_base_url)
        self.project_num = project_num

    def get_project_vars(self) -> List[dict]:
        endpoint = f'/projects/{self.project_num}/variables'
        return self._get(endpoint)

    def delete_all_vars(self):
        vars = self.get_project_vars()

        if len(vars) == 0:
            print(f'No vars exist in this project (project num: {self.project_num})')
            return

        for var in vars:
            var_key = print(var['key'])
            print(f'Deleting {var_key}')
            r = self._delete_var(var['key'])
            print(r)

    def _delete_var(self, var_name: str):
        url = f'/projects/{self.project_num}/variables/{var_name}'
        return self._request('DELETE', url)
    
    def set_project_variables(self, variables: dict):
        """Sets the variables of the project according to the passed arg.
        
        Args:
            variables (Dict[str: str]):
                This method will set the variables of this GitLab project
                to the variables passed as this argument.
                
                Make sure to use this format:
                
                variables = {
                    "variable_key": "variable_value",
                    "Data": "Dave",
                    "Dater": "Daver",
                    "Daterr": "Daverr"
                }
        """
        for var_key, var_value in variables.items():
            var_key = var_key.upper()
            
            is_taken = self._check_if_var_is_taken(var_key)

            if is_taken:
                self._update_project_variable(var_key, var_value)
            else:
                self._create_project_variable_with_defaults(var_key, var_value)

            print(f'Setting the variable "{var_key}".')

    def copy_vars_from_other_project(self, vars: List[dict]):
        for var in vars:
            print(f'Copying var "{var["key"]}"')
            self._create_project_variable(var)

    def _check_if_var_is_taken(self, var_key: str):
        existing_variables = self.get_project_vars()
        existing_var_keys = [v['key'] for v in existing_variables]
        if var_key in existing_var_keys:
            return True

    def _create_project_variable_with_defaults(self, var_key: str, var_value: str):
        url = f'/projects/{self.project_num}/variables'
        var_key = var_key.upper()

        post_body = {
            "variable_type": "env_var",
            "key": var_key,
            "value": var_value,
            "protected": True,
            "masked": False,
            "environment_scope": "*"
        }

        return self._post(url, post_body)

    def _create_project_variable(self, post_body: dict):
        url = f'/projects/{self.project_num}/variables'
        return self._post(url, post_body)

    def _update_project_variable(self, var_key: str, var_value: str):
        var_key = var_key.upper()
        endpoint = f'/projects/{self.project_num}/variables/{var_key}'

        body = {
            "variable_type": "env_var",
            "key": var_key,
            "value": var_value,
            "protected": True,
            "masked": False,
            "environment_scope": "*"
        }
        return self._put(endpoint, body)


if __name__ == '__main__':
    pass
