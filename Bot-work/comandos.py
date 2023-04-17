import discord
import random
from discord.ext import commands
import requests
import functools

descricao = """Vou tentar fazer um bot com algumas coisas, sem ser na pasta main"""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=descricao, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def soma(ctx, *numbers: int):
    while True:
        result = 0
        resultado_de_escape = 0
        resultado_de_escape2 = 0
        for numeros in numbers:
            resultado_de_escape += numeros
            resultado_de_escape2 -= numeros
            if resultado_de_escape == resultado_de_escape2 == 0:
                break
        for numeros in numbers:
            result += numeros
        if resultado_de_escape == resultado_de_escape2 == 0:
            await ctx.send(f"Por favor, digite um número válido!"
                           f" Use como referência '!soma <numero 1> <numero 2>'")
            break
        await ctx.send(f"Seu resultado é {result}")
        break


@soma.error
async def soma_error(ctx, error):
    if isinstance(error, IndexError) or isinstance(error, commands.errors.BadArgument):
        await ctx.send("Coloque um número para somar, por favor")
    else:
        print(f"Error: {error}")
        await ctx.send("Coloque um número para somar, por favor")


@bot.command()
async def entrou(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send("Digite algum membro, por favor")
        return
    await ctx.send(f"{member.name} entrou em {discord.utils.format_dt(member.joined_at)}")


@entrou.error
async def entrou_error(ctx, error):
    if isinstance(error, commands.errors.MemberNotFound):
        await ctx.send("Desculpe, membro não encontrado.")
    else:
        print(f"Error: {error}")


@bot.command()
async def subtrair(ctx, *numbers: int):
    while True:
        resultado_de_escape = 0
        resultado_de_escape2 = 0
        for numeros in numbers:
            resultado_de_escape += numeros
            resultado_de_escape2 -= numeros
            if resultado_de_escape == resultado_de_escape2 == 0:
                await ctx.send(f"Por favor, digite um número válido!"
                               f" Use como referência '!subtrair <numero 1> <numero 2>'")
                break
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        await ctx.send(f"Seu resultado é {result}")
        break


@subtrair.error
async def subtrair_error(ctx, error):
    if isinstance(error, IndexError) or isinstance(error, commands.errors.BadArgument):
        await ctx.send("Coloque um número para subtrair, por favor")
    else:
        print(f"Error: {error}")
        await ctx.send("Coloque um número para subtrair, por favor")


@bot.command()
async def multiplicar(ctx, *numbers: int):
    while True:
        result = 1
        resultado_de_escape = 0
        resultado_de_escape2 = 0
        for numeros in numbers:
            resultado_de_escape += numeros
            resultado_de_escape2 -= numeros
            if resultado_de_escape == resultado_de_escape2 == 0:
                break
        if resultado_de_escape == resultado_de_escape2 == 0:
            await ctx.send(f"Por favor, digite um número válido!"
                           f" Use como referência '!multiplicar <numero 1> <numero 2>'")
            break
        for numeros in numbers:
            result *= numeros
        await ctx.send(f"Seu resultado é {result}")
        break


@multiplicar.error
async def multiplicar_error(ctx, error):
    if isinstance(error, IndexError) or isinstance(error, commands.errors.BadArgument):
        await ctx.send("Coloque um número para somar, por favor")
    else:
        print(f"Error: {error}")
        await ctx.send("Coloque um número para somar, por favor")


@bot.command()
async def dividir(ctx, *numbers: int):
    while True:
        result = 1
        # Fail-safe caso a pessoa não digite nada
        resultado_de_escape = 0
        resultado_de_escape2 = 0
        for numeros in numbers:
            resultado_de_escape += numeros
            resultado_de_escape2 -= numeros
            break
        if resultado_de_escape == resultado_de_escape2 == 0:
            await ctx.send(f"Por favor, digite um número válido!"
                           f" Use como referência '!dividir <numero 1> <numero 2>'")
            break

        for numeros in numbers:
            result /= numeros
        await ctx.send(f"Seu resultado é {result}")
        break


@dividir.error
async def dividir_error(ctx, error):
    if commands.errors.BadArgument:
        await ctx.send("Não é possível dividir por 0!")
    else:
        print(f"Error: {error}")
        await ctx.send(f"Digite um número válido, por favor.")


@bot.command()
async def ajuda(ctx):
    await ctx.send("Lista de comandos: \n"
                   "!ajuda\n"
                   "!soma\n"
                   "!subtrair\n"
                   "!multiplicar\n"
                   "!dividir\n"
                   "!adivinha\n"
                   "!entrou\n"
                   "!clima\n")


bot.run('your_token')
