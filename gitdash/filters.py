class BaseFilter(object):
    """
    BaseFilter to apply filters on Repo/PullRequest objects.
    """

    def __init__(self, filter_str=''):
        """

        Args:
            filter_str (str): Filter string to
        """
        self.filter_str = filter_str.lower()

    @property
    def filter_on(self):
        raise NotImplemented

    def __call__(self, obj, wildcard=False, *args, **kwargs):
        """

        Args:
            obj (Repo or PullRequest): Filter object either repo or PR
            wildcard(bool): Boolean representing if a wildcard match is to be done or not.
            *args:
            **kwargs:

        Returns:
            bool: True or False based on the filter

        """
        self.obj = obj

        if wildcard:
            return self.filter_str in self.filter_on
        else:
            return self.filter_str == self.filter_on


class PRFilter(BaseFilter):
    """
    Filter to apply filters on PR. Filters title based on filter string
    """
    @property
    def filter_on(self):
        """

        Returns:

        """

        return self.obj.pr.title.lower()


class LabelFilter(PRFilter):

    @property
    def filter_on(self):
        """

        Returns:

        """

        return self.obj.labels

    def __call__(self, wildcard=None, *args, **kwargs):
        """

        Args:
            wildcard:
            *args:
            **kwargs:

        Returns:

        """
        if isinstance(self.filter_str, (list, tuple)):
            return all([label in self.filter_on for label in self.filter_str])


class MileStoneFilter(PRFilter):
    @property
    def filter_on(self):
        """

        Returns:

        """
        return self.obj.milestone.lower()


class RepoFilter(BaseFilter):
    @property
    def filter_on(self):
        """

        Returns:

        """
        return self.obj.name.lower()
