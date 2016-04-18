import argparse
import six

from github import GithubObject

from hub import DashBoard
# import prboard.filters as filters
# import prboard.settings as settings
# from prboard.utils import parse_pr_filters
import settings
import filters
from utils import parse_pr_filters

parser = argparse.ArgumentParser('')
parser.add_argument(
    "-b", "--baseurl",
    default=settings.DEFAULT_ORG,
    dest="org",
    type=six.text_type,
    help="Github base url to be used."
)

parser.add_argument(
    "-o", "--org",
    default=settings.DEFAULT_ORG,
    dest="org",
    type=six.text_type,
    help="Organization name to be checked. This is applicable for enterprise users. "
         "For personal accounts user name is sufficient"
)

parser.add_argument(
    "-r", "--repo",
    default=settings.DEFAULT_REPO_FILTER,
    dest="repos",
    type=six.text_type,
    help="Repo names to be filtered. Provide comma separated multiple repos"
)

parser.add_argument(
    "-s", "--status",
    default=GithubObject.NotSet,
    dest="status",
    type=six.text_type,
    help="Status to be filtered. Allowed values are open, closed, all. Default is all"
)

parser.add_argument(
    "-u", "--user",
    default=settings.DEFAULT_GITHUB_USERNAME,
    dest="username",
    type=six.text_type,
    help="User name to login to Github. Default is picked from settings.DEFAULT_GITHUB_USER"
)

parser.add_argument(
    "-ru", "--repouser",
    default=settings.DEFAULT_GITHUB_USERNAME,
    dest="repouser",
    type=six.text_type,
    help="User name on Github for which the dashboard must be checked. "
         "Login user name is different from checking user name. For instance you may want to check PRs on your "
         "colleague's Github account, but login with yours. This parameter is to provide your colleague's user name"
)

parser.add_argument(
    "-p", "--password",
    default=settings.DEFAULT_GITHUB_PASSWORD,
    dest="password",
    type=six.text_type,
    help="Password to login to Github. Default is picked from settings.DEFAULT_GITHUB_PASSWORD"
)

parser.add_argument(
    "-pr", "--pull",
    default=settings.DEFAULT_REPO_FILTER,
    dest="pull",
    type=six.text_type,
    help="Filter Pull requests, with the following criteria"
         "By PR Number ---->  num:123"
         "By PR Labels ---->  labels:label1;label2;label3"
         "By PR Title  ---->  title:pr_title   (wilcard match)"
         "By PR Title  ---->  etitle:pr_title  (exact match)"
         "By PR All    ---->  num:123,labels:label1;label2;label3,title:pr_title"
)


def main():
    args = parser.parse_args()
    kwargs = {}
    if args.username:
        kwargs['user_or_token'] = args.username
    if args.repouser:
        kwargs['repouser'] = args.repouser
    if args.password:
        kwargs['password'] = args.password
    if args.repos:
        repo_filters = map(filters.RepoFilter, filter(lambda x: x != '', args.repos.split(",")))
        kwargs['repo_filter'] = repo_filters
    if args.pull:
        pr_filters = parse_pr_filters(args.pull)
        kwargs['pr_filter'] = pr_filters
    DashBoard(**kwargs).dash()

if __name__ == '__main__':
    main()
