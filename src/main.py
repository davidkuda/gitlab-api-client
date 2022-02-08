# Author: David Kuda
# Creation Date: 1. October 2021

import os
from pprint import pprint

from gitlab_connection.connection_creator import ConnectionCreator


def main():

    connection_creator = connect_to_at()

    # Define the project of which you want to copy the existing vars
    src_repository = 841

    src_repository_vars_obj = connection_creator.create_project_vars_obj(src_repository)
    src_repository_vars = src_repository_vars_obj.get_project_vars()
    
    # Define the projects of which you want to set the variables
    dest_repository = 2782
    dest_repository = connection_creator.create_project_vars_obj(dest_repository)
    dest_repository.copy_vars_from_other_project(src_repository_vars)

def connect_to_at():
    # Make sure to have your personal GitLab Access Token as env var
    GITLAB_ACCESS_TOKEN = os.environ.get('GITLAB_PERSONAL_API_TOKEN')
    
    # Create a GitLab Connection
    connection_creator = ConnectionCreator(
        gitlab_access_token=GITLAB_ACCESS_TOKEN,
        api_base_url='https://gitlab.alexanderthamm.com/api/v4'
    )
    return connection_creator


def search_project_num():
    gitlab_connection = connect_to_at()
    project_finder = gitlab_connection.create_project_finder()
    project_finder.list_groups()
    project_finder.list_projects_of_group(852)
    project_finder.search_project('ecr-images')


if __name__ == '__main__':
    main()
