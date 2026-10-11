import requests
from config import IP_LOOKUP_URL
from geo import get_country


def check_proxy(proxy: str, url: str, timeout: int) -> dict | None:
    proxy_dict = {"http": proxy, "https": proxy}
    try:
        r = requests.get(url, proxies=proxy_dict, timeout=timeout)
        if r.status_code >= 400:
            return None

        ip_resp = requests.get(IP_LOOKUP_URL, proxies=proxy_dict, timeout=timeout)
        ip = ip_resp.json().get("origin", "").split(",")[0].strip()

        country = get_country(ip) if ip else "unknown"

        return {
            "proxy": proxy,
            "ip": ip,
            "country": country,
            "status": r.status_code,
        }
    except Exception:
        return None