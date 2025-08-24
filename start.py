def start_command(update, context):
    update.message.reply_text("✅ Welcome to AlphaMapRobot!\nType /help to see all Nmap command options.")

def help_command(update, context):
    help_text = """
📌 *AlphaMapRobot Help (Nmap Commands)*

Use the `/scan <options> <target>` command.

Examples:
- `/scan -sS example.com`  → SYN Scan
- `/scan -p 80,443 example.com`  → Scan ports 80 and 443
- `/scan -A example.com`  → OS Detection & Version Scan
- `/scan -O example.com`  → OS Fingerprinting
- `/scan -sV example.com`  → Service Version Detection
- `/scan --script vuln example.com`  → Run Vulnerability Scripts

✅ *Common Options*:
- `-p` → Specify Ports (e.g., `-p 1-1000`)
- `-sS` → SYN Scan
- `-sU` → UDP Scan
- `-sV` → Service Version Detection
- `-O` → OS Detection
- `-A` → Aggressive Scan (OS + Version + Traceroute)
- `-T4` → Speed up the scan
- `--script` → Use NSE scripts

Example full scan:
`/scan -sS -sV -A -T4 example.com`

⚠ Use responsibly. Only scan targets you own or have permission to test.
"""
    update.message.reply_text(help_text, parse_mode="Markdown")
