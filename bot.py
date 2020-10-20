import os

import aiohttp
import twitchio
import temmytranslator
from twitchio.ext import commands

aio_session = aiohttp.ClientSession()

uwus = [
    'uWu',
    'oWo',
    'UWU :3',
    'UwU',
    ':3',
    'nyxiative\'s mouse pad',
    '(ᵘʷᵘ)',
    '(ᵘﻌᵘ)',
    '˯˽˯',
    '(◡ ω ◡)',
    '(◡ u ◡)',
    '(◡ w ◡)',
    '(◡ ሠ ◡)',
    '(˘ω˘)',
    '(⑅˘꒳˘)',
    '(˘ᵕ˘)',
    '(˘ሠ˘)',
    '(˘³˘)',
    '(˘ε˘)',
    '(´˘`)',
    '(´^`)',
    '(˘ ^ ˘)',
    '( ᴜ ω ᴜ )',
    '( ´ω` )۶',
    '(„ᵕᴗᵕ„)',
    '(*ฅ́˘ฅ̀*) ',
    '(ㅅ ˘ )',
    '(⑅˘˘)',
    '( ｡ᵘ ᵕ ᵘ ｡)'
]
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            irc_token=os.environ["TMI_TOKEN"],
            client_id=os.environ["CLIENT_ID"],
            nick=os.environ["BOT_NICK"],
            prefix=os.environ["BOT_PREFIX"],
            initial_channels=[os.environ["CHANNEL"]]
        ),

    async def event_ready(self):
        print(f"Uwu Melkey Senpai | {self.nick}")

    # Triggers for particular events
    async def event_message(self, msg):
        ctx = await self.get_context(msg, cls=twitchio.Context)
        #rudamentary weab detection
        trigger_uwu = any(ele in str(msg.content) for ele in uwus)
        #BRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
        trigger_uwu_lower = any(ele in str(msg.content.lower()) for ele in uwus)
        if trigger_uwu or trigger_uwu_lower:
            if msg.author.name != self.nick:
                await msg.channel.send(random.choice(uwus))

        await self.handle_commands(msg, ctx=ctx)

    # Discord Command
    # @commands.command(name="cmd")
    # async def discord(self, ctx):
        # await ctx.send("The currenty list of commands: !discord, !project, !TJ, !editor, !theme,!GOAT, !config, !github")

    # Discord Command
    @commands.command(name="discord")
    async def discord(self, ctx):
        await ctx.send("Join our awesome Discord channel! - https://discord.gg/HHZMSCu")

    @commands.command(name="commands")
    async def test(self, ctx):
        commands = ''
        for k, v in self.commands.items():
            commands += f"!{k}"
            if v.aliases:
                aliases = ", ".join(f"!{a}" for a in v.aliases)
                commands += f" ({aliases})"
            commands += ", "
        await ctx.send(f"The current list of commands: {commands}")

    @commands.command(name="height")
    async def height(self, ctx):
        await ctx.send("MelkeyDev is 7'8\"")

    @commands.command(name="TJ")
    async def TJ(self, ctx):
        await ctx.send("Is my actual brother, thats totally not a lie.")

    @commands.command(name="beginbot")
    async def begingbot(self, ctx):
        await ctx.send("My favorite Twitch Scene is him in his Hottub")

    @commands.command(name="keyboard")
    async def keyboard(self, ctx):
        await ctx.send("Glorious GMMK Ice White with Glorious Panda switches from pcgamingrace.com SPONSORED BY @nyxiative")

    # Current project
    @commands.command(name="project")
    async def project(self, ctx):
        await ctx.send(
            "I am currently working on dockerizing and deploying my YouTube Downloader for my Russian Parents ye"
        )

    # Editor
    @commands.command(name="editor")
    async def editor(self, ctx):
        await ctx.send("Melkey is currently using NVIM as the Editor")

    # Current Theme in Editor
    @commands.command(name="theme")
    async def theme(self, ctx):
        await ctx.send("NVIM - SpaceCamp")

    # Current Theme in Editor
    @commands.command(name="GOAT")
    async def theme(self, ctx):
        await ctx.send("ThePrimeagen is the GOAT")

    # GitHub Link
    @commands.command(name="github")
    async def github(self, ctx):
        await ctx.send(
            "Melkey's GitHub can be found here: https://github.com/Amokstakov"
        )

    # config
    @commands.command(name="config", aliases=["rc", "dotfiles", "dopeassconfigfile"])
    async def githubdot(self, ctx):
        await ctx.send(
            "Melkey's config can be found here: https://github.com/Amokstakov/NvimConfig"
        )

    # Shoutout Commands

    @commands.command(name="so")
    async def shoutout(self, ctx, username: str) -> None:
        if ctx.author.is_mod == 1:
            await ctx.send(
                f"A big warm shoutout to the this person right here - show them some LOVE and FOLLOW, https://www.twitch.tv/{username}"
            )


    #Begin MDD

    #just a standard bot command, nothing to see here.
    @commands.command(name="bestmod")
    async def bestmod(self, ctx):
        await ctx.send("Andrew, obviously")
        
    @commands.command(name="real-bestmod")
    async def bestmod(self, ctx):
        await ctx.send("astro, obviously")

    @commands.command(name="worstmod")
    async def worstmod(self, ctx):
        await ctx.send("bk, obviously")

    #followage, gets the length of time that a given user has been following the channel
    @commands.command(name="followage", aliases=["followtime", "simptime"])
    async def followage(self, ctx):
        url = f'https://api.2g.be/twitch/followage/{ctx.channel.name}/{ctx.author.name}?format=mwdhms'
        async with aio_session.get(url) as response:
            data = await response.text()
        await ctx.send(str(data))

    #this is useful for mobile viewers as twitch has yet to get their shit together.
    @commands.command(name="uptime")
    async def uptime_m8(self, ctx):
        url = f'https://beta.decapi.me/twitch/uptime/{ctx.channel.name}'
        async with aio_session.get(url) as response:
            data = await response.text()
        await ctx.send(f'Current uptime for {ctx.channel.name} is {data}')

    #this will return a randomly generated insult
    @commands.command(name="insult", aliases=["femdom","make-me-cry"])
    async def insult_command(self, ctx):
        url ='https://insult.mattbas.org/api/insult'
        async with aio_session.get(url) as response:
            data = await response.text()
        await ctx.send(f"{data} {ctx.author.name}")

    #this will return a randomly generated compliment, how nice.
    @commands.command(name="compliment")
    async def compliment_command(self, ctx):
        url = 'https://complimentr.com/api'
        async with aio_session.get(url) as response:
            data = await response.json()
            output = str(data['compliment'])
        await ctx.send(f'{output} {ctx.author.name}')


    @commands.command(name="temmyifiy")
    async def temmyify(self, ctx):
        await ctx.send(temmytranslator.temmytranslate(ctx.content))
        
    @commands.command(name="hammond")
    async def hammond(self, ctx):
        await ctx.send("YOU IDIOT!") 
    
    

if __name__ == "__main__":
    bot = Bot()
    bot.run()
