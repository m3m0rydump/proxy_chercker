import requests
from config import GEO_API


def get_country(ip: str) -> str:
    try:
        r = requests.get(GEO_API.format(ip=ip), timeout=10)
        data = r.json()
        if data.get("status") == "success":
            country = data.get("country", "?")
            code = data.get("countryCode", "?")
            isp = data.get("isp", "?")
            return f"{country} [{code}] — {isp}"
    except Exception:
        pass
    return "unknown"