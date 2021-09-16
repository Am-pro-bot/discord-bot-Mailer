import discord
from discord.ext import tasks, commands
from os 

bot = commands.Bot(command_prefix='m!', help_command=None,intents = discord.Intents.all())

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')    

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


    
bot.run('ODg2NjM0NTA5MTU0NTI5Mjgw.YT4cuw.GDcUa3vmINEWuGsA3rmkTcappfA')
