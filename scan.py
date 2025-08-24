import subprocess

def scan_command(update, context):
    if not context.args:
        update.message.reply_text("❌ Usage: /scan <nmap options> <target>\nExample: /scan -sV example.com")
        return

    # Join user-provided arguments into one command
    user_command = context.args

    # Basic security check (only allow commands starting with '-' or valid targets)
    if any(';' in arg or '&&' in arg or '|' in arg for arg in user_command):
        update.message.reply_text("❌ Invalid characters detected!")
        return

    try:
        # Construct the nmap command
        command = ["nmap"] + user_command

        # Run the command
        result = subprocess.run(command, capture_output=True, text=True, timeout=60)

        # Limit output to Telegram's max message size (4096 chars)
        output = result.stdout if result.stdout else result.stderr
        if len(output) > 4000:
            output = output[:4000] + "\n\n⚠ Output truncated."

        update.message.reply_text(f"✅ Scan Results:\n```\n{output}\n```", parse_mode="Markdown")
    except subprocess.TimeoutExpired:
        update.message.reply_text("❌ Scan timed out (max 60 seconds).")
    except Exception as e:
        update.message.reply_text(f"❌ Error: {e}")
