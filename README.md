# 🌐 Proxy Checker

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)]()

A fast, multi-threaded Python tool that checks a list of proxies against a target URL.
Only working proxies are reported, along with their **country**, **ISP**, and **HTTP status**.

Built as a small modular project — easy to read, extend, and reuse.

---

## ✨ Features

- ⚡ **Multi-threaded** — checks all proxies in parallel via `ThreadPoolExecutor`
- 🌍 **Geo lookup** — detects the proxy's country and ISP by its external IP
- ✅ **Clean output** — shows only working proxies (errors are silently skipped)
- 📊 **Country summary** — groups working proxies by country at the end
- 🧩 **Modular structure** — separate files for loading, checking, geo lookup, and reporting
- 🖥️ **Interactive menu** — no CLI arguments to memorize

---

## 📦 Requirements

- **Python 3.9+**
- [`requests`](https://pypi.org/project/requests/) — HTTP library
- [`requests[socks]`](https://pypi.org/project/requests/#requests-with-socks) — for SOCKS4/SOCKS5 proxy support

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/USERNAME/proxy-checker.git
cd proxy-checker
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install requests
pip install "requests[socks]"
```

Or, if you have a `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Create your `proxies.txt`

Create a file named `proxies.txt` in the project root. One proxy per line.

```
# Lines starting with # are ignored
# Format: protocol://[user:pass@]host:port

http://192.168.1.1:8080
http://user:password@192.168.1.2:3128
socks4://user:password@192.168.1.3:1080
socks5://192.168.1.4:1080
```

Supported protocols:

| Protocol | Example                                |
| -------- | -------------------------------------- |
| HTTP     | `http://host:port`                     |
| HTTP + auth | `http://user:pass@host:port`        |
| SOCKS4   | `socks4://host:port`                   |
| SOCKS4 + auth | `socks4://user:pass@host:port`    |
| SOCKS5   | `socks5://host:port`                   |
| SOCKS5 + auth | `socks5://user:pass@host:port`    |

> ⚠️ `proxies.txt` is listed in `.gitignore` and will **not** be uploaded to GitHub.

---

## 🎮 Usage

Run the main script:

```bash
python main.py
```

You'll see an interactive menu:

```
========================================
PROXY CHECKER
========================================
  1. Exit
  2. Check proxies
========================================
Select option: 2
```

Choose **`2`** and answer a few prompts:

```
Enter URL: https://www.google.com
Enter timeout (seconds) [10]:
Enter number of threads [20]:
```

Then the tool will start checking — and print a result like this:

```
Loaded proxies: 18
Target: https://www.google.com
Threads: 20
Checking...

========================================
WORKING PROXIES (4 out of 18)
Request sent to: https://www.google.com
========================================
  1. http://185.12.34.56:8080
     IP:       185.12.34.56
     Country:  Germany [DE] — Hetzner Online GmbH
     Status:   HTTP 200

  2. socks5://91.22.33.44:1080
     IP:       91.22.33.44
     Country:  United States [US] — DigitalOcean, LLC
     Status:   HTTP 200

  3. http://203.0.113.7:3128
     IP:       203.0.113.7
     Country:  Netherlands [NL] — LeaseWeb Netherlands B.V.
     Status:   HTTP 200

  4. http://198.51.100.9:8080
     IP:       198.51.100.9
     Country:  France [FR] — OVH SAS
     Status:   HTTP 200

========================================
SUMMARY BY COUNTRY
========================================
  Germany [DE]: 1
  United States [US]: 1
  Netherlands [NL]: 1
  France [FR]: 1
```

---

## 🗂️ Project structure

```
proxy-checker/
├── main.py              # Menu entry point
├── checker_menu.py      # Interactive proxy check (menu option 2)
├── checker.py           # Check a single proxy
├── proxy_loader.py      # Load proxies from file
├── geo.py               # Country / ISP lookup by IP
├── reporter.py          # Output formatting
├── config.py            # Settings and shared constants
├── requirements.txt     # Dependencies
├── proxies.txt          # Your proxies (gitignored)
└── README.md
```

| File               | Responsibility                                              |
| ------------------ | ----------------------------------------------------------- |
| `main.py`          | Shows the menu and dispatches the chosen option              |
| `checker_menu.py`  | Asks for URL/timeout/threads, runs parallel checks           |
| `checker.py`       | Pure function `check_proxy()` — no I/O, easy to reuse        |
| `proxy_loader.py`  | Reads proxies from a text file                               |
| `geo.py`           | Queries `ip-api.com` to resolve country and ISP              |
| `reporter.py`      | Prints only working proxies and a country summary           |
| `config.py`        | Paths, API URLs, default values                              |

---

## ⚙️ How it works

For each proxy, the tool performs up to **two** requests:

1. **Target site check** — `GET {TARGET_URL}` through the proxy.
   If the status is `>= 400` or the request fails, the proxy is discarded.
2. **External IP lookup** — `GET https://httpbin.org/ip` through the same proxy.
   The returned IP is then looked up via **ip-api.com** to get the country and ISP.

All proxies are processed in parallel using a thread pool of the size you specify.

---

## 🧪 Example proxies for testing

You can use the following public testing services as "proxy sources" while you build your own list:

- [Free Proxy List](https://free-proxy-list.net/)
- [ProxyScrape](https://proxyscrape.com/free-proxy-list)
- [OpenProxyList](https://openproxylist.com/)

> Public proxies are unreliable, slow, and often blocked. For real work, use paid providers.

---

## 🛠️ Configuration

Most tweakable values live in `config.py`:

```python
PROXIES_FILE      = "proxies.txt"
GEO_API           = "http://ip-api.com/json/{ip}?fields=..."
IP_LOOKUP_URL     = "https://httpbin.org/ip"
DEFAULT_TIMEOUT   = 10
DEFAULT_THREADS   = 20
```

Change them if you want to use a different geo service, a different IP echo endpoint, or different defaults.

---

## 🧭 Troubleshooting

**`FileNotFoundError: proxies.txt`**
Create `proxies.txt` in the project root. The script looks for it next to `main.py`.

**All proxies fail with `ProxyError` or `ReadTimeout`**
Public proxies are usually dead or heavily rate-limited. Try fewer at a time, increase timeout, or use paid proxies.

**SOCKS proxies fail**
Make sure you installed SOCKS support: `pip install "requests[socks]"`.

**`ip-api.com` returns `status: fail`**
Free tier allows ~45 requests per minute per IP. For larger lists, get a token at [ipinfo.io](https://ipinfo.io) or [ipapi.co](https://ipapi.co) and swap the URL in `config.py`.

---



---

## ⚠️ Disclaimer

This tool is provided for **educational and research purposes only**.
Use it only with proxies you own or have explicit permission to use.
The author is not responsible for any misuse or damage caused by this software.
