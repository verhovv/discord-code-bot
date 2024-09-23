import discord
from discord import MessageType, Message
from discord.ext import commands
from discord.ext.commands import Context

from config import BOT_TOKEN
from spawner import test_code
from utils import review_code

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.command(name='run')
async def on_run_command(ctx: Context) -> None:
    if ctx.message.type != MessageType.reply:
        return

    replied_message: Message = await ctx.fetch_message(ctx.message.reference.message_id)
    replied_text = replied_message.content

    try:
        result, time_passed = await test_code(
            code=review_code(replied_text),
            stdin_string=ctx.message.content[5:].strip()
        )
    except TimeoutError:
        await ctx.send(content=f'Этот код работает слишком долго!')
        return

    await ctx.send(content=f'```\nOutput:\n{result}\n'[:1900] + f'```\n**Time passed: {time_passed:.2f}s**')


if __name__ == '__main__':
    bot.run(token=BOT_TOKEN)
