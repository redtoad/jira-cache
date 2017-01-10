
import sys
sys.path.insert(0, '..')

from jira import JIRA
from jira_cache import CachedIssues

print('Connecting to https://jira.atlassian.com...')
jira = JIRA('https://jira.atlassian.com/')
result = jira.search_issues('project=JRA and text ~ "Python"', expand='changelog')

print('Caching %i issues...' % len(result))
cached = CachedIssues(result)
cached.dump(open('python-issues.json', 'w'))

print('Loading issues from dump...')
print(CachedIssues.load(open('python-issues.json')))