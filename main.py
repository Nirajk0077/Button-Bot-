import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

api_id = int(os.environ.get("API_ID", 123456))
api_hash = os.environ.get("API_HASH", "your_api_hash")
bot_token = os.environ.get("BOT_TOKEN", "your_bot_token")

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Auto mode setting
auto_mode = True

@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Channel", url="https://t.me/your_channel"),
                InlineKeyboardButton("About", callback_data="about")
            ],
            [
                InlineKeyboardButton("Setting", callback_data="setting"),
                InlineKeyboardButton("Help", callback_data="help")
            ],
            [
                InlineKeyboardButton("CMD", callback_data="cmd"),
                InlineKeyboardButton("Share", switch_inline_query="Check out this Premium Bot!")
            ]
        ]
    )
    
    welcome_text = "Welcome to the Premium Button Bot!\nThis bot supports URL and inline buttons."
    
    # Send a welcome photo with spoiler
    image_url = os.environ.get("WELCOME_IMAGE_URL", "https://i.ibb.co/twqrWB97/photo-2026-05-20-21-48-32-7642094223839199252.jpg")
    await message.reply_photo(
        photo=image_url, 
        caption=welcome_text, 
        reply_markup=keyboard, 
        has_spoiler=True
    )

@app.on_callback_query()
async def callback_handler(client: Client, query):
    global auto_mode
    data = query.data
    
    if data == "about":
        await query.answer("This is a custom premium bot.", show_alert=True)
    elif data == "setting":
        mode_text = "Auto" if auto_mode else "Manual"
        setting_keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(f"Mode: {mode_text}", callback_data="toggle_mode")],
                [InlineKeyboardButton("Back", callback_data="back")]
            ]
        )
        await query.edit_message_caption("Settings:", reply_markup=setting_keyboard)
    elif data == "toggle_mode":
        auto_mode = not auto_mode
        mode_text = "Auto" if auto_mode else "Manual"
        setting_keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(f"Mode: {mode_text}", callback_data="toggle_mode")],
                [InlineKeyboardButton("Back", callback_data="back")]
            ]
        )
        await query.edit_message_caption("Settings:", reply_markup=setting_keyboard)
    elif data == "help":
        await query.answer("Help menu coming soon!", show_alert=True)
    elif data == "cmd":
        cmd_keyboard = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Command 1", callback_data="cmd1")],
                [InlineKeyboardButton("Command 2", callback_data="cmd2")],
                [InlineKeyboardButton("Back", callback_data="back")]
            ]
        )
        await query.edit_message_caption("Available Commands:", reply_markup=cmd_keyboard)
    elif data == "back":
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Channel", url="https://t.me/your_channel"),
                    InlineKeyboardButton("About", callback_data="about")
                ],
                [
                    InlineKeyboardButton("Setting", callback_data="setting"),
                    InlineKeyboardButton("Help", callback_data="help")
                ],
                [
                    InlineKeyboardButton("CMD", callback_data="cmd"),
                    InlineKeyboardButton("Share", switch_inline_query="Check out this Premium Bot!")
                ]
            ]
        )
        await query.edit_message_caption("Welcome to the Premium Button Bot!\nThis bot supports URL and inline buttons.", reply_markup=keyboard)
    else:
        await query.answer("Unknown command.", show_alert=True)

class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Bot is healthy and running!')

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server_address = ('', port)
    httpd = HTTPServer(server_address, HealthCheckHandler)
    print(f"Health check server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    # Start the web server in a background thread
    threading.Thread(target=run_server, daemon=True).start()
    print("Bot started...")
    app.run()
