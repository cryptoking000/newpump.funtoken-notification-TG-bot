import asyncio
import websockets
import json
import os
import telegram
from telegram.constants import ParseMode
from telegram import Update
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import aiohttp
load_dotenv()
TOKEN = os.getenv("TOKEN")

running = False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global running
    running = True
    await update.message.reply_text('Starting real-time messages...')
    await subscribe(update, context)

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global running
    running = False
    await update.message.reply_text('Stopped real-time messages.')

async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uri = "wss://pumpportal.fun/api/data"
    async with websockets.connect(uri) as websocket:
        
        # Subscribing to token creation events
        payload = {
            "method": "subscribeNewToken",
        }
        await websocket.send(json.dumps(payload))

        # Subscribing to trades made by accounts
        payload = {
            "method": "subscribeAccountTrade",
            "keys": ["AArPXm8JatJiuyEffuC1un2Sc835SULa4uQqDcaGpAjV"]  # array of accounts to watch
        }
        await websocket.send(json.dumps(payload))

        # Subscribing to trades on tokens
        payload = {
            "method": "subscribeTokenTrade",
            "keys": ["91WNez8D22NwBssQbkzjy4s2ipFrzpmn5hfvWVe2aY5p"]  # array of token CAs to watch
        }
        await websocket.send(json.dumps(payload))
        
        while running:
            try:
                message = await websocket.recv()
                data = json.loads(message)
                
                # Create styled message based on transaction type
                if data.get("txType") == "create":
                    # Get metadata URI and parse for image
                    uri = data.get('uri', '')
                    print(uri)
                    image_url = ''
                    if uri:
                        try:
                            async with aiohttp.ClientSession() as session:
                                async with session.get(uri) as response:
                                    metadata = await response.json()
                                    image_url = metadata.get('image', '')
                                    print("image_url", image_url)
                        except:
                            pass

                    formatted_message = (f"🚀 <b>{data.get('name', 'Unknown')}</b> (${data.get('symbol', 'N/A')})\n"
                        f"💎 Buy: <code>{data.get('initialBuy', 0):,.0f}</code> | SOL: <code>{data.get('solAmount', 0):,.2f}</code>◎ | MC: <code>{data.get('marketCapSol', 0):,.2f}</code>◎\n"
                        f"🏦 Pool: {data.get('pool', 'N/A').upper()} | 🔗 <code>{data.get('mint', 'N/A')[:8]}...</code>\n"
                        f"🌊 BC: <code>{data.get('vTokensInBondingCurve', 0):,.0f}</code> tokens, <code>{data.get('vSolInBondingCurve', 0):,.2f}</code>◎"
                    )

                    # Send image first if available
                    if image_url:
                        await update.message.reply_photo(
                            photo=image_url,
                            caption=formatted_message,
                            parse_mode=ParseMode.HTML
                        )
                    else:
                        await update.message.reply_text(
                            formatted_message,
                            parse_mode=ParseMode.HTML
                        )
                else:
                    # Handle other transaction types...
                    formatted_message = json.dumps(data, indent=2)
                    await update.message.reply_text(
                        formatted_message,
                        parse_mode=ParseMode.HTML
                    )
            except websockets.exceptions.ConnectionClosed:
                break
def main():
    try:
        application = ApplicationBuilder().token(TOKEN).concurrent_updates(True).build()
        
        # Add command handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("stop", stop))

        print("👟👟Bot is running...")
        application.run_polling(allowed_updates=Update.ALL_TYPES)
       
    except Exception as e:
        print(f"Fatal error: {e}")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped by user")
    except Exception as e:
        print(f"Fatal error: {e}")
