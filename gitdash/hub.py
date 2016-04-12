"""
Module to work with Github repo
"""

import logging
from functools import partial

import github
import github.GithubObject
import github.PaginatedList
import github.Repository


import settings


logger = logging.getLogger(__name__)
NotSet = github.GithubObject.NotSet


class Github(github.Github):
    """

    """
    def __init__(self, *args, **kwargs):
        super(Github, self).__init__(*args, **kwargs)

    def get_user_repos(self, user=NotSet, since=NotSet):
        """
        :calls: `GET /repositories <http://developer.github.com/v3/repos/#list-all-public-repositories>`_
        :param since: integer
        :rtype: :class:`github.PaginatedList.PaginatedList` of :class:`github.Repository.Repository`
        """
        assert since is NotSet or isinstance(since, (int, long)), since
        assert user is NotSet or isinstance(user, str), "User name must be a string"

        user = user == NotSet and self.get_user().login or user

        url_parameters = dict()
        if since is not NotSet:
            url_parameters["since"] = since
        return github.PaginatedList.PaginatedList(
            github.Repository.Repository,
            self.__requester,
            "/users/{}/repos".format(user),
            url_parameters
        )

    def get_org_repos(self, org, since=NotSet):
        """

        Returns:

        """
        assert since is NotSet or isinstance(since, (int, long)), since

        url_parameters = dict()
        if since is not NotSet:
            url_parameters["since"] = since

        return github.PaginatedList.PaginatedList(
            github.Repository.Repository,
            self.__requester,
            "orgs/{}/repositories".format(org),
            url_parameters
        )


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
        """

        Returns:

        """
        pass

    def print_dash(self):
        """

        """
        pr = self.pr
        print pr.number, pr.title, pr.state, pr.comments


class RepoDash(object):
    """
    Dashboard class
    """
    def __init__(self, repo_url=None, ghub=None, repo=None, user_or_token=None, password=None, pr_filter=None, cmd=True, state=NotSet):
        """

        """
        assert ghub is None and (repo is not None or user_or_token is not None), "User ID or Token must be provided."
        assert repo or repo_url, "Repo object or Repo url must be provided."
        if not repo:
            self.ghub = ghub and ghub or github.Github(user_or_token, password, base_url=settings.BASE_URL)
        self.repo = repo and repo or ghub.get_repo(repo_url)
        self.pr_filter = pr_filter
        self.cmd = cmd
        self.state = state

    @property
    def prs(self):
        """

        Returns:

        """
        pulls = [PRDash(pull, self.repo) for pull in self.repo.get_pulls(state=self.state)]
        if self.pr_filter:
            pulls = filter(self.pr_filter, pulls)

        return pulls

    def produce_dash(self):
        """

        Returns:

        """
        for pr in self.prs:
            if self.cmd:
                pr.print_dash()
            else:
                return pr.dash()


class DashBoard(object):
    """
    Dashboard class all repos on an organization
    """
    def __init__(self, user_or_token=settings.GITHUB_USERNAME, password=settings.GITHUB_PASSWORD, repo_filter=None,
                 pr_filter=None, state=NotSet, cmd=True, **kwargs):
        """

        """
        assert user_or_token is not None, "User ID or access token must be provided"
        #self.ghub = ExtendedGithub(user_or_token, password, base_url=settings.BASE_URL)
        self.ghub = Github(user_or_token, password, base_url=settings.BASE_URL)
        user = self.ghub.get_user().login
        self.repo_filter = repo_filter
        self.pr_filter = pr_filter
        self.state = state
        self.cmd = cmd
        self.org = kwargs.get('org', settings.DEFAULT_ORG)
        self.user = kwargs.get('user')

    @property
    def repos_func(self):
        return self.ghub.get_user_repos
        # return self.org and partial(self.ghub.get_org_repos, org=self.org) or self.user and partial(self.ghub.get_user_repos, user=self.user) or self.ghub.get_user_repos

    @property
    def repos(self):
        """
        Repos available on a user account

        Returns:
            repos(list): List of repos, filtered if filter is provided
        """

        if self.repo_filter:
            return filter(self.repo_filter, self.repos_func())
        else:
            return self.repos_func()

    def dash(self):
        for repo in self.repos:
            RepoDash(repo=repo, pr_filter=self.pr_filter, state=self.state, cmd=self.cmd).produce_dash()
