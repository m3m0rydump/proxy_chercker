import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROXIES_FILE = os.path.join(BASE_DIR, "proxies.txt")

GEO_API = "http://ip-api.com/json/{ip}?fields=status,country,countryCode,isp,query"

IP_LOOKUP_URL = "https://httpbin.org/ip"

DEFAULT_TIMEOUT = 10
DEFAULT_THREADS = 20