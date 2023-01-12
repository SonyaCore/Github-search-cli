import argparse
import sys

from .Search import Search
from .Timer import Timer
from .Utils import Color
from .Version import APP

formatter = lambda prog: argparse.HelpFormatter(prog, max_help_position=48)
parser = argparse.ArgumentParser(formatter_class=formatter,add_help=False)
parser.usage = (
    Color.Yellow
    + "github"
    + Color.Reset
    + " "
    + "searchquery --query endpoint_query"
)
parser.usage += (
    Color.Green
    + "\nsearchquerys : [code,commits,issues,labels,repository,topics,users]"
    + Color.Reset
)

parser.add_argument("search", action="store", help="Search api endpoint.")

parser.add_argument(
    "--query", "-q", action="store", help="Query for the searching method",metavar=""
)
parser.add_argument(
    "--sort", "-s", action="store", help="Sorting method for request output", default="",metavar=""
)
parser.add_argument(
    "--order",
    "-o",
    action="store",
    help="Define first search result returned is the highest or lowest number of matches.",metavar="",
    default="desc",
)
parser.add_argument(
    "--perpage",
    "-p",
    action="store",
    type=int,
    help="The number of results per page ",
    default=30,
    metavar=""
)
parser.add_argument(
    "--page",
    "-page",
    action="store",
    type=int,
    help="Page number of the results to fetch.",
    default=1,
    metavar=""
)
parser.add_argument(
    "--repoid",
    "-i",
    action="store",
    type=int,
    help="Respository id for labels endpoint",
    metavar=""
)
parser.add_argument("--save", "-j", action="store", type=str, help="Save JSON output",metavar="")
opt = parser.add_argument_group(f"info")
opt.add_argument("-v", "--version", action="version", version="%(prog)s " + str(APP.version))
opt.add_argument("-h", "--help", action="help", help="show this help message and exit")


args = parser.parse_args()

def main():
    github = Search()
    timer = Timer()

    timer.start()

    if args.search == "code":
        if args.sort == "":
            args.sort = "None"
        data = github.code(
            query=args.query,
            sort=args.sort,
            order=args.order,
            per_page=args.perpage,
            page=args.page,
        )

    elif args.search == "commits":
        if args.sort == "":
            args.sort = "author-date"
        data = github.commits(
            query=args.query,
            sort=args.sort,
            order=args.order,
            per_page=args.perpage,
            page=args.page,
        )

    elif args.search == "issues":
        if args.sort == "":
            args.sort = "comments"
        data = github.issues(
            query=args.query,
            sort=args.sort,
            order=args.order,
            per_page=args.perpage,
            page=args.page,
        )

    elif args.search == "labels":
        if args.sort == "":
            args.sort = "updated"
        data = github.labels(
            query=args.query,
            sort=args.sort,
            repository_id=args.repoid,
            order=args.order,
            per_page=args.perpage,
            page=args.page,
        )

    elif args.search == "repository":
        if args.sort == "":
            args.sort = "updated"
        data = github.repository(
            query=args.query,
            sort=args.sort,
            order=args.order,
            per_page=args.perpage,
            page=args.page,
        )

    elif args.search == "topics":
        data = github.repository(query=args.query, per_page=args.perpage, page=args.page)

    elif args.search == "users":
        if args.sort == "":
            args.sort = "followers"
        data = github.users(
            query=args.query,
            sort=args.sort,
            order=args.order,
            per_page=args.perpage,
            page=args.page,
        )

    print(data)

    if args.save:
        github.save(args.save, data)

    timer.stop()


if __name__ == "__main__":
    main()