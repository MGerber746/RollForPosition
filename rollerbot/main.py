import asyncio
import position_roller as p
import discord
import os

client = discord.Client()

class Job():
    __instance = None

    @staticmethod
    def getInstance():
        if Job.__instance == None:
            Job()
        return Job.__instance

    def __init__(self):
        if Job.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Job.__instance = self
            self.running = False
            self.people = []

    async def run_job(self):
        self.running = True
        await asyncio.sleep(10)
        self.running = False
        results = p.Roller(self.people).roll()
        self.people = []
        return results

def format_message(results):
    message = ""
    for entry in results:
        message += entry + ": " + results[entry].name + " "
    return message


@client.event
async def on_message(message):

    if message.content == '/rfp':
        if Job.getInstance().running == True:
            Job.getInstance().people.append(message.author.name)
        else:
            await message.channel.send('Roll For Position Begun. Enter /rfp in the next ten seconds to roll')
            Job.getInstance().people.append(message.author.name)
            result = await Job.getInstance().run_job()
            await message.channel.send(format_message(result))



client.run(os.getenv('TOKEN'))