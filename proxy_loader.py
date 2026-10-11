from config import PROXIES_FILE


def load_proxies(path: str = PROXIES_FILE) -> list[str]:
    """Load proxies from a text file (one per line)."""
    with open(path, "r", encoding="utf-8") as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#")
        ]