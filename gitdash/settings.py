import os

BASE_URL = 'https://api.github.com'

REPO_FILTERS = []
PR_FILTERS = []

GITHUB_USERNAME = os.environ.get('GITHUB_USERNAME', '')
GITHUB_PASSWORD = os.environ.get('GITHUB_PASSWORD', '')


# Default Organization
DEFAULT_ORG = ''
