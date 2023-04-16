import asyncio
import requests
import discord
from pyowm import OWM


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # Isso aqui serve pro bot não responder a si mesmo
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!clima'):
            await message.channel.send("Digite o local que você quer saber o clima")
            x = True

            def ta_certo(minha_mensagem):
                return minha_mensagem.author == message.author and bool(minha_mensagem.content)

            try:
                city = await self.wait_for('message', check=ta_certo, timeout=10.0)
                city_name = city.content

                api_key = "015f8141edc79dda4164c30a8929fcc6"
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
                response = requests.get(url)
                response.raise_for_status()
                weather_data = response.json()

                # PYOMW code
                owm = OWM('015f8141edc79dda4164c30a8929fcc6')
                mgr = owm.weather_manager()
                observation = mgr.weather_at_place(f'{city_name}')
                weather = observation.weather
                temp_dict_celsius = weather.temperature('celsius')
                temperatura = (temp_dict_celsius['temp'])

                tempo_pra_mandar = weather_data["weather"][0]["main"]
                if tempo_pra_mandar == "Rain":
                    tempo_pra_mandar = "chuvendo"
                elif tempo_pra_mandar == "Clouds":
                    tempo_pra_mandar = "nublado"
                elif tempo_pra_mandar == "Clear":
                    tempo_pra_mandar = "céu aberto"
                elif tempo_pra_mandar == "Snow":
                    tempo_pra_mandar = "nevando"
                else:
                    tempo_pra_mandar = weather_data["weather"][0]["main"]

                await message.channel.send(f"Está {tempo_pra_mandar} em {city_name}, com "
                                           f"{temperatura}°C de temperatura")

            except requests.exceptions.HTTPError as error:
                await message.channel.send(f"{city_name} não é uma cidade válida")
                print(f"HTTP Error in {error}")
            except KeyError as error:
                print(f"Response data is missing expected key: {error}")
            except asyncio.TimeoutError:
                x = False
                return await message.channel.send("Você demorou muito pra responder")
            except Exception as error:
                print(f"An error occurred: {error}")


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTA5MDA0MzI4MDA1OTgwMTYzMA.Gt--JE.3taTtaL25Z3fldkXh7HMCJIhnd5lBggd49zU6c')
