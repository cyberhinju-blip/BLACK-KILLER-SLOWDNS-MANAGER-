<div align="center">

```
██████╗ ██╗      █████╗  ██████╗██╗  ██╗    ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝    ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗
██████╔╝██║     ███████║██║     █████╔╝     █████╔╝ ██║██║     ██║     █████╗  ██████╔╝
██╔══██╗██║     ██╔══██║██║     ██╔═██╗     ██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗    ██║  ██╗██║███████╗███████╗███████╗██║  ██║
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
```

# BLACK KILLER SSH TUNNEL MANAGER

### ⚡ DNSTT Ultra Speed Edition — v9.2.3

[![Version](https://img.shields.io/badge/Version-9.2.3-red?style=for-the-badge)](https://github.com/cyberhinju-blip/BLACK-KILLER-SLOWDNS-MANAGER-)
[![Shell](https://img.shields.io/badge/Shell-Bash-green?style=for-the-badge&logo=gnu-bash)](https://github.com/cyberhinju-blip/BLACK-KILLER-SLOWDNS-MANAGER-)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-+255658785522-25D366?style=for-the-badge&logo=whatsapp)](https://wa.me/255658785522)

**Created By BLACK KILLER 👑**

</div>

---

## ⚡ Quick Install (One Command)

```bash
wget -O slowdns_script.sh https://raw.githubusercontent.com/cyberhinju-blip/BLACK-KILLER-SLOWDNS-MANAGER-/main/slowdns_script.sh && chmod +x slowdns_script.sh && sudo bash slowdns_script.sh
```

Or with curl:

```bash
curl -o slowdns_script.sh https://raw.githubusercontent.com/cyberhinju-blip/BLACK-KILLER-SLOWDNS-MANAGER-/main/slowdns_script.sh && chmod +x slowdns_script.sh && sudo bash slowdns_script.sh
```

---

## 📋 Requirements

- **OS:** Ubuntu 18.04 / 20.04 / 22.04 / 24.04 — Debian 10/11/12 — CentOS 7/8
- **Access:** Root (`sudo`)
- **RAM:** Minimum 512MB
- **DNS Records:** A record + NS record pointing to your VPS

---

## 🌐 DNS Records Setup

```
A  Record:   ns.yourdomain.com  →  YOUR_SERVER_IP
NS Record:   t.yourdomain.com   →  ns.yourdomain.com
```

---

## 🎯 Main Menu

```
◇────────────────────────────────────────────────────────◇
  VERSION: 9.2.3 ULTRA DIAMOND | CREATED BY BLACK KILLER
◇────────────────────────────────────────────────────────◇

  1)  🌐 DNSTT MANAGEMENT
  2)  👥 SSH USERS
  3)  🖥️  SYSTEM TOOLS
  0)  ⛔ EXIT
```

### Quick Access Commands (after first run)

```bash
menu      # Open main menu
dnstt     # Open directly
slowdns   # Open directly
```

---

## 🌐 DNSTT Management (14 Options)

| # | Feature |
|---|---------|
| 1 | 📦 Install / Setup DNSTT |
| 2 | 📊 View Status |
| 3 | 📋 Connection Info + Client Config |
| 4 | 📖 View Logs |
| 5 | ⚡ Performance Monitor |
| 6 | 📈 Real-Time Statistics |
| 7 | 🌐 Bandwidth Test |
| 8 | 🔧 Fix Domain Issue |
| 9 | 🔍 Troubleshoot |
| 10 | 🔄 Restart Service |
| 11 | 💾 Backup Configuration |
| 12 | 📥 Restore Configuration |
| 13 | ⏹️ Stop Service |
| 14 | 🗑️ Uninstall |

### MTU Options

| MTU | Mode | Speed |
|-----|------|-------|
| 512 | Classic DNS | Most Compatible ✓ |
| 1024 | Standard | Balanced |
| 1232 | EDNS0 Standard | Good |
| 1280 | High Speed | Fast ⭐ |
| 1420 | Very High Speed | Best for SSH ⭐⭐ |
| 4096 | EDNS0 Maximum | Ultra ⚡ |
| Custom | Manual | Advanced |

---

## 👥 SSH User Management (10 Options)

| # | Feature |
|---|---------|
| 1 | 👤 Add New User |
| 2 | 📋 List All Users |
| 3 | 🔄 Renew User |
| 4 | 🔒 Lock Account |
| 5 | 🔓 Unlock Account |
| 6 | 🖥️ SSH Banner |
| 7 | ♻️ Auto-Renew Settings |
| 8 | 📊 Auto-Renew Status |
| 9 | 💾 Backup & Restore |
| 10 | 🗑️ Delete User |

### User Creation Options

```
USERNAME       : your_choice
PASSWORD       : your_choice
DURATION       : 1 / 7 / 30 / 90 / 365 days
CONN LIMIT     : 0 = unlimited, or set a number
DATA LIMIT     : 0 = unlimited (GB)
AUTO-RENEW     : disabled / 1 day / 3 days / 7 days before expiry
```

### User Database

Users stored in `/etc/slowdns/users.txt` — 9 fields:

```
username|password|expiry|created|gb_limit|status|ar_days|ar_trigger|conn_limit
```

---

## 🖥️ System Tools (5 Options)

| # | Feature |
|---|---------|
| 1 | 📊 VPS Info Panel |
| 2 | ⚙️ Server Optimizer |
| 3 | 👁️ SSH Connection Monitor (real-time) |
| 4 | 🧹 Expired Users Cleaner |
| 5 | 🔄 Script Auto-Updater |

---

## 🔑 Client Configuration

### DNSTT UDP Mode

```bash
dnstt-client -udp YOUR_SERVER_IP:5300 \
  -pubkey YOUR_PUBLIC_KEY \
  -mtu 512 \
  YOUR_TUNNEL_DOMAIN

# Then connect SSH
ssh -D 1080 -p 22 username@127.0.0.1
```

---

## 🔧 SSH Optimization Applied

This script automatically optimizes your SSH server for DNS tunneling:

```
TCPKeepAlive      yes              # Keep tunnel alive
ClientAliveInterval 20            # Ping every 20 seconds
RekeyLimit        32M 15m         # Short rekey = no stalls
MaxSessions       500             # Many users supported
MaxStartups       200:30:1000     # High concurrency
Ciphers           chacha20-poly1305 first (lowest overhead)
MACs              ETM-only (fastest per-packet)
Compression       delayed (more payload per DNS query)
```

---

## 🚨 Emergency Recovery

If users are locked out, run this on the server:

```bash
sed -i 's/|locked|/|active|/g' /etc/slowdns/users.txt; screen -r -S limiter_daemon -X quit 2>/dev/null; rm -f /etc/slowdns/limiter_autostart /etc/slowdns/limiter_daemon.sh; echo DONE
```

---

## 🔄 Update Script

```bash
wget -O /usr/local/bin/menu https://raw.githubusercontent.com/cyberhinju-blip/BLACK-KILLER-SLOWDNS-MANAGER-/main/slowdns_script.sh && chmod +x /usr/local/bin/menu && echo "Updated OK"
```

---

## 📝 Changelog

| Version | Changes |
|---------|---------|
| v9.2.3 | Upgraded SSH optimization block: MaxSessions/MaxStartups/RekeyLimit/ClientAlive/PrintMotd |
| v9.2.2 | Restored conn_limit prompt; clean sshd conflict |
| v9.2.1 | Fixed kick-out bug — `exit`→`return` in `/etc/profile.d` MOTD script |
| v9.2.0 | Removed multi-login limiter daemon; added emergency recovery one-liner |
| v9.1.0 | Remove multi-login limiter daemon completely |
| v9.0.0 | Initial BLACK KILLER release — Ultra Diamond Edition |

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=cyberhinju-blip/BLACK-KILLER-SLOWDNS-MANAGER-&type=Date)](https://star-history.com/#cyberhinju-blip/BLACK-KILLER-SLOWDNS-MANAGER-&Date)

---

<div align="center">

**Created By BLACK KILLER 👑 💯**

*Ultra Diamond Edition — Fast, Clean, No Limits*

[![WhatsApp](https://img.shields.io/badge/Contact-WhatsApp%20%2B255658785522-25D366?style=for-the-badge&logo=whatsapp)](https://wa.me/255658785522)
[![GitHub](https://img.shields.io/badge/GitHub-cyberhinju--blip-black?style=for-the-badge&logo=github)](https://github.com/cyberhinju-blip)

</div>
