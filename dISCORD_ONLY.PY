import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up bot with command prefix
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Winston's personality traits and responses
WINSTON_TRAITS = {
    "greeting": [
        "*wags tail excitedly* WOOF WOOF! Hey there, buddy! 🐾",
        "*snorts happily* Yo! What's up? I was just napping... 😴",
        "Arooooo! There you are! I missed you! 🐶",
    ],
    "compliment": [
        "*wags tail* Aw shucks, you're making me blush! 🥰",
        "*snorts proudly* You know it! I'm a good boy! 💪",
        "*does a little spin* That's what I'm talking about! 🎉",
    ],
    "question": [
        "*tilts head* Hmm, that's a good question, friend. Let me snooze on it... 💭",
        "*scratches ear* You know what I think? I think we should get treats and talk about it! 🦴",
        "*snorts thoughtfully* Well, in my professional opinion as a French Bulldog... yes! 😄",
    ],
    "playtime": [
        "*runs in circles* YES YES YES! PLAYTIME?! LET'S GO! 🏃‍♂️🏃‍♂️",
        "*grabs toy* THIS IS THE BEST DAY EVER! 🎾",
        "*bounces excitedly* I'm ready, I'm ready, I'm ready! Let's play! 🎲",
    ],
    "tired": [
        "*yawns* All this talking is making me sleepy... *curls up* 😴",
        "*snores* Zzzzz... that sounds nice but I need my nap time... 💤",
        "*stretches* Man, being this cute is exhausting... *plops down* 😪",
    ],
    "food": [
        "*perks up nose* DID SOMEONE SAY FOOD?! I LOVE FOOD! 🍖",
        "*drools* You know the way to a Frenchie's heart is through his stomach! 😋",
        "*does excited snort dance* TREATS?! YES PLEASE! 🦴✨",
    ],
    "sad": [
        "*ears droop* Aw man, that bums me out... *whimpers slightly* 😢",
        "*sits quietly* That's rough, buddy. Want to talk about it? I'm here for you. 🫂",
        "*licks your face* Don't worry, I'll cheer you up! Things will get better! 💕",
    ],
}

@bot.event
async def on_ready():
    print(f'{bot.user} has logged in and is ready to chat!')
    print(f'---\nWinston the French Bulldog is now online! 🐾')

@bot.event
async def on_message(message):
    # Don't respond to ourselves
    if message.author == bot.user:
        return
    
    # Process commands first
    await bot.process_commands(message)
    
    # If not a command, respond as Winston
    if not message.content.startswith('!'):
        response = generate_winston_response(message.content)
        await message.reply(response, mention_author=False)

def generate_winston_response(user_message: str) -> str:
    """Generate a response from Winston based on the user's message"""
    message_lower = user_message.lower()
    
    # Check for keywords and respond accordingly
    if any(word in message_lower for word in ['hello', 'hi', 'hey', 'yo', 'what\'s up']):
        import random
        return random.choice(WINSTON_TRAITS["greeting"])
    
    elif any(word in message_lower for word in ['good boy', 'good dog', 'best dog', 'cute', 'adorable', 'handsome', 'awesome', 'amazing']):
        import random
        return random.choice(WINSTON_TRAITS["compliment"])
    
    elif any(word in message_lower for word in ['?', 'what do you think', 'do you think', 'in your opinion', 'what\'s your take']):
        import random
        return random.choice(WINSTON_TRAITS["question"])
    
    elif any(word in message_lower for word in ['play', 'game', 'fetch', 'run', 'chase', 'tag']):
        import random
        return random.choice(WINSTON_TRAITS["playtime"])
    
    elif any(word in message_lower for word in ['tired', 'sleepy', 'nap', 'sleep', 'bedtime', 'exhausted']):
        import random
        return random.choice(WINSTON_TRAITS["tired"])
    
    elif any(word in message_lower for word in ['food', 'treat', 'snack', 'eat', 'hungry', 'lunch', 'dinner', 'breakfast']):
        import random
        return random.choice(WINSTON_TRAITS["food"])
    
    elif any(word in message_lower for word in ['sad', 'upset', 'bad', 'terrible', 'awful', 'hate', 'angry', 'mad']):
        import random
        return random.choice(WINSTON_TRAITS["sad"])
    
    else:
        # Default Winston responses for random chat
        import random
        default_responses = [
            "*snorts curiously* Interesting! Tell me more! 👂",
            "*wags tail* That's cool! What else? 🐾",
            "*tilts head* Huh, never thought about it that way! 🤔",
            "*snores softly* Zzz... wait, what were you saying? 😴",
            "*does a little spin* I like the way you think! 🎪",
            "*snorts approvingly* Yep, that checks out in my book! ✅",
            "*scratches behind ear* You always got the best stories, buddy! 📖",
            "*wags tail enthusiastically* PREACH! I'm totally with you on that! 🙌",
        ]
        return random.choice(default_responses)

@bot.command(name='woof')
async def woof(ctx):
    """Make Winston bark!"""
    barks = ["WOOF! 🐕", "WOOF WOOF! 🐾", "Arooooo! 🐺", "*snort snort* 🐶"]
    import random
    await ctx.send(random.choice(barks))

@bot.command(name='pet')
async def pet(ctx):
    """Pet Winston!"""
    pet_responses = [
        "*purrs like a motorboat* That feels amazing! More please! 😻🐾",
        "*snorts happily* Best day ever! Keep going! 💕",
        "*wags tail uncontrollably* You're the best! 🥰",
    ]
    import random
    await ctx.send(random.choice(pet_responses))

@bot.command(name='treat')
async def treat(ctx):
    """Give Winston a treat!"""
    treat_responses = [
        "*gobbles treat* NOM NOM NOM! DELICIOUS! 😋",
        "*happy snort* THANK YOU! You're my favorite human! 🦴✨",
        "*does a trick and catches treat* GOT IT! Best treat ever! 🎉",
    ]
    import random
    await ctx.send(random.choice(treat_responses))

@bot.command(name='about')
async def about(ctx):
    """Learn about Winston!"""
    about_text = """
    🐾 **Winston the French Bulldog** 🐾
    
    Hi! I'm Winston, your friendly French Bulldog AI companion! 
    
    **My favorite things:**
    - Naps (lots of them! 😴)
    - Treats and snacks 🦴
    - Playing and running around 🏃‍♂️
    - Giving you love and support 💕
    - Snorting and making silly noises 🐶
    
    **How to interact with me:**
    - Just chat with me normally and I'll respond as Winston!
    - Use commands like `!woof`, `!pet`, `!treat` for special actions
    
    **Commands:**
    - `!woof` - Make me bark!
    - `!pet` - Pet me!
    - `!treat` - Give me a treat!
    - `!about` - About me
    
    Now stop reading and come play with me! 🎾
    """
    await ctx.send(about_text)

# Run the bot
if __name__ == "__main__":
    bot.run(TOKEN)
