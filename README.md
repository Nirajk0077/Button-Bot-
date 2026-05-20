# Premium Button Bot

This is a premium-feeling Telegram bot created using `pyrofork`. It features shareable buttons, an auto/manual mode toggle, and various buttons like Channel, About, Settings, Help, and a dedicated CMD button containing other commands.

## Features
- Built with `pyrofork` (https://github.com/SilentXBotz/pyrofork)
- Welcome message with image spoiler support
- Buttons: Channel, About, Setting, Help, CMD
- Nested commands under the CMD button
- Mode toggle (Auto/Manual)
- Shareable URLs
- Ready for deployment on Render, Railway, Koyeb

## Deployment

### Render
You can deploy this bot on Render using the provided `render.yaml` or by connecting your GitHub repository and creating a Background Worker.
- Build Command: `pip install -r requirements.txt`
- Start Command: `python main.py`

### Railway
You can deploy this bot on Railway by connecting your GitHub repository. The provided `railway.json` or `Procfile` will handle the setup.
- Start Command: `python main.py`

### Koyeb
You can deploy this bot on Koyeb by connecting your GitHub repository or using the provided `Dockerfile`.
- Build from Dockerfile or use Buildpack with `Procfile`.
- Command: `python main.py`

## Configuration
Before running the bot, make sure to update the following variables in `main.py`:
- `api_id`: Your Telegram API ID
- `api_hash`: Your Telegram API Hash
- `bot_token`: Your Telegram Bot Token

## Installation (Local)
1. Clone the repository
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the bot:
   ```bash
   python main.py
   ```
