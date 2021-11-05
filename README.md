# GitLab API Client

If you need to copy the variables of GitLab project or if you want to add variables to a new project you can do it with the code in this repository. 

### How to use the script

You only need to use the script `/src/set_project_variables.py`.

Make sure that you have the environment variable `GITLAB_PERSONAL_API_TOKEN` available. You need to create a personal access token in GitLab and save the value in that environment variable. 

__1. Make a list of projects.__ The variables of every project in that list will be changed. Example:

```python
# Define a list of projects
metadata_extraction = 464 
mp4_from_bag = 466 
video_split_and_mask_creation = 473

projects = [
        metadata_extraction,
        mp4_from_bag,
        video_split_and_mask_creation    
    ]    
```

__2. Define the variables that you want to set.__ Create a new dictionary with your variables. Example:

```python
# Define the variables that you want to set
variables = {
    "variable_key": "variable_value",
    "Data": "Dave",
    "Dater": "Daver",
    "Daterr": "Daverr"
}
```

__3. Set the variables of the projects.__ Example:

```python
# Set the variables for each project
for project in projects:
    project_variables = gitlab_connection.get_project_variables_object(project)
    project_variables.set_project_variables(variables)
```



### How to extend the project with further classes

Let's say you want to implement the feature to add tickets to an issue board. You would probably want to do that in `/src/GitLabConnection.py`. So far you will find two classes in this script:

- `GitLabConnection` (base class)
- `GitLabProjectVariables(GitLabConnection)` (inherits from GitLabConnection)

So in order to extend the base class you just add a new class in `/src/GitLabConnection.py` and you make sure that your new class inherits from the base class `GitLabConnection`. 

I created a factory method to instantiate `GitLabProjectVariables` objects: __`GitLabConnection.create_project_variables_object()`__
