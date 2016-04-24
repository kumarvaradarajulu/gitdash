prboard Command line Git PR dashboard
=====================================

.. image:: https://travis-ci.org/kumarvaradarajulu/prboard.svg?branch=master
    :target: https://travis-ci.org/kumarvaradarajulu/prboard

.. image:: https://landscape.io/github/kumarvaradarajulu/prboard/master/landscape.svg?style=plastic
   :target: https://landscape.io/github/kumarvaradarajulu/prboard/master
   :alt: Code Health

.. image:: https://coveralls.io/repos/github/kumarvaradarajulu/prboard/badge.svg?branch=master
    :target: https://coveralls.io/github/kumarvaradarajulu/prboard?branch=master

Help
----
usage:  [-h] [-b BASEURL] [-o ORG] [-r REPOS] [-s STATUS] [-u USERNAME]
        [-ru REPOUSER] [-p PASSWORD] [-pr PULL] [-d DETAILED_MODE] [-v] [-V]

optional arguments:
  -h, --help            show this help message and exit
  -b BASEURL, --baseurl BASEURL
                        Github base url to be used.
  -o ORG, --org ORG     Organization name to be checked. This is applicable
                        for enterprise users. For personal accounts user name
                        is sufficient
  -r REPOS, --repo REPOS
                        Repo names to be filtered. Provide comma separated
                        multiple repos
  -s STATUS, --status STATUS
                        Status to be filtered. Allowed values are open,
                        closed, all. Default is all
  -u USERNAME, --user USERNAME
                        User name to login to Github. Default is picked from
                        settings.DEFAULT_GITHUB_USER
  -ru REPOUSER, --repouser REPOUSER
                        User name on Github for which the dashboard must be
                        checked. Login user name is different from checking
                        user name. For instance you may want to check PRs on
                        your colleague's Github account, but login with yours.
                        This parameter is to provide your colleague's user
                        name
  -p PASSWORD, --password PASSWORD
                        Password to login to Github. Default is picked from
                        settings.PRBOARD_GITHUB_PASSWORD
  -pr PULL, --pull PULL
                        Filter Pull requests, with the following criteriaBy PR
                        Number ----> num:123By PR Labels ---->
                        labels:label1;label2;label3By PR Title ---->
                        title:pr_title (wilcard match)By PR Title ---->
                        etitle:pr_title (exact match)By PR All ---->
                        num:123,labels:label1;label2;label3,title:pr_title
  -d DETAILED_MODE, --detailed_mode DETAILED_MODE
                        Option to control output mode. If Detailed mode is set
                        each PR and it's comments is displayed
  -v, --verbose         Control verbosity level. Can be supplied multiple
                        times to increase verbosity level
  -V, --version         To know prboard version number
