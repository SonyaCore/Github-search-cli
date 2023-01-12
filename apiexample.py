from Github.Search import Search
from Github.Timer import Timer


github = Search()
timer = Timer()

# intial a timer (optional)
timer.start()

# use github.user method to fetch users from github rest api with a query
data = github.users("code")

# printing the fetched data
print(data)

# save the result to a json file
github.save("user.json" , data)

timer.stop()