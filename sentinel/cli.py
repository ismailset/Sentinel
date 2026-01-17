import argparse
from sentinel.security import check_security
from sentinel.uptime import check_uptime
from sentinel.passwords import check_password

def main():
    parser = argparse.ArgumentParser(prog="sentinel")
    sub = parser.add_subparsers(dest="command")

    sec = sub.add_parser("security")
    sec.add_argument("url")

    up = sub.add_parser("uptime")
    up.add_argument("url")

    pwd = sub.add_parser("password")
    pwd.add_argument("password")

    args = parser.parse_args()

    if args.command == "security":
        check_security(args.url)
    elif args.command == "uptime":
        check_uptime(args.url)
    elif args.command == "password":
        check_password(args.password)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
