from discord.ext import commands
from datetime import datetime
from discord import (
  Intents,
  Message,
  Activity,
  ActivityType,
  Status
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

  async def on_ready(self):
    print("hello fellow abuc nbuc akmc members! i'm online!")
    await self.change_presence(
      activity = Activity(
        type = ActivityType.watching, 
        name = "rp!help"
      ),
      status = Status.dnd
    )
