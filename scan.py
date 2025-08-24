import subprocess

def scan_command(update, context):
    if len(context.args) == 0:
        update.message.reply_text("Usage: /scan <nmap options> <target>")
        return

    command = ["nmap"] + context.args
    update.message.reply_text(f"🔍 Running scan: {' '.join(command)}")

    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        if len(result) > 4000:  # Telegram message limit
            update.message.reply_text("Output too large. Sending as file...")
            with open("scan_result.txt", "w") as f:
                f.write(result)
            update.message.reply_document(open("scan_result.txt", "rb"))
        else:
            update.message.reply_text(f"```\n{result}\n```", parse_mode="Markdown")
    except subprocess.CalledProcessError as e:
        update.message.reply_text(f"Error: {e.output}")
