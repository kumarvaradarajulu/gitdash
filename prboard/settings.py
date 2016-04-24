import os

PRBOARD_BASE_URL = "https://api.github.com"
PRBOARD_PR_FILTER = ""
PRBOARD_REPO_FILTER = ""
PRBOARD_ORG_FILTER = ""
PRBOARD_GITHUB_USERNAME = os.environ.get("PRBOARD_GITHUB_USERNAME", "")
PRBOARD_GITHUB_PASSWORD = os.environ.get("PRBOARD_GITHUB_PASSWORD", "")
PRBOARD_DETALED_MODE = True

PRBOARD_REPOS = PRBOARD_PR_FILTER.split(",")
PRBOARD_PR = []

# Default Organization
PRBOARD_ORG = PRBOARD_ORG_FILTER.split(",")

# Settings can be stored in file and that overwrites whats define in the sttings file.
PRBOARD_SETTINGS_FILE = os.environ.get('PRBOARD_SETTINGS_FILE', os.path.join(os.path.expanduser("~"), "prboard.cfg"))
