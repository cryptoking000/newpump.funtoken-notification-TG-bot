Here's an awesome README template for your `newpump.funtoken-notification-TG-bot` GitHub repository:

---

# NewPump Fun Token Notification Telegram Bot

This Telegram bot provides real-time notifications for new tokens and trades from the Pump Portal API. It alerts users about token creation events and token trades, helping you stay ahead of trends in the crypto space!

## Features

- **Real-time notifications**: Get notified about new tokens and trading activity instantly.
- **Token creation alerts**: Receive detailed information about newly created tokens.
- **Trade monitoring**: Track token trades for specific accounts and token contracts.
- **Customizable**: Subscribe to different token contract addresses or accounts to watch.
- **Telegram integration**: Receive updates directly on Telegram in a user-friendly format, including token images when available.

## Requirements

- Python 3.8+
- `python-dotenv` for managing environment variables.
- `python-telegram-bot` library for Telegram integration.
- `aiohttp` for handling asynchronous HTTP requests.
- `websockets` for connecting to real-time data streams.
- A Telegram bot token (you can create one by chatting with [BotFather](https://core.telegram.org/bots#botfather)).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/newpump.funtoken-notification-TG-bot.git
   cd newpump.funtoken-notification-TG-bot
   ```

2. Create a `.env` file in the project root and add your Telegram bot token:
   ```env
   TOKEN=your-telegram-bot-token
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Start the Bot

To start receiving real-time notifications, simply send `/start` to your Telegram bot.

```bash
/start
```

The bot will subscribe to token creation events and trades.

### Stop Notifications

To stop receiving notifications, send `/stop` to the bot.

```bash
/stop
```

### Watching Specific Tokens and Accounts

You can customize which tokens and accounts the bot monitors by editing the relevant parts of the code. By default, the bot is set to watch a specific token contract and account. Modify the `payload` section in the `subscribe()` function to add more token contracts or accounts.

## Code Overview

### Main Bot Logic

- The bot listens to real-time data via WebSocket (`wss://pumpportal.fun/api/data`).
- Subscribes to the following events:
  - **New token creation** (`subscribeNewToken`).
  - **Account trades** (`subscribeAccountTrade`).
  - **Token trades** (`subscribeTokenTrade`).
  
### Messages

When the bot receives a token creation event, it formats the message with details such as:
- Token name and symbol
- Initial buy price and market cap
- Pool details
- Token image (if available)

### Commands

- `/start`: Starts the bot and subscribes to real-time notifications.
- `/stop`: Stops the bot and unsubscribes from the data stream.

## Running the Bot

To run the bot, execute the following command:

```bash
python bot.py
```

The bot will continuously run and send messages to Telegram until you stop it manually.

## Example Message

Here's an example of a message the bot might send upon detecting a new token:

```
🚀 <b>NewToken</b> ($NTK)
💎 Buy: <code>1,000</code> | SOL: <code>50.00</code>◎ | MC: <code>500.00</code>◎
🏦 Pool: MAIN | 🔗 <code>91WNez8D...</code>
🌊 BC: <code>500</code> tokens, <code>250.00</code>◎

```
![image](https://github.com/user-attachments/assets/b74cc5ef-fbfd-46de-b279-7b1c3faa7bb6)
![image](https://github.com/user-attachments/assets/eb0c216c-ed96-4d47-8c54-6cfd5f2df5e0)



If the token has an image, it will be sent alongside the message.

## Troubleshooting

- **Bot is not responding**: Check that your bot token is correct in the `.env` file and that you have an active internet connection.
- **WebSocket connection issues**: Ensure that the Pump Portal API is online and accessible.

## Contributing

Feel free to fork the repository and submit pull requests. If you have any ideas for improvements or encounter bugs, open an issue and I'll get back to you as soon as possible!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README provides a comprehensive guide for setting up, using, and understanding your Telegram bot project. Feel free to modify it based on additional features or details!
