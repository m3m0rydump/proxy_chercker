from checker_menu import run_proxy_check


def print_menu() -> None:
    print("=" * 40)
    print("PROXY CHECKER")
    print("=" * 40)
    print("  1. Exit")
    print("  2. Check proxies")
    print("=" * 40)


def main() -> None:
    run_proxy_check()

main()