from hub import DashBoard
import filters


def main():
    DashBoard(user='kumarvaradarajulu', repo_filter=filters.RepoFilter('django-andblog'), pr_filter=filters.LabelFilter('enhancement')).dash()


if __name__ == '__main__':
    main()
