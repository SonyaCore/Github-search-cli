# Github-search-cli

![python3]
[![project-url](https://img.shields.io/pypi/status/github-search-cli)](https://pypi.org/pypi/github-search-cli/)
[![version](https://img.shields.io/pypi/v/github-search-cli)](https://pypi.org/pypi/github-search-cli/)
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

### GitHub restful API search implementation on python3

## About

github-search-cli provides a module called Github, that can be used to access all of GitHub's Search API functionality from your command-line

https://docs.github.com/en/rest/search

## Installation

### Installing gitub-search-cli using pip

```
pip3 install github-search-cli
```

OR

### Installing through GitHub

```
pip3 install --upgrade git+https://github.com/SonyaCore/Github-search-cli.git
```

## Usage

**Show help and exit**

```python3
python3 -m Github -h
```

**Options**

```
  --query , -q     Query for the searching method
  --sort , -s      Sorting method for request output
  --order , -o     Define the first search result returned is the highest or lowest number of matches.
  --perpage , -p   The number of results per page
  --page , -page   Page number of the results to fetch.
  --repoid , -i    Repository id for labels endpoint
  --save , -j      Save JSON output
```

all the search queries for https://docs.github.com/en/rest/search is implemented on this python module
list of available search queries
`code,commits,issues,labels,repository,topics,users`

for fetching 100 results or 200 results per page use --perpage arugment
ex :

```
python3 -m Github repository --query repo:username/repo --perpage 200 --save reg.json
```

### Search examples

Search for users with a query

```python3
python3 -m Github users -q user  --save user.json
```

Search for repositories with defined arguments

```python3
python3 -m Github repository --query repo:username/repo --save reg.json
```

## Using API

You can also use it like this:

```
from Github.Search import Search
from Github.Timer import Timer


# initial github class
github = Search()

# initial timer class
timer = Timer()

# intial a timer (optional)
timer.start()

# using github.user method to fetch users from GitHub rest API with a query
users = github.users("code")

# using github.repository method to fetch repositories based on their name and ...
repository = github.repository("test",sort="stars",order="desc")


# using github.commits method to search on commits
commits = github.commits("repo:octocat/Spoon-Knife+css",sort="committer-date")

# printing the fetched data
print(users)
print(repository)
print(commits)

# save the result to a JSON file
github.save("user.json", users)
github.save("repo.json",repository)
github.save("commits.json",commits)

timer.stop()
```

## License

Licensed under the [GPL-3][license] license.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/SonyaCore/Github-search-cli?style=flat
[contributors-url]: https://github.com/SonyaCore/Github-search-cli/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/SonyaCore/Github-search-cli?style=flat
[forks-url]: https://github.com/SonyaCore/Github-search-cli/network/members
[stars-shield]: https://img.shields.io/github/stars/SonyaCore/Github-search-cli?style=flat
[stars-url]: https://github.com/SonyaCore/Github-search-cli/stargazers
[issues-shield]: https://img.shields.io/github/issues/SonyaCore/Github-search-cli?style=flat
[issues-url]: https://github.com/SonyaCore/Github-search-cli/issues
[python3]: https://img.shields.io/badge/Python3-blue?logo=python
[license]: LICENCE
