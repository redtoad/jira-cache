
from jira_cache import CachedIssues


def test_initialisation_works_for_empty_list():
    issues = CachedIssues([])
    assert issues == []