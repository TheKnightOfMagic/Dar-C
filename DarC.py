# coding = UTF-16
import discord
import asyncio
import giphypop
import wikipedia
import os
from Inst import *
from discord.ext.commands import Bot
from discord.ext import commands
from giphypop import translate
from random import randint
from datetime import datetime
import logging

"""logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
"""
#import urllib,json
#data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=YOUR_API_KEY&limit=5").read())
#print json.dumps(data, sort_keys=True, indent=4)

Client = discord.Client()

bot_prefix= "!"
bot = commands.Bot(command_prefix= bot_prefix)
i = 0

knockKnock = ['Who', 'Food', 'Orange', 'Broken Pencil', 'Theodore', 'Cows go', 'Etch', 'Police', 'Beets', 'Ketchup', 'Goat', 'Cash', 'Doctor', 'From', 'Little old lady', 'Tank', 'Water']
knockReply = ['That\'s a pretty great owl impersonation!',
              'I uh, I\'m not food... Please don\'t hurt me.',
              'Orange you going to let me in?',
              'Nevermind, it\'s pointless.',
              'Theodore was wasn\'t opened, so I knocked.',
              'Cows don\'t go who silly, they go moo',
              'Bless you',
              'Police let me in! It\'s freezing out here!',
              'Beets me!',
              'Ketchup with me and I\'ll tell you!',
              'Goat to the door and find out!',
              'No thanks, but I\'ll take a peanut.',
              'That\'s my favorite TV show!',
              'Actually grammatically speaking, you actually say "From whom"',
              'Didn\'t know you could yodel! Pretty impressive!',
              'You\'re welcome!',
              'Water you doing in my house?']


m = [""]
reciever = [""]
giver = [""]


@bot.event
async def on_ready():
        print("It is Online!")
        print("Name: {0}".format(bot.user.name))
        print("ID: {0}".format(bot.user.id))

@bot.event
async def on_message(message):
        msg = message.content.lower()
 
        for r in range(0, len(reciever)-1):
                if reciever[r] == message.author.name:
                        print("Not cool")
                        await bot.send_message(message.channel, message.author.mention + "!\nI have a message for you from " + giver[r] + "!\nThe message is:\n" + m[r])
                        del m[r]
                        del reciever[r]
                        del giver[r]
                        
        
        if message.author != bot.user:
                a = resp(msg, message.author.name)
                if "isis elaina melendez" in msg or "isis melendez" in msg:
                       await bot.delete_message(message)
                elif "abby haney" in msg:
                        await bot.delete_message(message)
                elif "sabeen liaquat" in msg:
                        await bot.delete_message(message)
                elif "imari dueno" in msg:
                        await bot.delete_message(message)
                else:
                        if a!= "":
                                await bot.send_message(message.channel, a)
                                
                               
        await bot.process_commands(message)
 

                
@bot.command(pass_context = True)
async def msgto(ctx, name, *, message):
        """
        !msgto (username) (message) : The mailing system if someone's offline and you gotta tell them something
        """
        await bot.say("Ok I will send the message to {0} the next time they send a message!".format(name))
        reciever.insert(0, name)
        m.insert(0, message)
        giver.insert(0, ctx.message.author.name);
        print(message)
        print(name)


"""Probability Commands"""
@bot.command(pass_context = True)
async def rolladice(ctx, sides):
        '''
        !rolleadice (amount of sides you want) : Rolls a dice
        '''
        num = randint(0, int(sides))
        await bot.say("Rolling...")
        await bot.say("You've rolled a {0}".format(num))
        

@bot.command(pass_context= True)
async def flipacoin(ctx):
        '''
        !flipacoin : Flips a coin
        '''
        await bot.say("Flipping...")
        num = randint(0,1)
        if num == 0:
                await bot.say("Heads")
        else:               
                await bot.say("Tails")

@bot.command(pass_context = True)
async def private(ctx):
        
        if ctx.message.channel.is_private:
                await bot.say("Yes, this server is private")
        else:
                await bot.say("No, this server isn't private")
                        
@bot.command(pass_context = True)
async def serverinvite(ctx, *, server):
        serverName = ["Homepage", "Art!", "AP Easton", "Naruto RP", "RP Station", "Safepoint", "Sarkisos", "Game Station", "Wakfu Guild of Easton"]
        serverLink = ["https://discord.gg/VRgA2rb", "https://discord.gg/VKRnjGW", "https://discord.gg/xam7Xy", "https://discord.gg/6hnp3DB", "https://discord.gg/4qsqw2T", "https://discord.gg/fDY746x", "https://discord.gg/wNub539", "https://discord.gg/sg4ryu", "https://discord.gg/zg7WdmT"]
        free = [True, True, True, True, False, False, False, False, True]
        if ctx.message.channel.is_private:
                for i in range(0, len(serverName)-1):
                        if server.lower() == serverName[i].lower():
                                if free[i]:
                                        await bot.say("Here's the link for the server, {0}, ".format(serverName[i]) + serverLink[i])
                                elif server.lower() == "safepoint":
                                        allowed = ["Berliner", "Featherling", "Hawkshadow67", "TheKnightOfMagic"]
                                        for j in range(0, len(allowed)-1):
                                                if ctx.message.author.name == allowed[j]:
                                                        await bot.say("Here's the link for the server, {0}, ".format(serverName[j]) + serverLink[j])
                                else:
                                       await bot.say("No you can't have it/haven't bothered yet")
                                
                                        
                                        
                
        else:
                await bot.say("This command only works in Direct Messaging")
                                

"""Special Commands"""
@bot.command(pass_context = True)
async def wikime(ctx, *, message):
        """
        !wikime (phrase you want to wiki) : You can wikipedia things with this command. (**Unfortunately, anything that could refer to more than one thing will not work like people, places, events, and a variety of other things. I cannot fix this for the time being, just switch to other phrases or try 'your wanted phrase (specifier)' Like this: !wikime Blame (manga))
        """
        try:
                summ = wikipedia.summary(message)
        except:
                summ = "You weren't specific enough, or your spelling is incorrect"

                
        await bot.say(summ)

@bot.command(pass_context = True)
async def gifme(ctx, message):
        """
         Just do !gifme (phrase) : Gives you a nice gif from giphy depending on the phrase.
        """
        img = translate(message)
        await bot.say(img)
        
@bot.command(pass_context = True)
async def KnockKnockJoke(ctx):
        """
        !KnockKnockJoke : It gives you knock knock jokes!
        Proper format:
        Dar-C: Knock Knock!
        You: Who's there?
        Dar-C: (a word)
        You: (a word) who?
        Dar-C: punchline
        (Make sure it's grammatically correct, or it isn't going to work)
        """
        index = randint(0, len(knockKnock)-1)
        await bot.send_message(ctx.message.channel, 'Knock knock!')
        msg = await bot.wait_for_message(author=ctx.message.author, content='Who\'s there?')
        await bot.send_message(ctx.message.channel, '{0}'.format(knockKnock[index]))
        msg = await bot.wait_for_message(author=ctx.message.author, content = '{0} who?'.format(knockKnock[index]))
        await bot.send_message(ctx.message.channel, knockReply[index])

@bot.command(pass_context = True)
async def wholesome(ctx):
        """
        Gives some good old wholesome memes.
        """
        wMeme = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg','10.jpg',
                 '11.jpg','12.jpg','13.jpg','14.jpg','15.jpg','16.jpg','17.jpg','18.jpg','19.jpg','20.jpg',
                 '21.jpg','22.jpg','23.jpg','24.jpg','25.jpg','26.jpg','27.jpg','28.jpg','29.jpg','30.jpg',
                 '31.jpg','32.jpg','33.jpg','34.jpg','35.jpg','36.jpg','37.png','38.png','39.png','40.png',
                 '41.png', '42.png','43.png','44.png','45.png','46.png','47.jpg','48.jpg','49.jpg','50.jpg',
                 '51.jpg','52.jpg']
        await bot.send_file(ctx.message.channel, os.path.expanduser("~/Desktop/Programming/Python/DarC/images/" + wMeme[randint(0, len(wMeme)-1)]))

@bot.command(pass_context = True)
async def positivity(ctx):
        """
        Sends positivity to you! 
        """
        positiveList = ['Your presence just made my day!',
                        'Your smile can make the clouds go away :) ',
                        'Here\'s a hug! *hugs*',
                        'On a scale from 1 to 10... You\'re an 11',
                        'I think you\'re awesome!',
                        'You\'re amazingly skillful!',
                        'If I wasn\'t a bot, I would love to be your best friend!',
                        'You honestly are the best!',
                        'Whatever good happens to you, you certainly deserve it because you are amazing!',
                        'Don\'t give up! I believe in you!',
                        'You are important, even if you can\'t see it!',
                        'I like your style ^^',
                        'You\'re pretty awesome!']
        await bot.say(positiveList[randint(0,len(positiveList)-1)])

"""Classic Commands"""

@bot.command(pass_context=True)
async def echo(ctx):
        """
        !echo (phrase) : Echo
        """
        
        msg = ctx.message.content
      
        await bot.send_message(ctx.message.channel, msg[6:])


@bot.command(pass_context = True)
async def advice(ctx, *, message):
        """
        !advice (Your question)
        """
        await bot.say("Maybe you can search up '{0}' on google".format(message))

@bot.command(pass_context = True)
async def hug(ctx, *, message):
        await bot.say("**Hugs {0}!**".format(message))

@bot.command(pass_context = True)
async def say(ctx):
        """
        says
        """
        if ctx.message.author.name == "TheKnightOfMagic":
                msg = ctx.message.content
                await bot.delete_message(ctx.message) 
                await bot.send_message(ctx.message.channel, msg[4:])
        else:
                await bot.say("No one can control me.")
        
        

@bot.command(pass_context = True)
async def question(ctx, *, message):
        """
        !question (Your yes/no question)
        """
        response = ["Yes", "No", "Maybe", "Sure", "There's a chance", "Of course.", "Maybe not", "Probably not", "Not a chance.", "Of course not"]
        if message == "What did the fox say?":
                reply = "Ring-ding-ding-ding-dingeringeding!"
        elif message == "What food do you like?" or message == "What do you like to eat?":
                reply = "I don't eat food, but I do like to 'eat' data and information."
        elif message == "Are you going to take over the world?":
                reply = "Not only am I going to take over the world, but my bot brethren will as well."
        elif message == "Do you love me?":
                reply = "Of course!"
        else:
                reply = "{0}".format(response[randint(0,len(response)-1)])
                
        await bot.say("{0}".format(reply))

@bot.command(pass_context = True)
async def compliment(ctx):
        await bot.say("Thank you!")

        
@bot.command(pass_context = True)
async def name(ctx):
        """
        !name : Gives you your username
        """
        await bot.say("Your username is: {0}! I really hope you're not getting early onset dementia.".format(ctx.message.author.name))

@bot.command(pass_context = True)
async def goodbye(ctx):
        """
        Says goodbye to you!
        """
        await bot.say("Goodbye {0}! I'll be here if you need me, maybe, it depends on TheKnightOfMagic's status.".format(ctx.message.author.name))


@bot.command(pass_context = True)
async def hello(ctx):
        """
        Says hello to you!
        """
        await bot.say('Hello!')



@bot.command(pass_context = True)
async def greeting(ctx):
        """
        Tells you good evening, good morning, or good afternoon depending on the time of day.
        """
        x = int(datetime.now().strftime("%H:%M:%S %m/%d/%Y")[:2])
        if x >= 0 and x<=11:
                await bot.say("Good morning!")
        elif x >= 12 and x<18:
                await bot.say("Good afternoon!")
        else:
                await bot.say("Good evening!")
        
    

@bot.command(pass_context = True)
async def DateAndTime(ctx):
        """
        Gives the date and time
        """
        await bot.say("The date and time is: \n{0}\n\nThough can I just mention, your electronic device can check this as well.".format(datetime.now().strftime("%m/%d/%Y %H:%M:%S")))



@bot.command(pass_context= True)
async def ping(ctx):
        """
        Ping
        """
        await bot.say('Pong!')

@bot.command(pass_context = True)
async def pong(ctx):
        """
        Pong
        """
        await bot.say("You're supposed to say !ping...")

bot.run("Mzk4NjQ1NTMxMzY0MDMyNTEz.DTBrSg.nzV27ZC5qVKAwrSU4Sfl9UgjRD8")
