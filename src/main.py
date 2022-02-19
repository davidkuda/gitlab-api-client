# Author: David Kuda
# Creation Date: 1. October 2021

import os

from gitlab_connection.connection_creator import ConnectionCreator


GITLAB_ACCESS_TOKEN = os.environ.get("GITLAB_ACCESS_TOKEN")
GITLAB_API_ENDPOINT = os.environ.get("GITLAB_API_ENDPOINT")


def main():
    connection_creator = ConnectionCreator(
        gitlab_access_token=GITLAB_ACCESS_TOKEN,
        api_base_url=GITLAB_API_ENDPOINT,
    )

    # Define the project of which you want to copy the existing vars
    src_project_id = 306
    src_project = connection_creator.create_project_connection(src_project_id)
    src_project_vars = src_project.get_project_vars()
    
    # Define the projects of which you want to set the variables
    dest_project_id = 3011
    dest_project = connection_creator.create_project_connection(dest_project_id)
    dest_project.copy_vars_from_other_project(src_project_vars)


if __name__ == '__main__':
    main()
