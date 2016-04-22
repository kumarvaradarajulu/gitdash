# import prboard.constants as constants
import constants


def parse_pr_filters(filter_str):
    """
    Function to parse PR filter specified.
        "By PR Number ---->  num:123"
        "By PR Labels ---->  labels:label1,label2,label3"
        "By PR Title  ---->  title:pr_title   (wilcard match)"
        "By PR Title  ---->  etitle:pr_title  (exact match)"
        "By PR All    ---->  num:123,labels:label1,label2,label3,title:pr_title"

    Args:
        filter_str (str): Filter String to be parsed

    Returns:
        filters (list): List of filter objects

    """
    filter_mappings = constants.FILTER_COMMAND_MAPPING
    filts = filter(lambda x: x!= "", filter_str.split(','))
    filter_objects = []
    for f in filts:
        try:
            cmd, value = f.split(':')
            filter_class = filter_mappings[cmd]
            filter_objects.append(filter_class(filter_value=value))
        except (ValueError, KeyError):
            continue

    return filter_objects


class PrintPR(object):
    def __init__(self, pr, repo, detailed_mode=False):
        self.pr = pr
        self.repo = repo
        self.prnum = pr.number
        self.title = pr.title
        self.comments = pr.comments
        self.state = pr.state
        self.detailed_mode = detailed_mode

    def print_output(self):
        if self.detailed_mode:
            self.print_detailed_output()
        else:
            self.print_summary()

    def print_summary(self):
        colors = constants.Colors
        print colors.BOLD + str(self.prnum).ljust(6) + ' ' + self.title[:50].ljust(50) + ' ' + colors.FAIL + str(self.comments) + ' comment(s)' + colors.ENDC

    def print_detailed_output(self):
        colors = constants.Colors
        print colors.HEADER + str(self.prnum).ljust(6) + ' ' + self.title[:100]
        print colors.WARNING + '=' * 50 + colors.ENDC
        if self.comments:
            for comment in self.pr.get_issue_comments():
                print colors.BOLD + '{}@@{}:::'.format(comment.user.login, str(comment.updated_at)).ljust(40) + colors.ENDC + comment.body
        else:
            print "No comments"
