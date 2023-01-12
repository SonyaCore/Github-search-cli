#!/bin/env python3

################
import sys, os
import requests
import json
import time

################

################
class InvalidSorts(Exception):
    pass


class InvalidOrder(Exception):
    pass


class InvalidOutput(Exception):
    pass


class StNotModified(Exception):
    pass


class StValidationFailed(Exception):
    pass


class StServierUnavailable(Exception):
    pass


################


class QueryConstructor:
    data_length = 256


class StatusCodes:
    OK = (200,)
    not_modified = 304
    validation_failed = 422
    service_unavailable = 503


class Search:
    """
    https://docs.github.com/en/rest/search
    github rest api implementation for searching results
    every function takes an query string and a sorting method
    A query can contain any combination of search qualifiers supported on GitHub.
    The format of the search query is:
    SEARCH_KEYWORD_1 SEARCH_KEYWORD_N QUALIFIER_1 QUALIFIER_N
    """

    def __init__(self) -> None:
        self.headers = {"Accept": "application/vnd.github+json"}
        self.url = "https://api.github.com/search/"
        self.order = ["desc", "asc"]
        self.sortlist_code = ["None"]  # dummy array value
        self.sortlist_commits = ["author-date", "committer-date"]
        self.sortlist_issues = [
            "comments",
            "reactions",
            "reactions-+1",
            "reactions--1",
            "reactions-smile",
            "reactions-thinking_face",
            "reactions-heart",
            "reactions-tada",
            "interactions",
            "created",
            "updated",
        ]
        self.sortlist_lables = ["created, updated"]
        self.sortlist_repository = ["stars", "forks", "help-wanted-issues", "updated"]
        self.sortlist_users = ["followers", "repositories", "joined"]
        self.status_code = int

    def querycheck(self, order, sort, sortlist):
        """
        querychecking for input sorting or order is in the self.sortlists
        """
        if order not in self.order:
            raise InvalidOrder(
                "Invalid order query \n Valid order : {}".format(self.order)
            )
        if sort not in sortlist:
            raise InvalidSorts(
                "Invalid sort query \n Valid order : {}".format(sortlist)
            )

    def statuscode_check(self):
        """
        check status code of sending data to github api endpoints
        """
        if self.status_code == StatusCodes.OK:
            pass
        elif self.status_code == StatusCodes.not_modified:
            raise StNotModified("Not modified")
        elif self.status_code == StatusCodes.validation_failed:
            raise StValidationFailed(
                "Validation failed, or the endpoint has been spammed."
            )
        elif self.status_code == StatusCodes.service_unavailable:
            raise StServierUnavailable("Service unavailable")

    def code(
        self,
        query: str,
        sort: str = "None",
        order: str = "desc",
        per_page: int = 30,
        page: int = 1,
    ) -> json:
        self.querycheck(order, sort, self.sortlist_code)

        self.url += "code?q={}&order={}&per_page={}&page={}".format(
            query, order, per_page, page
        )
        data = requests.get(self.url, headers=self.headers)
        self.status_code = data.status_code
        result = json.loads(data.content)
        return json.dumps(result, indent=2)

    def commits(
        self,
        query: str,
        sort: str = "author-date",
        order: str = "desc",
        per_page: int = 30,
        page: int = 1,
    ) -> json:
        self.querycheck(order, sort, self.sortlist_commits)

        self.url += "commits?q={}&sort={}&order={}&per_page={}&page={}".format(
            query, sort, order, per_page, page
        )
        data = requests.get(self.url, headers=self.headers)
        self.status_code = data.status_code
        result = json.loads(data.content)
        return json.dumps(result, indent=2)

    def issues(
        self,
        query: str,
        sort: str = "comments",
        order: str = "desc",
        per_page: int = 30,
        page: int = 1,
    ) -> json:
        self.querycheck(order, sort, self.sortlist_issues)

        self.url += "issues?q={}&sort={}&order={}&per_page={}&page={}".format(
            query, sort, order, per_page, page
        )
        data = requests.get(self.url, headers=self.headers)
        self.status_code = data.status_code
        result = json.loads(data.content)
        return json.dumps(result, indent=2)

    def labels(
        self,
        repository_id: int,
        query: str,
        order: str = "desc",
        sort: str = "created",
        per_page: int = 30,
        page: int = 1,
    ) -> json:
        self.querycheck(order, sort, self.sortlist_lables)

        self.url += (
            "labels?repository_id={}&q={}&sort={}&order={}&per_page={}&page={}".format(
                repository_id, query, sort, order, per_page, page
            )
        )
        data = requests.get(self.url, headers=self.headers)
        self.status_code = data.status_code
        result = json.loads(data.content)
        return json.dumps(result, indent=2)

    def repository(
        self,
        name: str,
        sort: str,
        order: str = "desc",
        per_page: int = 30,
        page: int = 1,
    ) -> json:
        self.querycheck(order, sort, self.sortlist_repository)

        self.url += "repositories?q={}&s={}&order={}&per_page={}&page={}".format(
            name, sort, order, per_page, page
        )
        data = requests.get(self.url, headers=self.headers)
        self.status_code = data.status_code
        result = json.loads(data.content)
        return json.dumps(result, indent=2)

    def topics(self, query: str, per_page: int = 30, page: int = 1) -> json:
        self.url += "topics?q={}&per_page={}&page={}".format(query, per_page, page)
        data = requests.get(self.url, headers=self.headers)
        self.status_code = data.status_code
        result = json.loads(data.content)
        return json.dumps(result, indent=2)

    def users(
        self,
        query: str,
        sort: str = "followers",
        order: str = "desc",
        per_page: int = 30,
        page: int = 1,
    ) -> json:
        self.querycheck(order, sort, self.sortlist_users)

        self.url += "users?q={}&sort={}&order={}&per_page={}&page={}".format(
            query, sort, order, per_page, page
        )
        data = requests.get(self.url, headers=self.headers)
        self.status_code = data.status_code
        result = json.loads(data.content)
        return json.dumps(result, indent=2)

    def save(self, filename: str, function):
        try:
            if filename.split(".")[1] != "json":
                raise InvalidOutput("File must be JSON")
        except IndexError:
            filename += ".json"

        with open(filename, "a") as file:
            data = json.loads(function)
            file.write(json.dumps(data, indent=2))
