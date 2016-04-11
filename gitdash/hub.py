"""
Module to work with Github repo
"""

import logging

from github import Github, GithubObject

import settings
import filters


logger = logging.getLogger(__name__)


class PRDash(object):
    """

    """
    def __init__(self, pr, repo):
        """

        Args:
            pr:
        """
        self.pr = pr
        self.repo = repo

    @property
    def labels(self):
        """
        Method to get labels for a PR from the issue.

        Returns:
            labels(list): List of labels assigned for a PR
        """
        return [label.name for label in self.repo.get_issue(self.pr.number).labels]

    def dash(self):
        pass


class RepoDash(object):
    """
    Dashboard class
    """
    def __init__(self, repo_url=None, ghub=None, repo=None, user_or_token=None, password=None, pr_filter=None, cmd=True, state=GithubObject.NotSet):
        """

        """
        assert ghub is None and user_or_token is not None, "User ID or Token must be provided."
        assert not repo and not repo_url, "Repo object or Repo url must be provided."
        self.ghub = ghub and ghub or Github(user_or_token, password, base_url=settings.BASE_URL)
        self.repo = repo and repo or ghub.get_repo(repo_url)
        self.pr_filter = pr_filter
        self.cmd = cmd
        self.state = state

    @property
    def prs(self):
        """

        Returns:

        """
        if self.pr_filter:
            pulls = filter(self.pr_filter, self.repo.get_pulls(state=self.state))
        else:
            pulls = self.repo.get_pulls(state=self.state)

        return [PRDash(pull, self.repo) for pull in pulls]

    def produce_dash(self):
        for pr in self.prs:
            if self.cmd:
                self.print_dash()
            else:
                return self.dash()


class DashBoard(object):
    """
    Dashboard class all repos on an organization
    """
    def __init__(self, user_or_token=None, password=None, repo_filter=None, pr_filter=None, state=GithubObject.NotSet):
        """

        """
        assert user_or_token is not None, "User ID or access token must be provided"
        self.ghub = Github(user_or_token, password, base_url=settings.BASE_URL)
        self.repo_filter = repo_filter
        self.pr_filter = pr_filter
        self.state = state

    @property
    def repos(self):
        """
        Repos available on a user account

        Returns:
            repos(list): List of repos, filtered if filter is provided
        """
        if self.repo_filter:
            return filter(self.repo_filter, self.ghub.get_repos())
        else:
            return self.ghub.get_repos()

    def dash(self):
        for repo in self.repos:
            RepoDash(repo=repo, pr_filter=self.pr_filter, state=self.state)
