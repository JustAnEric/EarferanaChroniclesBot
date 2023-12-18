from discord.ext import commands
from datetime import datetime
from discord import (
  Intents,
  Message,
  Activity,
  ActivityType,
  Status,
  Embed,
  Colour
)

class BotApplication(commands.Bot):
  def __init__(self):
    super().__init__(
      command_prefix = "rp!",
      case_insensitive = True, 
      intents = Intents(
        guild_messages = True, 
        guild_reactions = True, 
        guilds = True, 
        invites = True, 
        members = True, 
        messages = True, 
        reactions = True, 
        message_content = True
      )
    )

    self.add_listener('ready', self.on_ready)

    # commands section
    
    @self.command(
      name="tech",
      description="Research about any topic in Map RP.",
      brief="Research about any topic in Map RP."
    )
    async def research(ctx, query=None):
      em1 = Embed(
        title="Research command",
        description="Find all new things you can research!",
        color=Colour.random()
      )
      em1.set_author(name="RP Bot™")
      em1.set_footer(text="rp!research", icon_url="")
  
      await ctx.send(embed=em1)
      await ctx.send("https://maprpdevelopment.fandom.com/wiki/Technologies")

    @self.group(
      invoke_without_command=True,
      name="map",
      description="View Map for RP Bot. (Default and Satellite View.)",
      brief="View Map for RP Bot. (Default and Satellite View.)"
    )
    async def map(ctx):
      # This defaults back to the default map.
      em = Embed(
        title="RP Map (Default Terrain)",
        color=Colour.gold()
      )
      em.set_image(
        url="https://media.discordapp.net/attachments/970259189656080444/1035520437821644911/MAPRP_UPDATE_1.png"
      )
      await ctx.send(
        embed=em,
        content="**`Because you didn't supply a argument after the command, none was chosen. So, we chose the default map. You either supplied something that was wrong or something else that had different spelling.`**"
      )

    @map.command(
      name="map default",
      description="The map with the territories",
      aliases=["default", "normal", "territories", "current"],
      brief="The map with the territories"
    )
    async def default(ctx):
      em = Embed(
        title="RP Map (Default Terrain)",
        color=Colour.gold()
      )
      em.set_image(
          url="https://media.discordapp.net/attachments/970259189656080444/1035520437821644911/MAPRP_UPDATE_1.png"
      )
      await ctx.send(embed=em)

    @map.command(
      name="map satellite",
      description="The satellite version of the map",
      aliases=["satellite", "satelite", "sattelite"],
      brief="The satellite version of the map"
    )
    async def satellite(ctx):
      em = Embed(
        title="RP Map (Satellite Version)",
        color=Colour.gold()
      )
      em.set_image(
          url="https://cdn.discordapp.com/attachments/938799685492162593/976130435006484510/Untitled42_20220517223300.png"
      )
      await ctx.send(embed=em)
      if (ctx.invoked_with == "satelite" or ctx.invoked_with == "sattelite"):
          await ctx.send(
              content=f"**`Because you used a common misspelling for the word satellite after the command, sattelite was chosen. So, we chose the sattelite map. You misspelled the word sattelite, by spelling it as {ctx.invoked_with}.`**"
          )

    @map.command(
      aliases=["goma"], 
      brief="The map with the Goman territory"
    )
    async def goman(ctx):
      em = Embed(title="RP Map (Goman)", color=Colour.gold())
      em.set_image(
          url="https://cdn.discordapp.com/attachments/899282814879555634/906212487437897758/unknown.png"
      )
      await ctx.send(embed=em)

    @map.command(
      aliases=["tectonics", "plate", "plates"],
      brief="The map with the tectonic plates"
    )
    async def tectonic(ctx):
      em = Embed(title="RP Map (Tectonic Plates)",
                         color=Colour.gold())
      em.set_image(
          url="https://cdn.discordapp.com/attachments/899282814879555634/945646850919260170/unknown.png"
      )
      await ctx.send(embed=em)

    @map.command(
      aliases=["without-gomans", "no-gomans", "no gomans"],
      brief="The map without the gomans"
    )
    async def without_gomans(ctx):
      em = Embed(
        title="RP Map (Without Gomans)",
        color=Colour.gold()
      )
      em.set_image(
          url="https://media.discordapp.net/attachments/970259189656080444/1014504703322751016/unknown.png"
      )
      await ctx.send(embed=em)

    @map.command(
      aliases=["continent", "contient", "contients"],
      brief="The map with the continents"
    )
    async def continents(ctx):
      em = Embed(
        title="RP Map (Continents)",
        color=Colour.gold()
      )
      em.set_image(
          url="https://media.discordapp.net/attachments/970259189656080444/1007290758954483832/unknown.png"
      )
      await ctx.send(embed=em)

    @map.command(
      aliases=["ernian"],
      brief="The Ernia map"
    )
    async def ernia(ctx):
      em = Embed(
        title="RP Map (Ernia)",
        color=Colour.gold()
      )
      em.set_image(
          url="https://media.discordapp.net/attachments/970259189656080444/991234840903036928/unknown.png"
      )
      await ctx.send(embed=em)

    @map.command(brief="The territory of Corda")
    async def corda(ctx, year=None):
      if year == "700":
        em = Embed(
          title="Corda Map (700)",
          color=Colour.gold()
        )
        em.set_image(
          url="https://cdn.discordapp.com/attachments/899282814879555634/946036118938324992/Untitled13_20220223212932.png"
        )
        await ctx.send(embed=em)
      elif year == "800":
        em = Embed(
          title="Corda Map (800)",
          color=Colour.gold()
        )
        em.set_image(
          url="https://cdn.discordapp.com/attachments/899282814879555634/934284987149205605/Untitled7_20220116205009.png"
        )
        await ctx.send(embed=em)
      elif year == "900":
        em = Embed(
          title="Corda Map (900)",
          color=Colour.gold()
        )
        em.set_image(
          url="https://cdn.discordapp.com/attachments/899282814879555634/934284987413430272/Untitled7_20220116203818.png"
        )
        await ctx.send(embed=em)
      elif year == "1000":
        em = Embed(
          title="Corda Map (1000)",
          color=Colour.gold()
        )
        em.set_image(
          url="https://cdn.discordapp.com/attachments/899282814879555634/934284987711234109/Untitled7_20220116203528.png"
        )
        await ctx.send(embed=em)
      elif year == "1100" or year is None:
        em = Embed(
          title="Corda Map (1100)",
          color=Colour.gold()
        )
        em.set_image(
          url="https://cdn.discordapp.com/attachments/899282814879555634/934284987946119198/Untitled7_20220116202439.png"
        )
        await ctx.send(embed=em)

    @self.command(brief="Wiki page for Map RP.")
    async def wiki(ctx):
      em = Embed(
        title="Map RP Wiki",
        description="Shows the wiki page! (click on the author link ^^^)",
        color=Colour.random()
      )
      em.set_author(
        name="Click me to go to the wiki!",
        url="https://maprpdevelopment.fandom.com/wiki/Map_RP_Wiki"
      )
      await ctx.send(embed=em)

    # begin deprecated command 
    """
    @self.command(brief="Latest Dev Diary for Map RP.")
    async def diary(ctx):
      em = Embed(
        title="Latest Dev Diary",
        description="Shows the latest dev diary! (click on the author link ^^^)",
        color=Colour.random()
      )
      em.set_author(
        name="Click me to go to the latest Dev Diary!",
        url="https://discord.com/channels/729578838320742401/906653896787763221/945772804681400400"
      )

      buttons = [
        Button(
            style=5,
            url="https://discord.com/channels/729578838320742401/906653896787763221/943545953233825863",
            label="Dev Diary 0: Info about Dev Diaries"
        ),
        Button(
            style=5,
            label="Latest Dev Diary: Dev Diary #1",
            url="https://discord.com/channels/729578838320742401/906653896787763221/945772804681400400"
        ),
        Button(
            style=5,
            label="#1",
            url="https://discord.com/channels/729578838320742401/906653896787763221/945772804681400400"
        )
    ]

    print(ctx.channel)
    print(dir(ctx.channel))
    await ctx.send(embed=em, components=buttons)

    button_ctx = await wait_for_component(bot, components=action_row)
    await button_ctx.edit_origin(
        content=f"You pressed the button with the ID {ctx.id}!")
    """
    # end deprecated command

    @self.command(brief="Gets the current year")
    async def currentyear(ctx):
      channel = self.get_channel(938799685492162593)
      message = await channel.fetch_message(945556182712606780)
      await ctx.send(f"It's year {message.content}.")

    @self.command(brief="Sets the year")
    async def setyear(ctx, year):
      devs = [
        687980259332587586, 811966926208237618, 719785204285308931,
        586535675772403734, 687980259332587586, 927278839774724156,
        719785204285308931, 586535675772403734, 862046044862021682,
        778158738318032937, 941337177986596885, 1031217311283159141,
        880433376148979732
      ]
      if ctx.message.author.id in devs:
        channel = bot.get_channel(938799685492162593)
        message = await channel.fetch_message(945556182712606780)
        await message.edit(content=year)
  
        if year == "69" or int(message.content) % 100 == 69:
          await ctx.send("https://tenor.com/view/69-gif-23047473")
        await ctx.send(f"It's now year {year}.")
      else:
        await ctx.send("I don't recognize you.")

    @self.command(brief="Advances the year")
    async def advance(ctx, year=None):
      devs = [
        687980259332587586, 811966926208237618, 719785204285308931,
        586535675772403734, 687980259332587586, 927278839774724156,
        719785204285308931, 586535675772403734, 862046044862021682,
        778158738318032937, 941337177986596885, 1031217311283159141,
        880433376148979732
      ]
      if ctx.message.author.id in devs:
        channel = bot.get_channel(938799685492162593)
        message = await channel.fetch_message(945556182712606780)
  
        if year is not None:
          await message.edit(content=int(message.content) + int(year))
          if str(year) == "69" or int(message.content) + year % 100 == 69:
          await ctx.send("https://tenor.com/view/69-gif-23047473")
        else:
          await message.edit(content=1 + int(message.content))
  
        await ctx.send(
          f"It's now year {int(message.content) + (year if year is not None else 1)}."
        )
      else:
        await ctx.send("I don't recognize you.")

    @self.tree.command(name="advance", description="Advances the year")
    async def _advance(interaction: discord.Interaction, year: int):
      class Empty:
        pass
      interaction.message = Empty()
      interaction.message.author = interaction.user
      await advance.__call__(interaction, year)

    @self.tree.command(name="countryinfo", description="Gets the info of a country")
    async def _countryinfo(interaction: discord.Interaction, country: str):
      await countryinfo.__call__(interaction, country)

    @self.command(brief="Checks the latency of the bot")
    async def ping(ctx):
      await ctx.send(f'Pong! {bot.latency * 1000} ms.')

    @self.command(brief="Checks if you're a developer")
    async def devornot(ctx):
      botdevs = [
        687980259332587586, 811966926208237618, 719785204285308931,
        586535675772403734, 1031217311283159141, 880433376148979732,
        880433376148979732
      ]
      gamedevs = [
        687980259332587586, 927278839774724156, 719785204285308931,
        586535675772403734, 862046044862021682, 778158738318032937,
        941337177986596885, 1031217311283159141, 880433376148979732,
        880433376148979732
      ]
      userid = ctx.message.author.id
      await ctx.send(
          f'You are {"a bot dev" if userid in botdevs else "not a bot dev"}.\nYou are {"a game dev" if userid in gamedevs else "not a game dev"}.'
      )

    @self.tree.command(description="Checks if you're a developer")
    async def devornot2(interaction: discord.Interaction):
      botdevs = [
        687980259332587586, 811966926208237618, 719785204285308931,
        586535675772403734, 1031217311283159141, 880433376148979732,
        880433376148979732
      ]
      gamedevs = [
        687980259332587586, 927278839774724156, 719785204285308931,
        586535675772403734, 862046044862021682, 778158738318032937,
        941337177986596885, 1031217311283159141, 880433376148979732,
        880433376148979732
      ]
      userid = interaction.user.id
      await interaction.send(
          f'You are {"a bot dev" if userid in botdevs else "not a bot dev"}.\nYou are {"a game dev" if userid in gamedevs else "not a game dev"}.'
      )

    @self.command(brief="Checks the Country info of the country supplied")
    async def countryinfo(ctx, countryname):
      # ADD COUNTRIES BELOW WITH INFO:
  
      for country in countries:
        for data_name in country['name']:
          if countryname in country['name']:
            em = Embed(title=country['name'],description=country['description'],color=country['color'])
            em.add_field(name="ID", value="**#" + country['id'] + "**")
            em.set_footer(text=country['footer'])
            em.set_thumbnail(url=country['thumb'])
            await ctx.send(embed=em)
            return
          elif countryname == country['id']:
            em = Embed(title=country['name'],description=country['description'],color=country['color'])
            em.add_field(name="ID", value="**#" + country['id'] + "**")
            em.set_footer(text=country['footer'])
            em.set_thumbnail(url=country['thumb'])
            await ctx.send("Found from id", embed=em)
            return
          elif countryname in country['aliases']:
            em = discord.Embed(title=country['name'],description=country['description'],color=country['color'])
            em.add_field(name="ID", value="**#" + country['id'] + "**")
            em.set_footer(text=country['footer'])
            em.set_thumbnail(url=country['thumb'])
            await ctx.send("Found from aliases", embed=em)
            return  
      bot_countries = db["countries"]
  
      for country in bot_countries.values():
        for data_name in country['name']:
          if countryname in country['name']:
            em = Embed(title=country['name'],description=country['description'],color=Colour.random())
            em.add_field(name="ID", value="**#" + country['id'] + "**")
            em.set_footer(text="Land owned by " + country['name'])
            await ctx.send(embed=em)
            return
          elif countryname == country['id']:
            em = Embed(title=country['name'],description=country['description'],color=Colour.random())
            em.add_field(name="ID", value="**#" + country['id'] + "**")
            em.set_footer(text="Land owned by " + country['name'])
            await ctx.send(embed=em)
            await ctx.send("Found from id", embed=em)
            return
  
      await ctx.send(
          "This country entered is invalid. Please retry your spelling or try another country."
      )

    @self.command(brief="This is a command that shows you how to create your country on the WIKI website!")
    async def create_a_country(ctx):
      em = discord.Embed(
        title="4 easy steps to creating your country",
        description="This easy guide will teach you step-by-step on how to create a country. Please follow the steps very carefully."
      )
      em.add_field(name="1.", value="Have a idea")
      em.add_field(name="2.", value="Create the country")
      em.add_field(name="3.", value="Get Creative!")
      em.add_field(name="4.", value="Software to help you make your Country of Dreams")
      em.set_footer(
          text="More info here: [https://maprpdevelopment.fandom.com/wiki/How_to_Make_A_Country](https://maprpdevelopment.fandom.com/wiki/)"
      )
      await ctx.send(embed=em)

    @self.tree.command(name="ping", description="Checks the latency of the bot")
    async def _ping(ctx: discord.Interaction):
      await ctx.send(f'Pong! {bot.latency * 1000} ms.')


    @self.tree.command(name="test", description="Test command")
    async def _test(ctx: discord.Interaction):
      await ctx.send("test command")

    @self.tree.command(name="research", description="Research about any topic in Map RP.")
    async def _research(ctx: discord.Interaction):
      await research.__call__(ctx)

    # end commands section

    #events section
    @bot.listen("on_invite_create")
    async def invite_create(invite):
      if invite.guild != None and invite.guild.id == 1099631641040793612:
        if invite.max_age > 43200 or invite.max_age == 0:
          await invite.delete(reason="More than one day")
          return
        if invite.max_uses != 1:
          await invite.delete(reason="Max uses isn't exactly 1")

    @bot.listen("on_message")
    async def message_create(message):
      if message.guild != None and message.guild.id == 1130954621561602258:
        if message.author.id == 999736048596816014 and ("A wild countryball appeared!" in message.content):
          await message.channel.send("<@&1135307528553644103>")

    # end events section

    self.run("ADD_TOKEN_HERE_FROM_GITHUB_ENVIRONMENT_VARIABLES")

  async def on_ready(self):
    print("hello fellow abuc nbuc akmc members! i'm online!")
    await self.change_presence(
      activity = Activity(
        type = ActivityType.watching, 
        name = "rp!help"
      ),
      status = Status.dnd
    )
