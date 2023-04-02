import base64
from art import text2art
from selfcord.ext import commands as vbot


class TextCmds(
        vbot.Cog,
        name="Text",
        description="Various commands for text editing"):
    def __init__(self, bot):
        self.bot: vbot.Bot = bot

    @vbot.command(
        name="encode",
        description="Encodes a string into base64"
    )
    async def encode(self, ctx, *, string):
        msg = ctx.message

        message_bytes = string.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        await msg.edit(content=f"```yaml\n{base64_message}```")

    @vbot.command(
        name='decode',
        description="Decodes a base64 string (or any string)"
    )
    async def decode(self, ctx, *, string):
        msg = ctx.message

        base64_bytes = string.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')

        await msg.edit(content=f"```yaml\n{message}```")

    @vbot.command(
        name="space",
        description="Spaces every character in a string"
    )
    async def space(self, ctx, *, txt):
        msg = ctx.message
        spaced_txt = " ".join([''.join(item) for item in zip(txt[::1])])

        try:
            await msg.edit(content=spaced_txt)

        except Exception as e:
            await msg.edit(content=f"```yaml\n- An error has occurred: {e}")

    @vbot.command(
        name="upper",
        description="Makes every character uppercase in a string"
    )
    async def _upper(self, ctx, *, txt):
        msg = ctx.message
        uppercased = txt.upper()

        try:
            await msg.edit(content=uppercased)

        except Exception as e:
            await msg.edit(content=f"```yaml\n- An error has occurred: {e}")

    @vbot.command(
        name="lower",
        description="Makes every character lowercase in a string"
    )
    async def _lower(self, ctx, *, txt):
        msg = ctx.message
        lowercased = txt.lower()

        try:
            await msg.edit(content=lowercased)

        except Exception as e:
            await msg.edit(content=f"```yaml\n- An error has occurred: {e}")

    @vbot.command(
        name="invert",
        description="Inverts the characters' case (use command to understand)"
    )
    async def invert(self, ctx, *, txt):
        msg = ctx.message
        inverted = txt.swapcase()

        try:
            await msg.edit(content=inverted)

        except Exception as e:
            await msg.edit(content=f"```yaml\n- An error has occurred: {e}")

    @vbot.command(
        name="reverse",
        description="Reverses a string"
    )
    async def reverse(self, ctx, *, txt):
        msg = ctx.message
        reversed = txt[::-1]

        try:
            await msg.edit(content=reversed)

        except Exception as e:
            await msg.edit(content=f"```yaml\n- An error has occurred: {e}")

    @vbot.command(
        name="annoy",
        description="Makes a string annoying"
    )
    async def annoy(self, ctx, *, txt):
        msg = ctx.message
        annoying = ""

        for idx in range(len(txt)):
            if not idx % 2:
                annoying += txt[idx].upper()

            else:
                annoying += txt[idx].lower()

        await msg.edit(content=annoying)

    @vbot.group(
        name="ascii",
        description="ASCII-ify your message",
        invoke_without_command=True
    )
    async def ascii(self, ctx: vbot.Context, *, message: str):
        msg = ctx.message
        text = text2art(message)
        await msg.edit(content=f'```yaml\n{text}```')

    @ascii.command(
        name="random",
        description="ASCII-ify your message with a random font"
    )
    async def asciirandom(self, ctx: vbot.Context, *, message: str):
        msg = ctx.message
        try:
            text = text2art(message, font="random")
            await msg.edit(content=f'```yaml\n{text}```')

        except Exception as e:
            await msg.edit(content=f"```yaml\n- An error has occurred: {e}")


if __name__ == "__main__":
    print("You need to run main.py to run the bot")


async def setup(bot):
    await bot.add_cog(TextCmds(bot))
