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

import os
from pprint import pprint

from GitLabConnection import GitLabConnection
from utils import transform_vars_data_structure


def main():

    # Make sure to have your personal GitLab Access Token as env var
    GITLAB_ACCESS_TOKEN = os.environ.get('GITLAB_PERSONAL_API_TOKEN')

    # Create a GitLan Connection
    gitlab_connection = GitLabConnection(
        gitlab_access_token=GITLAB_ACCESS_TOKEN,
        api_base_url='https://gitlab.alexanderthamm.com/api/v4'
    )
    
    # Optionally: Search for the numbers of a project
    # gitlab_connection.list_groups()
    # gitlab_connection.list_projects_of_group(362)
    # gitlab_connection.search_project('jupyter')

    # Define the project of which you want to copy the existing vars
    jupyter_images = 578

    jupyter_images_vars_object = gitlab_connection \
        .get_project_variables_object(jupyter_images)
    jupyter_images_vars = jupyter_images_vars_object.get_project_vars()
    
    vars = transform_vars_data_structure(jupyter_images_vars)
    
    # Define the projects of which you want to set the variables
    metadata_extraction = 464 
    mp4_from_bag = 466 
    video_split_and_mask_creation = 473
    
    projects = [
        metadata_extraction,
        mp4_from_bag,
        video_split_and_mask_creation    
    ]    
    
    # Set the variables for each project
    for project in projects:
        project_variables = gitlab_connection \
            .get_project_variables_object(project)
        project_variables.set_project_variables(vars)
    

if __name__ == '__main__':
    main()
