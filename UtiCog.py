import discord
from discord.ext import commands
from embed import commandss_embed

# définition de du Cog UtiCog qui rassemble toutes les commandes utilitaires

class UtiCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    # ce morceau de code annonce que le Cog a bien été allumé

    @commands.Cog.listener(name="on_ready")
    async def start_UtiCog(self) -> None:
        print("le cog UtiCog a été démarrée")

    #commande /Wiki ou *Wiki qui affiche un embed qui redirige vers le Wiki

    @commands.hybrid_command(name="wiki", description="Vous allez à la médiatèque chez Iris")
    async def wiki(self, ctx: commands.Context) -> discord.Message:
        wiki_embed = discord.Embed(
            title="Le wiki",
            description="Voici le wiki",
            url="https://roblox-arcane-odyssey.fandom.com/wiki/Arcane_Odyssey_Wiki",
            colour=discord.Colour.random(),
        )
        await ctx.send(embed=wiki_embed)
        
    # commande /tool ou *tool qui redirige vers un site d'outils pour les joueurs d'AO
    
    @commands.hybrid_command(name="tool", description="Vous allez à la salle de brainstorming d'Iris")
    async def tool(self, ctx : commands.Context) -> discord.Message:
        tool_embed = discord.Embed(
            title="Arcane odyssey tool",
            description="Voici des outils pour construire son stuff, son bateau, ses potions sur arcane odyssey",
            url="https://balancing.arcaneodyssey.net/",
            colour=discord.Colour.random(),
        )
        await ctx.send(embed=tool_embed)

    # commande /trello ou *trello qui redirige vers le trello d'AO (géré par vetex)

    @commands.hybrid_command(name="trello", description="Vous allez espoinner chez Vetex")
    async def trello(self, ctx : commands.Context) -> discord.Message:
        trello_embed = discord.Embed(
            title="Le trello d'arcane odyssey",
            description="Voici le trello où vous pouvez voir ce que Vetex a prévu pour le futur du jeu",
            url="https://trello.com/b/Mv99bZYP/arcane-odyssey",
            colour=discord.Colour.random(),
        )
        await ctx.send(embed=trello_embed)

    # commande /chart ou *chart qui redirige vers un site qui aide a résoudre les cartes au trésor

    @commands.hybrid_command(name="chart", description="Vous trouvez un village minecraft et allez voir le cartographe")
    async def chart(self, ctx : commands.Context) -> discord.Message:
        chart_embed = discord.Embed(
            title="Arcane odyssey chart",
            description="Un moyen efficace de résoudre les cartes au trésor sur arcane odyssey",
            url="https://myaltaccountsthis.github.io/arcane-odyssey-guides/treasure.html",
            colour=discord.Colour.random(),
        )
        await ctx.send(embed=chart_embed)

    # comande /forum ou *forum qui vous permet d'acceder au forum (entre nous pas très utile)

    @commands.hybrid_command(name="forum", description="Allez vous plaindre que le jeu est nul sur le forum")
    async def forum(self, ctx : commands.Context) -> discord.Message:
        forum_embed = discord.Embed(
            title="Arcane odyssey forum",
            description="Le forum officiel du jeu (|!| c'est en anglais |!|)",
            url="https://forum.arcaneodyssey.dev/",
            colour=discord.Colour.random(),
        )
        await ctx.send(embed=forum_embed)
        
    # commande /lore ou *lore qui vous redirige vers le google docs du lore du serveur (prévoyez un interprête)

    @commands.hybrid_command(name="lore", description="Père castor vous raconte le lore d'arcane odyssey")
    async def lore(self, ctx : commands.Context) -> discord.Message:
        lore_embed = discord.Embed(
            title="Arcane odyssey lore",
            description="Le lore officiel du jeu (|!| c'est en anglais |!|)",
            url="https://docs.google.com/document/d/120q6IC_SZoKjPRf0NMAxgZunDYLhV5r5_-kxcV8BcFw/edit",
            colour=discord.Colour.random(),
        )
        return await ctx.send(embed=lore_embed)
    
    # commande /value ou *value qui permet d'acceder au google docs (même si entre nous c'est plus proche d'un excel) du cours de la bourse 

    @commands.hybrid_command(name="value", description="Allez voir le cours du marché")
    async def value(self, ctx: commands.Context) -> discord.Message:
        lore_embed = discord.Embed(
            title="Arcane odyssey value list",
            description="La liste des valeurs de tout les items en galleons (|!| c'est en anglais |!|)",
            url="https://docs.google.com/spreadsheets/d/1L2P8zWs0VQ0kNxvP4wlbpK_7ySHr6OCiyq_mWROH9zk/edit#gid=71788216",
            colour=discord.Colour.random(),
        )
        return await ctx.send(embed=lore_embed) 
    
    # commande /commands ou *commands pour avoir la liste des commandes ainsi que leur description
    
    @commands.hybrid_command(name="commands", description="Affiche l'aide des commandes")
    async def commands(self, ctx: commands.Context) -> discord.Message:
        help_embed = commandss_embed
        commands_embed = discord.Embed(
            title="Menu d'aide",
            description=help_embed,
            colour=discord.Colour.blue()
        )
        await ctx.send(embed=commands_embed)
         
