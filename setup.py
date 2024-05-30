
import discord
from discord.ext import commands
from uticog import UtiCog

# définire la class MyBot

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='*', intents=discord.Intents.all())

    # ajout des Cogs au reste du bot

    async def setup_hook(self) -> None:
        await self.add_cog(UtiCog(self))
        await self.tree.sync()

    # event on_ready qui print dans la console un message qui annon que le bot est prêt

    async def on_ready(self) -> None:
        print("Iris toujours prête à servir")
