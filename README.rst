==========
jira-cache
==========

Dump Jira issues to file and reload them without connection to the original server.

Quickstart
----------

Dump issues::

    from jira import JIRA
    from jira_cache import CachedIssues

    jira = JIRA('https://jira.atlassian.com/')
    result = jira.search_issues('project=JRA and text ~ "Python"')
    cached = CachedIssues(result)
    cached.dump(open('python-issues.json', 'w'))

Loading from file::

    from jira import JIRA
    from jira_cache import CachedIssues

    result = CachedIssues.load(open('python-issues.json'))

Installation
------------

Simply run ::

    pip install jira-history

Contributing
------------

Please do! I would love for this to be developed further by anyone who is interested. Wherever possible, please
provide unit tests for your work (yes, this is very much a 'do as I say, not as I do' kind of moment).
Don't forget to add your name to AUTHORS.

License
-------

Copyright (c) 2016 Sebastian Rahlf

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.