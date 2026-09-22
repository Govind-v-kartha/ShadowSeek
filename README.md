<div align="center">
  <h1>🔍 Shadowseek</h1>
  <p><strong>Advanced OSINT Reconnaissance & User Presence Intelligence Agent</strong></p>
  <p>An intelligence-gathering platform for security researchers, penetration testers, and threat analysts: 150+ platform investigation modules behind an interactive dual-panel terminal interface, consolidated multi-target master summary, and native Model Context Protocol (MCP) server.</p>
  <p><em>Use it as an Interactive REPL, command-line tool, or autonomous AI-driven MCP server.</em></p>
  <p><em>Engineered for stealth, depth, and intelligence — verified accounts and deterministic extractions.</em></p>
</div>

<div align="center">

[![Release](https://img.shields.io/badge/version-1.6.0-blue?style=flat-square)](https://github.com/Govind-v-kartha/ShadowSeek/releases)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![MCP](https://img.shields.io/badge/protocol-MCP-blueviolet?style=flat-square)](https://modelcontextprotocol.io/)
[![Creator](https://img.shields.io/badge/creator-govind-orange?style=flat-square)](https://github.com/Govind-v-kartha)
[![Portfolio](https://img.shields.io/badge/portfolio-govind--v--kartha.vercel.app-informational?style=flat-square)](https://govind-v-kartha.vercel.app/)
[![Platforms](https://img.shields.io/badge/platforms-150%2B%20sites-success?style=flat-square)](#supported-platform-categories)

</div>

---

## ⚡ Quick Start (Free, MIT)

### Installation

```bash
# Clone the repository
git clone https://github.com/Govind-v-kartha/ShadowSeek.git
cd ShadowSeek

# Install dependencies and register CLI globally
pip install -e .
```

### Launch Modes

```bash
# 1. Launch Interactive REPL Console (Default)
shadowseek
# or
osint

# 2. Direct Username Reconnaissance
shadowseek -u johndoe

# 3. Direct Email Presence Enumeration
shadowseek -e target@example.com

# 4. Cross-Scan & Pivot Chain Analysis
shadowseek -u johndoe --cross-scan

# 5. Check for Infostealer Compromise (Hudson Rock)
shadowseek -e target@example.com --hudson

# 6. Export Full Forensic PDF Report
shadowseek -e target@example.com -f pdf -o investigation_report.pdf
```

---

## 🖥️ Interactive Console & Visual Interface

Run `shadowseek` with no arguments to enter the **Interactive Console Mode**. The session remains active across inquiries, letting you pivot, scan skipped loud modules on demand, browse categories, and export reports seamlessly.

```text
   _____ _                 _                     _    
  / ____| |               | |                   | |   
 | (___ | |__   __ _  __| | _____      _____  ___| | __
  \___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / / __|/ _ \ |/ /
  ____) | | | | (_| | (_| | (_) \ V  V /\__ \  __/   < 
 |_____/|_| |_|\__,_|\__,_|\___/ \_/\_/ |___/\___|_|\_\ Version: 1.6.0
                                                       Creator: govind
╭────────────────────── Shadowseek - Developed by govind ──────────────────────╮
│ Interactive Console Commands:                                                │
│   • Enter any username or email     Scan target across all platforms         │
│   • loud or 2                         Scan skipped loud modules for current  │
│ target                                                                       │
│   • export <pdf|json|csv>          Export scan results to file               │
│   • summary or 5                      Display merged final results for all   │
│ scanned targets                                                              │
│   • cats or 4                         List all available categories &        │
│ modules                                                                      │
│   • clear                           Clear the console screen                 │
│   • exit or 0                           Quit Shadowseek                      │
╰──────────────────────────────────────────────────────────────────────────────╯

Shadowseek > afnanothayi232500@gmail.com
```

### 1. Side-by-Side Dual-Panel Layout (Non-Table Design)
During active investigations, results are rendered side-by-side in distinct rounded aesthetic cards rather than rigid tabular spreadsheets:
- **Left Panel (Registered / Hits)**: Shows confirmed account registrations grouped by category, accompanied by rich metadata trees (avatars, bio links, streaks, IDs).
- **Right Panel (Skipped Loud Modules)**: Highlights skipped high-noise services that trigger password reset notifications or emails, allowing selective one-click verification.

```text
╭────────────────── RESULTS / REGISTERED (15) ──────────────────╮ ╭─────────── SKIPPED (38) - LOUD MODULES ────────────╮
│ == COMMUNITY ==                                               │ │ ~ Babestation (Adult)    ~ Cv.ee (Jobs)            │
│   ✔ Quora: Registered                                         │ │ ~ Fantasia (Adult)       ~ Pulser (Jobs)           │
│       └── email_confirmed: True                               │ │ ~ Flirtbate (Adult)      ~ Cv.lv (Jobs)            │
│                                                               │ │ ~ Made.porn (Adult)      ~ Programminghub          │
│ == CREATOR ==                                                 │ │                          (Learning)                │
│   ✔ Canva: Registered                                         │ │ ~ Sexvid (Adult)         ~ Bnrlanguages (Learning) │
│   ✔ Figma: Registered                                         │ │ ~ Buymeacoffee (Creator) ~ Bunpo (Learning)        │
│                                                               │ │ ~ Payhip (Creator)       ~ Talkpal (Learning)      │
│ == DEV ==                                                     │ │ ~ Luarocks (Dev)         ~ Cambly (Learning)       │
│   ✔ Wix: Registered                                           │ │ ~ Medium (Dev)           ~ Hanzii (Learning)       │
│                                                               │ │ ~ Finch (Fitness)        ~ Indiatimes (News)       │
│ == ENTERTAINMENT ==                                           │ │ ~ Jobs.cz (Jobs)         ~ Amazon (Shopping)       │
│   ✔ Letterboxd: Registered                                    │ ╰─────────────── Type 'loud' to scan ────────────────╯
│                                                               │
│ == LEARNING ==                                                │
│   ✔ Coursera: Registered                                      │
│   ✔ Duolingo: Registered                                      │
│       ├── streak: 0                                           │
│       └── avatar: https://simg-ssl.duolingo.com/avatar/...    │
╰───────────────────────────────────────────────────────────────╯
```

### 2. Consolidated Master Summary
Type `summary` (or `5`), execute `loud` scanning, or exit the interactive console to view the **Consolidated Final Results** card. It merges all scanned targets, presents clean category counts, and prints an alphabetical multi-column platform checklist:

```text
╭────────────────────────────────── SHADOWSEEK - CONSOLIDATED FINAL RESULTS ───────────────────────────────────╮
│ Target (Email): afnanothayi232500@gmail.com  •  15 registered accounts found                                 │
│                                                                                                              │
│   • COMMUNITY (1): Quora                                                                                     │
│   • CREATOR (2): Canva, Figma                                                                                │
│   • DEV (1): Wix                                                                                             │
│   • ENTERTAINMENT (1): Letterboxd                                                                            │
│   • LEARNING (2): Coursera, Duolingo                                                                         │
│   • MUSIC (1): Gaana                                                                                         │
│   • NEWS (1): Indiatimes                                                                                     │
│   • OTHER (1): Office365                                                                                     │
│   • SHOPPING (1): Amazon                                                                                     │
│   • SOCIAL (4): Facebook, Instagram, Pinterest, X (twitter)                                                  │
│                                                                                                              │
│ ✔ Amazon                    ✔ Facebook                  ✔ Pinterest                                          │
│ ✔ Canva                     ✔ Figma                     ✔ Quora                                              │
│ ✔ Coursera                  ✔ Gaana                     ✔ Wix                                                │
│ ✔ Duolingo                  ✔ Instagram                 ✔ X (twitter)                                        │
│                                                                                                              │
╰──────────────────────────────────────────── Developed by govind ─────────────────────────────────────────────╯
```

---

## 🚀 Key Features

| Capability | Details |
|---|---|
| **Interactive REPL** | Full-featured command console with persistent context, selective loud scanning, and command shortcuts (`loud`, `export`, `summary`, `cats`). |
| **Side-by-Side Dual View** | Sleek rounded terminal cards cleanly separating verified account hits from skipped loud modules without ugly tabular grids. |
| **Consolidated Final Dashboard** | Merges multiple targets, category breakdowns, and platform checklists into a unified master report on scan completion or exit. |
| **150+ Modular Platforms** | Extensive coverage spanning Social, Dev, Community, Creator, Gaming, Learning, Adult, Jobs, Music, and Shopping domains. |
| **Stealth & Anti-Fingerprinting** | Powered by asynchronous HTTP/2 and `curl_cffi` browser TLS fingerprint impersonation to bypass bot blocks and Cloudflare traps. |
| **Cross-Scanning & Deep Pivots** | Recursively extracts personal websites, bios, and verified accounts; features multi-path routing (e.g. LinkedIn personal profiles vs company pages). |
| **Hudson Rock Cyber Intel** | `--hudson` flag directly queries Hudson Rock's infostealer database for stolen credentials and infected machines tied to email targets. |
| **Native MCP Server Support** | Built-in Model Context Protocol server exposing username/email reconnaissance to Claude Desktop, Claude Code, and autonomous AI agents. |
| **Forensic Multi-Format Reports** | Auto-formats exportable reports to **PDF** (complete with avatars & metadata trees), structured **JSON**, and **CSV**. |

---

## 🛠️ Usage & CLI Reference

### 1. Interactive REPL (Recommended)
```bash
shadowseek
```
Inside the prompt:
- Enter any username (e.g. `johndoe`) or email (e.g. `john@example.com`).
- Enter `loud` or `2` to scan skipped loud modules for the current target.
- Enter `export pdf`, `export json`, or `export csv` (or `3`) to save reports.
- Enter `summary` or `5` to view the merged master dashboard.
- Enter `cats` or `4` to list all supported categories and modules.
- Enter `clear` to reset the terminal screen.
- Enter `exit` or `0` to quit with an automated session summary.

### 2. Command-Line Scanning Flags
```bash
# Scan username across all platforms
shadowseek -u johndoe

# Scan email across all platforms
shadowseek -e target@example.com

# Target specific categories
shadowseek -u johndoe -c dev,social
shadowseek -e target@example.com -c creator

# Target specific modules
shadowseek -u johndoe -m github,reddit,linkedin
shadowseek -e target@example.com -m coursera,duolingo

# Include loud modules directly
shadowseek -e target@example.com --allow-loud

# Enable deep cross-scanning (follow links & bio pivots)
shadowseek -u johndoe --cross-scan --cross-depth 2

# Check breach & infostealer telemetry
shadowseek -e target@example.com --hudson

# Generate reports
shadowseek -u johndoe -f pdf -o johndoe_report.pdf
shadowseek -e target@example.com -f json -o target.json
shadowseek -e target@example.com -f csv -o target.csv

# Batch scan from file
shadowseek -uf targets_usernames.txt
shadowseek -ef targets_emails.txt
```

### Full CLI Options

| Flag / Option | Argument | Description |
|---|---|---|
| `-u, --username` | `<name>` | Single username to enumerate across all modules |
| `-e, --email` | `<addr>` | Single email to check for registration and leaks |
| `-uf, --username-file` | `<file>` | Path to a text file containing usernames (one per line) |
| `-ef, --email-file` | `<file>` | Path to a text file containing emails (one per line) |
| `-c, --category` | `<cats>` | Comma-separated list of categories to scan (e.g. `dev,social`) |
| `-m, --module` | `<mods>` | Comma-separated list of specific modules to scan (e.g. `github,x`) |
| `-i, --interactive` | — | Explicitly start the interactive REPL session |
| `--allow-loud` | — | Enable scanning of loud modules that trigger notifications/resets |
| `--cross-scan` | — | Follow links, handles, and verified accounts exposed in results |
| `--cross-depth` | `<int>` | Number of recursive pivot rounds (default: `1`) |
| `--cross-links` | `<type>` | Pivot link filter: `all`, `verified`, or `none` (default: `all`) |
| `--cross-emails` | `<type>` | Pivot email filter: `all`, `verified`, or `none` (default: `verified`) |
| `--hudson` | — | Query Hudson Rock infostealer intelligence API |
| `-f, --format` | `<fmt>` | Report output format: `pdf`, `json`, or `csv` |
| `-o, --output` | `<path>` | Custom output file destination |
| `-C, --concurrency` | `<int>` | Custom concurrency worker limit (default: `60` user, `25` email) |
| `-t, --timeout` | `<sec>` | HTTP request timeout in seconds (default: `10.0`) |
| `-d, --delay` | `<sec>` | Delay in seconds between requests for stealth/rate-limits |
| `-P, --proxy-file` | `<path>` | Path to proxy file (HTTP, SOCKS5) |
| `--no-nsfw` | — | Exclude adult and NSFW platforms from the scan |
| `-lu, --list-user` | — | Display all available username modules |
| `-le, --list-email` | — | Display all available email modules |
| `--version` | — | Show version and creator attribution |

---

## 🌐 Supported Platform Categories

Shadowseek organizes 150+ individual platform modules across targeted categories:

| Category | Example Platforms |
|---|---|
| **Community** | Quora, Reddit, StackOverflow, Disboard, HackerNews |
| **Creator** | Patreon, Substack, Medium, Gumroad, Luma, BuyMeACoffee, Ko-fi |
| **Developer** | GitHub, GitLab, DockerHub, Bitbucket, Wix, Replit, PyPI, NPM |
| **Social** | X (Twitter), Instagram, Facebook, Pinterest, Mastodon, Bluesky, LinkedIn |
| **Entertainment** | Letterboxd, Spotify, SoundCloud, YouTube, Twitch, Netflix, Crunchyroll |
| **Learning** | Coursera, Duolingo, Codecademy, Cambly, Talkpal |
| **Gaming** | Steam, Roblox, Chess.com, EpicGames, Minecraft |
| **Shopping** | Amazon, eBay, Flipkart, Etsy |
| **Jobs & Career** | LinkedIn Personal (`/in/`), LinkedIn Company (`/company/`), Freelancer, Upwork |
| **Adult (Opt-in)** | Adult webcam and content platforms *(filtered by default with `--no-nsfw`)* |

---

## 🤖 Model Context Protocol (MCP) Server

Shadowseek includes a first-class **MCP Server** that exposes username and email intelligence directly to AI tools such as **Claude Desktop**, **Claude Code**, and agentic LLM pipelines.

### Setup with Claude Desktop
Add the server definition to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "shadowseek": {
      "command": "python",
      "args": ["-m", "user_scanner.mcp.server"]
    }
  }
}
```

### Setup with Claude Code
```bash
claude mcp add shadowseek python -m user_scanner.mcp.server
```

Once registered, your AI assistant can directly invoke Shadowseek to investigate targets, correlate identities across platforms, and extract verified social handles.

---

## 👤 Creator & Maintainer

Created and actively developed by **govind**:
- **GitHub**: [Govind-v-kartha](https://github.com/Govind-v-kartha)
- **Portfolio**: [govind-v-kartha.vercel.app](https://govind-v-kartha.vercel.app/)
- **Project Repository**: [Govind-v-kartha/ShadowSeek](https://github.com/Govind-v-kartha/ShadowSeek)

---

## ⚖️ Legal Disclaimer

> **Notice**: Shadowseek is designed for legal, ethical, and authorized security assessments, digital forensic investigations, and defensive open-source intelligence gathering only. Users are responsible for complying with all local, state, and international laws when using this tool. The creator assumes no liability for misuse or damage caused by this software.

---

## 📄 License

This project is open-source and licensed under the [MIT License](LICENSE) — free for personal, educational, and commercial use.
