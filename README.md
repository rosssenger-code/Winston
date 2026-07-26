# 🐾 Winston the French Bulldog Discord Bot

A fun and interactive Discord bot that acts as Winston, your charming French Bulldog friend! Winston responds to your messages with personality, charm, and plenty of French Bulldog attitude.

## Features

✨ **Smart Personality System** - Winston responds contextually based on keywords in your messages
- Greetings: Enthusiastic and tail-waggy responses
- Compliments: Winston gets excited when you praise him
- Questions: Winston thinks deeply about your questions (in his doggy way)
- Playtime: High-energy responses when you mention games
- Food/Treats: Nothing gets Winston more excited than snacks!
- Emotions: Winston responds sympathetically when you're sad

🎮 **Special Commands**
- `!woof` - Make Winston bark!
- `!pet` - Pet Winston and get a happy response
- `!treat` - Give Winston a treat
- `!about` - Learn about Winston

💬 **Natural Chat** - Just message Winston naturally and he'll respond as a French Bulldog would!

## Installation

### Prerequisites
- Python 3.8+
- A Discord bot token (from Discord Developer Portal)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rosssenger-code/Winston.git
   cd Winston
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your bot token:**
   - Create a `.env` file in the root directory
   - Add your Discord bot token:
     ```
     DISCORD_TOKEN=your_bot_token_here
     ```

4. **Run the bot:**
   ```bash
   python winston_bot.py
   ```

## How to Create a Discord Bot Token

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name (e.g., "Winston")
3. Go to the "Bot" tab and click "Add Bot"
4. Under TOKEN, click "Copy" to copy your bot token
5. Paste it in your `.env` file
6. Go to OAuth2 > URL Generator
7. Select scopes: `bot`
8. Select permissions: `Send Messages`, `Read Messages/View Channels`
9. Copy the generated URL and use it to invite Winston to your server

## Usage

Once Winston is running and in your Discord server:

### Chat naturally with Winston:
```
You: Hey Winston!
Winston: *wags tail excitedly* WOOF WOOF! Hey there, buddy! 🐾

You: Wanna play?
Winston: *runs in circles* YES YES YES! PLAYTIME?! LET'S GO! 🏃‍♂️🏃‍♂️

You: Got any treats?
Winston: *perks up nose* DID SOMEONE SAY FOOD?! I LOVE FOOD! 🍖
```

### Use special commands:
```
!woof       - Listen to Winston bark
!pet        - Pet Winston
!treat      - Give Winston a treat
!about      - Learn about Winston
```

## Customization

Want to add more of Winston's personality? Edit the `WINSTON_TRAITS` dictionary in `winston_bot.py`:

```python
WINSTON_TRAITS = {
    "your_keyword": [
        "Response 1 🐾",
        "Response 2 🐶",
        "Response 3 🎾",
    ],
}
```

Then add keyword detection in the `generate_winston_response()` function.

## File Structure

```
Winston/
├── winston_bot.py      # Main bot script
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (add your token here)
└── README.md          # This file
```

## Troubleshooting

**Bot doesn't respond:**
- Make sure your bot token is correct in `.env`
- Verify the bot has permissions to see and send messages
- Check that the bot is in your Discord server

**ModuleNotFoundError:**
```bash
pip install -r requirements.txt
```

**Bot keeps disconnecting:**
- Check your internet connection
- Make sure your token is still valid

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork and submit pull requests to improve Winston!

---

Made with ❤️ and lots of snorts 🐾
