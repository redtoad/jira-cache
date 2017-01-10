import json

from jira.resources import cls_for_resource


class CachedIssues(list):

    def __init__(self, issues, jql=None):
        list.__init__(self, issues)

    def dump(self, fp):
        return json.dump([issue.raw for issue in iter(self)], fp)

    @staticmethod
    def load(fp):
        data = json.load(fp)
        issues = [cls_for_resource(issue['self'])(None, None, issue) for issue in data]
        return CachedIssues(issues)