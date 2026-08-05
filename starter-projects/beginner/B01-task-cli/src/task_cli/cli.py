import argparse
import sys

from .service import TaskService
from .storage import JsonStorage


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="A small task list")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--title", required=True)
    subparsers.add_parser("list")

    # Student Core: wire these commands to TaskService.complete/delete.
    done_parser = subparsers.add_parser("done")
    done_parser.add_argument("id", type=int)
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    service = TaskService(JsonStorage())
    try:
        if args.command == "add":
            task = service.add(args.title)
            print(f"created #{task.id}: {task.title}")
        elif args.command == "list":
            for task in service.list():
                mark = "x" if task.completed else " "
                print(f"[{mark}] #{task.id} {task.title}")
        elif args.command == "done":
            task = service.complete(args.id)
            print(f"completed #{task.id}")
        elif args.command == "delete":
            service.delete(args.id)
            print(f"deleted #{args.id}")
    except (NotImplementedError, ValueError, KeyError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
