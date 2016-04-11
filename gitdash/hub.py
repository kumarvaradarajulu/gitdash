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
        self.ghub = ghub and ghub or Github(user_or_token, password, base_url=settings.BASE_URL)
        self.repo = ghub.get_repo(repo_url)

    @property
    def labels(self):
        """
        Method to get labels for a PR from the issue.

        Returns:
            labels(list): List of labels assigned for a PR
        """
        return [label.name for label in self.repo.get_issue(self.repo.number).labels]


class DashBoard(object):
    """
    Dashboard class all repos on a user account
    """
    def __init__(self, user_or_token=None, password=None, repo_filters=[], pr_filters=[]):
        """

        """
        assert user_or_token is not None, "User ID or access token must be provided"
        self.ghub = Github(user_or_token, password, base_url=settings.BASE_URL)
        self.repo_filters = repo_filters
        self.pr_filters = pr_filters

    @property
    def repos(self):
        """
        Repos available on a user account

        Returns:
            repos(list): List of repos, filtered if filter is provided
        """

        return filter(self.repo_filters, self.ghub.get_repos())
