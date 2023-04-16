import asyncio
import discord
from discord.ext import commands
import random
import comandos


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # Isso aqui serve pro bot não responder a si mesmo
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!adivinha'):
            await message.channel.send('Adivinha um número de 0 a 10')
            x = True

        answer = random.randint(0, 10)

        def ta_certo(minha_mensagem):
            return minha_mensagem.author == message.author and minha_mensagem.content.isdigit() and x is True

        try:
            guess = await self.wait_for('message', check=ta_certo, timeout=5.0)

        except asyncio.TimeoutError and x is True:
            return await message.channel.send(f"Foi mal, mas você demorou muito pra responder, a resposta era {answer}")

        if int(guess.content) == answer:
            await message.channel.send("Você acertou!")
        else:
            await message.channel.send(f"Você errou! A resposta era {answer}")


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTA5MDA0MzI4MDA1OTgwMTYzMA.Gt--JE.3taTtaL25Z3fldkXh7HMCJIhnd5lBggd49zU6c')
