# -*- coding: utf-8 -*-
# Import modules
import vk
import sys
import time
import random
import argparse
import clipboard
import configparser

# Parse config
config = configparser.RawConfigParser()
config.read ('etc/main.conf')

# Get properties
v = config.get('Api', 'v') # Get API version
delay = config.get('Misc', 'delay') # Get delay
docsdir = config.get('Filesystem', 'docsdir') # Get docsdir
token = config.get('User', 'accessToken') # Get auth token
copypastedir = config.get('Filesystem', 'copypastedir') # Get copypastedir
shitpost_album_owner_id = config.get('Shitpost', 'album_owner_id')
shitpost_album_id = config.get('Shitpost', 'album_id')
delay = float(delay)

# Create VK session
vksession = vk.Session()
vkapi = vk.API(vksession)

# Functions
def loaddoc (name): # Load documentation
	doc = open(docsdir + '/' + name, 'r')
	doc = doc.read()
	return doc
def zlogen(power):
	phrases = [
		'ЖЫВТОНЕЧОЧОУПЯЧКА1111111',
		'ОЯЕБУ!!!!!!11!!адинадин',
		'ОНОТОЛЕ НЕГОДУЕ!111',
		'ВОЕНЕ УПЧК СТРАШНЕ ОТАКЕ ДДоСЕ!111',
		'ПОПЯЧТС!11!!!1',
		'ЪЕЧЧОЖА!!!!11',
		'ЛуЧИ ПОНОСА!!!1111111',
		'СВОБОДА РАВЕНСТВО УПЯЧКА!11111!1С.Р.У111111111!!!',
		'ОН КАГБЕ ГОВОРИ НАМ -',
		'ОТАКе ВОЕНЕ!111',
		'ПОТС ЗОХВАЧЕН111',
		'ЕБАНЕМСЯ НА ОТЛИЧНЕНЬКО!!!111',
		'ОНОТОЛЕ ПРОКЛИНАЕ УГ!!111',
		'ЖЕПЬ ЕБРИЛО!!11111111адинадин',
		'ХУРЬ!!!1',
		'ЧАКЕ СТРАШНЕ ГНЕВЕ!111адин11',
		'ДОЛГОПЯТ КАКБЕ ЛЮБИМЕ ЖЫВТОНЕ ОНОТОЛЕ!!!111',
		'УПЯЧКОЧАТ11!!!!адин1',
		'МЖВЯЧНИ ПРДУНЬ–ПРДУНЬ1111',
		'ЪЖЧЛО!адин11111!!!!!',
		'ЖАЖА11!',
		'СЛАВА ЛЕОНИДЕ!111',
		'ГЛАНДЭ ОЯЕБУ ПОПЯЧТС!1111аДИН',
		'ПыЩЩЩЩЩЩ!!!!!!1111 ПЫЩЩЩЩЩЩ!!111 ПыЩЩЩЩЩЩЩЩЩ!!!!!!1111111СТОАДИНАЦАТЬ',
		'ОНОТОЛЕ КАКБЕ БЛАГОСЛОВЛЯЕ ДОБЛЕСТНЕ ВОЕНЕ УПЧК!!111адинадин',
		'СМОТРИ БАЛЕТ СУКА!1111',
		'УГ НА ГЛАГНЕ!!111',
		'ЭЕКСТЕЛР ТЫОЙ ЯЕБАНЕЙУ КОТУ111111111',
		'Я ИДИОТ1УБЕЙТЕ МЕНЯ КТО–НИБУДЬ!',
		'ОНОТОЛЕ СЕРЧАЕ!!111адинадин',
		'ЖРИ ПЯНИ СУКА!111',
		'НЕ ПОТСЬ УГ НА ГЛАГНЕ!!!!1111111АДИН',
		'СЛАВА ОНОТОЛЕ!111',
		'Медведев — шмель11111111 ЖЖЖЖЖ1111111!111',
		'ОНОТОЛЕ КАКБЕ БЛАГОСЛОВЛЯЕ ДОБЛЕСТНЕ ВОЕНЕ УПЧК!!111адинадин',
		'ЕБАНИСТЫД!!1',
		'ПЕПЯКОТУТСЯ!11111адин',
		'ОНОТОЛЕЙ!!!11',
		'А ТЫ ЗНАЕШЬ В ЧЁМ СОЛЬ, %USERNAME%?!1711',
		'СКОЛОПЕНДРЕ БОДРЕ И МОГУЧЕ ЖЫВТОНЕ - НАСЕКОМЕ!!11',
		'ПЫЩЩЩЩЩЩ!!111аДИН',
		'ТЫ ПРОБОВАЛ ЛИЗАТЬ ОКТАЭДР??777!1',
		'С.Р.У11!!111',
		'УПЯЧКА СЛЕДИТ ЗА ТОБОЙадин1!111111!!!',
		'СИСЬКЕ!111'
	]
	i = 0
	zlo = ''
	while i < power:
		i+=1
		zlo += random.choice(phrases)
	return zlo
def loadcopypaste(name): # Load copypaste
	if name == 'ZLO':
		copypaste = zlogen(15)
	elif name == '' or name == None:
		copypaste = ''
	else:
		copypaste = open(copypastedir + '/' + name, 'r')
		copypaste = copypaste.read()
	return copypaste
def createparser(): # Create command's arguments parser
	parser = argparse.ArgumentParser()
	return parser
def wallposts(owner_id, count): # Get posts in wall
	wallposts = vkapi.wall.get(
		owner_id = owner_id,
		count = count,
		access_token = token,
		v = v
	)
	return wallposts
def wallpostcomment(owner_id, post_id, message, attachments=''): # Send comment to post in wall
	response = vkapi.wall.createComment(
		owner_id = owner_id,
		post_id = post_id,
		message = message,
		attachments = attachments,
		v = v,
		access_token = token
	)
	return response
def wallpost(owner_id, message, attachments=''):
	response = vkapi.wall.post(
		owner_id = owner_id,
		message = message,
		v = v,
		access_token = token
	)
	return response
def inalbum(owner_id, album_id, count, rev):
	response = vkapi.photos.get(
		access_token = token,
		owner_id = owner_id,
		album_id = album_id,
		count = count,
		rev = rev,
		v = v
	)
	return response['items']
def genPhotoAttachment(owner_id, photo_id):
	return 'photo' + str(owner_id) + '_' + str(photo_id)
def sendToConf(chat_id, message, attachment):
	return vkapi.messages.send(
		chat_id = chat_id,
		message = message,
		attachment = attachment,
		v = v,
		access_token = token
	)

# Select attack type
argparser = createparser()
argparser.add_argument('--type')
argparser.add_argument('--count')
argparser.add_argument('--message')
argparser.add_argument('--chat-id')
argparser.add_argument('--owner-id')
argparser.add_argument('--attachments')
arguments = argparser.parse_args()
seltype = arguments.type
if seltype == 'wallcomments':
	# Wall comments attack
	int(arguments.count)
	int(arguments.owner_id)
	count = arguments.count
	owner_id = arguments.owner_id
	target = wallposts(owner_id, count)
	namemessage = arguments.message
	attachments = arguments.attachments
	while True:
		message = loadcopypaste(namemessage)
		for post in target['items']:
			print(wallpostcomment(owner_id, post['id'], message, attachments))
			time.sleep(delay)
		time.sleep(10)
if(seltype == 'wallpost'):
	owner_id = arguments.owner_id
	int(owner_id)
	namemessage = arguments.message
	attachments = arguments.attachments
	while True:
		message = loadcopypaste(namemessage)
		wallpost(owner_id, message, attachments)
		time.sleep(delay)
if(seltype == 'confshit'):
	chat_id = arguments.chat_id
	namemessage = arguments.message
	album = inalbum(shitpost_album_owner_id, shitpost_album_id, 1000, 1)
	i = 0
	while True:
		message = loadcopypaste(namemessage)
		photo = random.choice(album)
		photo = genPhotoAttachment(photo['owner_id'], photo['id'])
		print('PASS #' + str(i) + '	' + str(sendToConf(chat_id, message, photo)))
		i += 1
		time.sleep(delay)
