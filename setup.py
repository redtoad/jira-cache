from distutils.core import setup
import os


def read(path):
    root = os.path.dirname(os.path.abspath(__file__))
    return open(os.path.join(root, path)).read()


setup(
    name='jira-cache',
    description='Dump Jira issues to file and reload them without connection to the original server.',
    long_description=read('README.rst'),
    url='https://github.com/redtoad/jira-cache',
    version='0.8',
    author='Sebastian Rahlf',
    author_email='basti@redtoad.de',
    packages=['jira_cache'],
    requires=['jira'],
    license='MIT'
)