#!/bin/env python3

################
import sys
import requests
import json
################

################
class APP:
    name : str = "Github-search-cli"
    version : float = 0.1
################

################
class InvalidSorts(Exception):
    pass

class InvalidOrder(Exception):
    pass
################

print(APP.name , APP.version , "Python " + sys.version)

class Search():
    def __init__(self) -> None:
        self.headers = {"Accept": "application/vnd.github+json"}
        self.url = "https://api.github.com/search/"
        self.order = ["desc","asc"]
        self.sortlist_code = ['None'] # dummy array value
        self.sortlist_commits = ["author-date", "committer-date"]
        self.sortlist_issues = ["comments", "reactions", "reactions-+1", "reactions--1", "reactions-smile", "reactions-thinking_face", "reactions-heart", "reactions-tada", "interactions", "created", "updated"]
        self.sortlist_lables = ["created, updated"]
        self.sortlist_repository = ["stars", "forks", "help-wanted-issues", "updated"]
        self.sortlist_users = ["followers", "repositories", "joined"]

    def querycheck(self,order, sort , sortlist ):
        if order not in self.order :
            raise InvalidOrder("Invalid order query \n Valid order : {}".format(self.order))
        if sort not in sortlist:
            raise InvalidSorts("Invalid sort query \n Valid order : {}".format(sortlist))

    def code(self,query : str ,sort : str = 'None' , order : str = "desc" , per_page : int = 30 , page : int = 1) -> json:
        self.querycheck(order,sort,self.sortlist_code)

        self.url +=  "code?q={}&order={}&per_page={}&page={}".format(query,order,per_page,page)
        data = requests.get(self.url,headers=self.headers)
        result = json.loads(data.content)
        return json.dumps(result,indent=2)


    def commits(self,query :str , sort : str = "author-date" , order : str =  "desc" , per_page : int = 30 , page : int = 1) -> json:
        self.querycheck(order,sort,self.sortlist_commits)

        self.url +=  "commits?q={}&sort={}&order={}&per_page={}&page={}".format(query,sort,order,per_page,page)
        data = requests.get(self.url,headers=self.headers)
        result = json.loads(data.content)
        return json.dumps(result,indent=2)


    def issues(self,query :str , sort : str = "comments" , order : str =  "desc" , per_page : int = 30 , page : int = 1) -> json:
        self.querycheck(order,sort,self.sortlist_issues)

        self.url +=  "issues?q={}&sort={}&order={}&per_page={}&page={}".format(query,sort,order,per_page,page)
        data = requests.get(self.url,headers=self.headers)
        result = json.loads(data.content)
        return json.dumps(result,indent=2)


    def labels(self,repository_id : int , query : str , order : str = "desc" , sort : str = "created" , per_page : int = 30 , page :int = 1) -> json:
        self.querycheck(order,sort,self.sortlist_lables)
        
        self.url +=  "labels?repository_id={}&q={}&sort={}&order={}&per_page={}&page={}".format(repository_id,query,sort,order,per_page,page)
        data = requests.get(self.url,headers=self.headers)
        result = json.loads(data.content)
        return json.dumps(result,indent=2)

    def repository(self,name : str , sort : str, order : str = "desc" , per_page : int = 30, page : int = 1 ) -> json:
        self.querycheck(order,sort,self.sortlist_repository)
   
        self.url +=  "repositories?q={}&s={}&order={}&per_page={}&page={}".format(name,sort,order,per_page,page)
        data = requests.get(self.url,headers=self.headers)
        result = json.loads(data.content)
        return json.dumps(result,indent=2)


    def topics(self,query : str , per_page : int = 30 , page : int = 1) -> json:
        self.url +=  "topics?q={}&per_page={}&page={}".format(query,per_page,page)
        data = requests.get(self.url,headers=self.headers)
        result = json.loads(data.content)
        return json.dumps(result,indent=2)
    

    def users(self,query : str , sort : str = "followers" , order : str = "desc" , per_page : int = 30 ,page : int = 1) -> json:
        self.querycheck(order,sort,self.sortlist_users)
        
        self.url +=  "users?q={}&sort={}&order={}&per_page={}&page={}".format(query,sort,order,per_page,page)
        data = requests.get(self.url,headers=self.headers)
        result = json.loads(data.content)
        return json.dumps(result,indent=2)



github = Search()
# print(github.code("repo:username/repo"))
# print(github.repository('mika','updated',per_page=10,page=4))
# print(github.commits("committer:commiterusername",per_page=1))
# print(github.issues("windows+label:bug+language:python+state"))
# print(github.users("SonyaCore",sort="repositories"))
# print(github.topics('v2ray',per_page=100))
# print(github.users("username"))