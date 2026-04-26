import argparse

def main():
    parser = argparse.ArgumentParser(description="CLI Tool for Project Management")
    subparsers = parser.add_subparsers()

    # Example command: add-user
    user_parser = subparsers.add_parser('add-user', help="Add a new user")
    user_parser.add_argument('--name', type=str, required=True, help="Name of the user")
    user_parser.add_argument('--email', type=str, required=True, help="Email of the user")
    user_parser.set_defaults(func=lambda args: print(f"Adding user: {args.name}, {args.email}"))

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()