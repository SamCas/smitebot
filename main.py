import discord
from pymongo import MongoClient
from envars import *
from utils import *

sampleBuild = {
    'godName' : 'scylla',
    'start' : ['Mage\'s Blessing', 'Tiny Trinket', 'Healing Potion x2', 'Mana Potion x3'],
    'core' : ['Soul Gem', 'Shoes of Focus', 'Soul Reaver'],
    'full' : ['Polynomicon', 'Typhon\'s  Fang'],
    'alt' : ['Obsidian', 'Pythagorem\'s Piece', 'Rod of Tahuti', 'Spear of Desolation']
}

def main():
    mongoClient = MongoClient(MONGO_KEY)
    db = mongoClient['smitebot']
    builds = db.builds

    def discordConnection():
        discordClient = discord.Client()

        @discordClient.event
        async def on_ready():
            print('We have logged in as {0.user}'.format(discordClient))

        @discordClient.event
        async def on_message(message):
            if message.author == discordClient.user:
                return

            if message.content.startswith('-build'):
                godName = BotUtils().getMessage(message.content)
                response = BotUtils().parseMongoResponse(builds.find_one({'godName':godName}))
                await message.channel.send(response)    

        discordClient.run(DISCORD_BOT_TOKEN)

    discordConnection()

if __name__ == "__main__":
    main()