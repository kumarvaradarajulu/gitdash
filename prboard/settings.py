import os

from utils import parse_pr_filters

DEFAULT_BASE_URL = "https://api.github.com"

DEFAULT_PR_FILTER = ""
DEFAULT_REPO_FILTER = ""
DEFAULT_ORG_FILTER = ""

DEFAULT_REPOS = DEFAULT_PR_FILTER.split(",")
DEFAULT_PR = parse_pr_filters(DEFAULT_PR_FILTER)

DEFAULT_GITHUB_USERNAME = os.environ.get("DEFAULT_GITHUB_USERNAME", "")
DEFAULT_GITHUB_PASSWORD = os.environ.get("DEFAULT_GITHUB_PASSWORD", "")


# Default Organization
DEFAULT_ORG = DEFAULT_ORG_FILTER.split(",")
