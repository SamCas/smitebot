class BotUtils():
    def __init__(self):
        pass

    def getMessage(self, rawMessage):
        message = rawMessage.split(' ',1)
        return message[1]

    def parseMongoResponse(self, response):
        godName = response.get('godName')
        startingItems = ', '.join(response.get('start'))
        coreItems = ', '.join(response.get('core'))
        fullItems = ', '.join(response.get('full'))
        altItems = ', '.join(response.get('alt'))

        message = '```'
        message += 'God Name: {0}\n'.format(godName).title()
        message += 'Starting Items: \n {0}'.format(startingItems)
        message += '\nCore Items: \n {0}'.format(coreItems)
        message += '\nFull Items: \n {0}'.format(fullItems)
        message += '\nAlternative Items: \n {0}'.format(altItems)
        message += '```'
        print(response)
        return message