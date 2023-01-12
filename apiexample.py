from Github.Search import Search
from Github.Timer import Timer


# initial github class
github = Search()

# initial timer class
timer = Timer()

# intial a timer (optional)
timer.start()

# using github.user method to fetch users from github rest api with a query
users = github.users("code")

# useing github.repository method to fetch repositories based on their name and ...
repository = github.repository("test",sort="stars",order="desc")


# using github.commits method to search on commits 
commits = github.commits("repo:octocat/Spoon-Knife+css",sort="committer-date")

# printing the fetched data
print(users)
print(repository)
print(commits)

# save the result to a json file
github.save("user.json" , users)
github.save("repo.json",repository)
github.save("commits.json",commits)

timer.stop()