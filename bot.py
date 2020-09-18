import os

import twitchio
from twitchio.ext import commands


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
        print(f"Ready | {self.nick}")

    # Triggers for particular events
    async def event_message(self, msg):
        ctx = await self.get_context(msg, cls=twitchio.Context)
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
        await ctx.send("The current list of commands: !discord, !project, !TJ, !editor, !theme, !GOAT, !config, !github")

    @commands.command(name="TJ")
    async def TJ(self, ctx):
        await ctx.send("Is my actual brother, thats totally not a lie.")

    @commands.command(name="beginbot")
    async def begingbot(self, ctx):
        await ctx.send("My favorite Twitch Scene is him in his Hottub")

    @commands.command(name="keyboard")
    async def keyboard(self, ctx):
        await ctx.send("Glorious GMMK Ice White with MX Browns from pcgamingrace.com SPONSORED BY @nyxiative")

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
    @commands.command(name="config")
    async def githubdot(self, ctx):
        await ctx.send(
            "Melkey's config can be found here: https://github.com/Amokstakov/NvimConfig"
        )

    # Shoutout Commands

    @commands.command(name="so")
    async def shoutout(self, ctx, username: str) -> None:
        print(ctx.author.badges)
        print(ctx.author.name)
        print(ctx.channel)
        if ctx.author.is_mod == 1:
            await ctx.send(
                f"A big warm shoutout to the this person right here - show them some LOVE and FOLLOW, https://www.twitch.tv/{username}"
            )


if __name__ == "__main__":
    bot = Bot()
    bot.run()
