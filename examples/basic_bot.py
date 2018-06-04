import discord, random, time
from discord.ext import commands

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='\', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdX format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdX!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')
                   
async def autothief():
    while True:
        a = 24
        while a > 0:
            await bot.say('$steal')
            time.sleep(3600)
            a -= 1
        b = 500
        while b > 0:
            await bot.say('$give 100 <@!438443378498338816>')
            b -= 1
        b = 99
        while b > 0:
            await bot.say('$give 1 <@!438443378498338816>')
            b -= 1

bot.run('NDUzMjA4ODk2NjEwMjM4NDc0.DfbjVg.6GoDKoWf3Tblnwa5xBphwGexR_M')
