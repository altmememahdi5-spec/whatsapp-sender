# WhatsApp Sender (PyQt5 + Flask + WhatsApp Cloud API)

A desktop app to send and receive WhatsApp messages using WhatsApp Cloud API. It includes:
- PyQt5 GUI (conversations, chat view, composer)
- Flask webhook server at `http://127.0.0.1:5000/webhook`
- SQLite storage for contacts and messages
- Support for freeform replies (within 24h) and template messages

## Requirements
- Python 3.9+
- Windows/macOS/Linux

## Install
```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Configure Meta (WhatsApp Cloud API)
1. In Meta Developer portal, create an app and set up WhatsApp Cloud API.
2. Get your:
   - Permanent Access Token
   - Phone Number ID
   - WhatsApp Business Account ID (WABA ID)
3. Set a Verify Token (any secret you choose) and put it in the app Settings.
4. Configure Webhook URL: `http://YOUR_PUBLIC_TUNNEL/webhook` and verify using your Verify Token.
   - For local dev, use a tunnel like `ngrok http 5000` or `cloudflared tunnel --url http://localhost:5000`.
   - Add subscriptions for `messages`.

## Running (Dev)
```bash
python main.py
```
Open File → Settings and paste:
- Access Token
- Phone Number ID
- WABA ID
- Verify Token
- Webhook Port (default 5000)

## Build Windows Installer (.exe)
Prereqs:
- Windows 10/11
- Python 3.9+
- Inno Setup 6 (optional, for installer; download and install)

Steps:
```powershell
# From project root
powershell -ExecutionPolicy Bypass -File .\build\build.ps1
```
Outputs:
- Portable app: `dist/WhatsAppSender/WhatsAppSender.exe`
- Installer (if Inno Setup installed): `dist/WhatsAppSender-Setup.exe`

If Inno Setup is not installed, the script will only build the portable app.

## Notes
- Templates are fetched via the WABA ID and current Graph API version from settings.
- Basic desktop notifications are shown for new messages.
- Errors from the API are shown in dialogs.

## Troubleshooting
- If sending fails with 400/401, check Access Token validity and permissions.
- If replies fail outside 24h, use a template.
- Ensure your webhook is verified and subscribed to messages.
