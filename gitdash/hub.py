"""
Module to work with Github repo
"""

import logging

from github import Github

import settings


logger = logging.getLogger(__name__)


class RepoDash(object):
    """
    Dashboard class
    """
    def __init__(self, ghub=None, user_or_token=None, password=None, repo_url=None):
        """

        """
        assert ghub is None and user_or_token is not None, "User ID or Token must be provided"
        assert repo_url, "Repo URL must be specified"
        self.ghub = ghub if ghub else Github(user_or_token, password, base_url=settings.BASE_URL)
        self.repo = ghub.get_repo(repo_url)

    @property
    def labels(self):
        """
        Method to get labels for a PR from the issue.

        Returns:
            labels(list): List of labels assigned for a PR
        """
        return [label.name for label in self.repo.get_issue(self.repo.number).labels]
