#!/usr/bin/env python3

# Author: David Kuda
# Creation Date: 8. February 2022

import argparse
import os
import sys

from gitlab_connection.connection_creator import ConnectionCreator


TOKEN = os.environ.get("GITLAB_TOKEN")
GITLAB_API_ENDPOINT = os.environ.get("GITLAB_API_ENDPOINT")


def main(args=None):
    """Search for a group or a project on GitLab to find the id.
    
    Example usage:
        python3 search.cli.py --project gitlab-api
        python3 seaerch.cli.py --group site-reliability-engineering 
    """
    if args is None:
        args = sys.argv[1:]
    
    args = parse_args(args)
    
    if (
        not args.project
        and not args.group
    ):
        print("Please provide either \"--project\" or \"--group\" to the command.")
        return 1

    finder = ConnectionCreator(
        gitlab_access_token=TOKEN,
        api_base_url=GITLAB_API_ENDPOINT
    ).create_project_finder()

    if args.project:
        finder.search_project(args.search)
    
    if args.group:
        finder.search_group(args.search)
    
    return 0


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("search", type=str)
    parser.add_argument("-g", "--group", action="store_true")
    parser.add_argument("-p", "--project", action="store_true")
    return parser.parse_args(args)


if __name__ == "__main__":
    main()
