from concurrent.futures import ThreadPoolExecutor, as_completed
from proxy_loader import load_proxies
from checker import check_proxy
from reporter import print_results
from config import DEFAULT_TIMEOUT, DEFAULT_THREADS


def run_proxy_check() -> None:
    target_url = input("Enter URL: ").strip()
    timeout_input = input(f"Enter timeout (seconds) [{DEFAULT_TIMEOUT}]: ").strip()
    timeout = int(timeout_input) if timeout_input else DEFAULT_TIMEOUT

    threads_input = input(f"Enter number of threads [{DEFAULT_THREADS}]: ").strip()
    threads = int(threads_input) if threads_input else DEFAULT_THREADS

    proxies = load_proxies()
    total = len(proxies)

    print(f"\nLoaded proxies: {total}")
    print(f"Target: {target_url}")
    print(f"Threads: {threads}")
    print("Checking...\n")

    results = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {
            executor.submit(check_proxy, proxy, target_url, timeout): proxy
            for proxy in proxies
        }
        for future in as_completed(futures):
            res = future.result()
            if res:
                results.append(res)

    print_results(results, total, target_url)