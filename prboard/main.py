import argparse
import six

from github import GithubObject

from . import __description__
from hub import DashBoard
import prboard.filters as filters
import prboard.settings as settings
from prboard.utils import parse_pr_filters

parser = argparse.ArgumentParser(__description__)
parser.add_argument(
    "-o", "--org",
    default=settings.DEFAULT_REPOS,
    dest="org",
    type=six.text_type,
    help="Organization name to be checked. This is applicable for enterprise users. For personal accounts user name is sufficient"
)

parser.add_argument(
    "-r", "--repo",
    default=settings.DEFAULT_REPOS,
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
    "-p", "--password",
    default=settings.DEFAULT_GITHUB_PASSWORD,
    dest="password",
    type=six.text_type,
    help="Password to login to Github. Default is picked from settings.DEFAULT_GITHUB_PASSWORD"
)

parser.add_argument(
    "-pr", "--pull",
    default=settings.DEFAULT_REPOS,
    dest="pull",
    type=six.text_type,
    help="Filter Pull requests, with the following criteria"
         "By PR Number ---->  num:123"
         "By PR Labels ---->  labels:label1,label2,label3"
         "By PR Title  ---->  title:pr_title   (wilcard match)"
         "By PR Title  ---->  etitle:pr_title  (exact match)"
         "By PR All    ---->  num:123,labels:label1,label2,label3,title:pr_title"
)


def main():
    args = parser.parse_args()
    repo_filters = map(filters.RepoFilter, args.repos)
    pr_filters = parse_pr_filters(args.pull)
    #DashBoard(user=args.username, password=args.password, repo_filter=repo_filters, pr_filter=filters.LabelFilter('enhancement')).dash()
    DashBoard(user=args.username, password=args.password, repo_filter=repo_filters, pr_filter=pr_filters).dash()

if __name__ == '__main__':
    main()
