import requests
import os
import sys

CURRENT_VERSION = "1.0.0"
VERSION_URL = "https://example.com/version.txt"
TOOL_URL = "https://example.com/tool.py"
TOOL_FILENAME = "tool.py"

def check_for_update():
    try:
        response = requests.get(VERSION_URL)
        latest_version = response.text.strip()

        if latest_version != CURRENT_VERSION:
            print(f"[UPDATE] A new version ({latest_version}) is available.")
            download_update()
        else:
            print("[INFO] You are using the latest version.")
    except Exception as e:
        print(f"[ERROR] Failed to check for updates: {e}")

def download_update():
    try:
        response = requests.get(TOOL_URL)
        with open(TOOL_FILENAME, "wb") as file:
            file.write(response.content)
        print("[SUCCESS] The tool has been updated. Please restart it.")
        sys.exit()
    except Exception as e:
        print(f"[ERROR] Failed to download the update: {e}")

# --- Main Execution ---
check_for_update()

# --- Your Tool Code Below ---
print("[RUNNING] Tool is running...")
# Add your actual tool logic here
