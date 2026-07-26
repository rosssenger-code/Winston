from dotenv import load_dotenv
  import discord
  import os

  # load environment variables from .env file
  load_dotenv()

  #Set up intents
  intents = discord.Intents.default()
  intents.message_content = True # Ensure that the bot can read message content

  @client.event
  async def on_ready():
    print('we have logged in as {0.user}'.format(clien

  @client.event
  async def on_message(message):
      if message.author == client.user:
            return

      if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))
