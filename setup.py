from setuptools import setup
import os


def read(path):
    root = os.path.dirname(os.path.abspath(__file__))
    return open(os.path.join(root, path)).read()


setup(
    name='jira-cache',
    description='Dump Jira issues to file and reload them without connection to the original server.',
    long_description=read('README.rst'),
    url='https://github.com/redtoad/jira-cache',
    version='0.8.3',
    author='Sebastian Rahlf',
    author_email='basti@redtoad.de',
    packages=['jira_cache'],
    install_requires=['jira'],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='jira ticket caching json dump'
)
