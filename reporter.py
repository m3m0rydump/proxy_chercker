def print_results(results: list[dict], total: int, target_url: str) -> None:
    """Print only successful proxies and a summary by country."""
    print("=" * 40)
    print(f"WORKING PROXIES ({len(results)} out of {total})")
    print(f"Request sent to: {target_url}")
    print("=" * 40)

    if not results:
        print("No working proxies found.")
        return

    for i, r in enumerate(results, 1):
        print(f"{i:>3}. {r['proxy']}")
        print(f"     IP:       {r['ip']}")
        print(f"     Country:  {r['country']}")
        print(f"     Status:   HTTP {r['status']}")
        print()

    print("=" * 40)
    print("SUMMARY BY COUNTRY")
    print("=" * 40)

    by_country: dict[str, int] = {}
    for r in results:
        country = r["country"].split(" — ")[0]
        by_country[country] = by_country.get(country, 0) + 1

    for country, count in sorted(by_country.items(), key=lambda x: -x[1]):
        print(f"  {country}: {count}")