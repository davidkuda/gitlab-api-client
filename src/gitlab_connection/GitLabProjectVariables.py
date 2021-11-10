from .GitLabConnection import GitLabConnection


class GitLabProjectVariables(GitLabConnection):
    def __init__(self, gitlab_access_token, api_base_url, project_num) -> None:
        super().__init__(gitlab_access_token, api_base_url)
        self.project_num = project_num

    def get_project_vars(self):
        endpoint = f'/projects/{self.project_num}/variables'
        return self._get(endpoint)
    
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
                self._create_project_variable(var_key, var_value)

            print(f'Setting the variable "{var_key}".')

    def _check_if_var_is_taken(self, var_key: str):
        existing_variables = self.get_project_vars()
        existing_var_keys = [v['key'] for v in existing_variables]
        if var_key in existing_var_keys:
            return True

    def _create_project_variable(self, var_key: str, var_value: str):
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
