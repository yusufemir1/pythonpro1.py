import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
!bunu ekledım
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
    bunu ekledim
    @bot.command()
async def repeat(ctx, times: int, content: str):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
        bunu ekledim
        @bot.command()
async def repeat(ctx, times: int, content: str):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)     
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
    
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run('token')
