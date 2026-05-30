import discord
from discord.ext import commands
from discord import app_commands

TOKEN = "MTUxMDEwNTcxMDkwNDQ3NTY4OQ.Gn7Nun.h7n5CFPTfmWGVRKhHjjZZ1pOpBvXPnqRMPoTbI"

# 🔥 TERI DISCORD ID (already daal di)
OWNER_ID = 1203610575381205033

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# ============== SLASH COMMANDS ==============
@bot.tree.command(name="play", description="Download BlossomTree RPG game")
async def slash_play(interaction: discord.Interaction):
    embed = discord.Embed(title="🌸 BLOSSOMTREE RPG", color=0xff69b4)
    embed.add_field(name="📱 Download APK", value="[Click Here](https://github.com/sunnynimbre3/blossomtree-game)", inline=False)
    embed.add_field(name="🌐 Web Version", value="[Click Here](https://sunnynimbre3.itch.io/blossomtree-demo)", inline=False)
    embed.add_field(name="💝 Support", value="UPI: sunnynimbre3@oksbi\nPayPal: paypal.me/@mrlegend4591", inline=False)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="stats", description="Check your game stats")
async def slash_stats(interaction: discord.Interaction, member: discord.Member = None):
    if not member:
        member = interaction.user
    embed = discord.Embed(title=f"📊 {member.display_name}'s STATS", color=0x00ff00)
    embed.add_field(name="Level", value="1", inline=True)
    embed.add_field(name="Class", value="Warrior", inline=True)
    embed.add_field(name="Gold", value="100", inline=True)
    embed.add_field(name="Kills", value="0", inline=True)
    embed.add_field(name="Boss Kills", value="0", inline=True)
    embed.add_field(name="Best Floor", value="1", inline=True)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="daily", description="Claim your daily reward")
async def slash_daily(interaction: discord.Interaction):
    embed = discord.Embed(title="🎁 DAILY REWARD", description="+50 Gold + 1 Health Potion", color=0xffd700)
    embed.add_field(name="Streak", value="Day 1", inline=True)
    embed.add_field(name="Next Reward", value="+100 Gold (Day 2)", inline=True)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="event", description="View current event")
async def slash_event(interaction: discord.Interaction):
    embed = discord.Embed(title="🌸 BLOSSOM FESTIVAL", color=0xff69b4)
    embed.add_field(name="Bonus", value="2x EXP + 2x Gold", inline=True)
    embed.add_field(name="Time Left", value="7 days", inline=True)
    embed.add_field(name="Special Boss", value="Blossom Guardian", inline=True)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="leaderboard", description="View top players")
async def slash_leaderboard(interaction: discord.Interaction):
    embed = discord.Embed(title="🏆 TOP PLAYERS", color=0xffd700)
    embed.add_field(name="#1 👑", value="Sunny - Level 50", inline=False)
    embed.add_field(name="#2 ⚔️", value="Coming Soon", inline=False)
    embed.add_field(name="#3 🛡️", value="Coming Soon", inline=False)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="help", description="Show all commands")
async def slash_help(interaction: discord.Interaction):
    embed = discord.Embed(title="🌸 BLOSSOMTREE COMMANDS", color=0xff69b4)
    embed.add_field(name="🎮 GAME", value="`/play` `/stats` `/daily` `/event` `/leaderboard`", inline=False)
    embed.add_field(name="ℹ️ INFO", value="`/help` `/serverinfo` `/ping`", inline=False)
    embed.set_footer(text="Also use !commands for prefix commands")
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="serverinfo", description="Get server information")
async def slash_serverinfo(interaction: discord.Interaction):
    guild = interaction.guild
    embed = discord.Embed(title=f"📊 {guild.name} INFO", color=0x00bfff)
    embed.add_field(name="👑 Owner", value=guild.owner.mention, inline=True)
    embed.add_field(name="👥 Members", value=guild.member_count, inline=True)
    embed.add_field(name="📝 Channels", value=len(guild.channels), inline=True)
    embed.add_field(name="🎭 Roles", value=len(guild.roles), inline=True)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="ping", description="Check bot latency")
async def slash_ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    embed = discord.Embed(title="🏓 PONG!", description=f"Latency: {latency}ms", color=0x00ff00)
    await interaction.response.send_message(embed=embed)

# ============== PREFIX COMMANDS ==============
@bot.command(name='commands')
async def show_commands(ctx):
    embed = discord.Embed(title="🌸 BLOSSOMTREE COMMANDS", color=0xff69b4)
    embed.add_field(name="Slash Commands (/)", value="`/play` `/stats` `/daily` `/event` `/leaderboard` `/help` `/serverinfo` `/ping`", inline=False)
    embed.add_field(name="Prefix Commands (!)", value="`!commands` `!sync`", inline=False)
    await ctx.send(embed=embed)

@bot.command(name='sync')
async def sync_commands(ctx):
    """Sync slash commands - sirf owner use kar sakta hai"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ Only bot owner can use this command!")
        return
    await ctx.send("🔄 Syncing slash commands...")
    try:
        synced = await bot.tree.sync()
        await ctx.send(f"✅ Synced {len(synced)} slash commands!")
    except Exception as e:
        await ctx.send(f"❌ Error: {e}")

# ============== BOT READY ==============
@bot.event
async def on_ready():
    print(f'✅ {bot.user} is online!')
    print(f'✅ Bot is in {len(bot.guilds)} servers')
    await bot.change_presence(activity=discord.Game(name="🌸 BlossomTree RPG | /help"))
    
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} slash commands")
    except Exception as e:
        print(f"❌ Sync error: {e}")

bot.run(TOKEN)
