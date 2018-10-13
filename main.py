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
delay = int(delay)

# Create VK session
vksession = vk.Session()
vkapi = vk.API(vksession)

# Functions
def loaddoc (name): # Load documentation
	doc = open(docsdir + '/' + name, 'r')
	doc = doc.read()
	return doc
def loadcopypaste(name): # Load copypaste
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
	message = arguments.message
	message = loadcopypaste(message)
	attachments = arguments.attachments
	while True:
		for post in target['items']:
			print(wallpostcomment(owner_id, post['id'], message, attachments))
			time.sleep(delay)
		time.sleep(10)
if(seltype == 'wallpost'):
	owner_id = arguments.owner_id
	int(owner_id)
	message = arguments.message
	message = loadcopypaste(message)
	attachments = arguments.attachments
	while True:
		wallpost(owner_id, message, attachments)
		time.sleep(delay)
if(seltype == 'confshit'):
	chat_id = arguments.chat_id
	message = arguments.message
	album = inalbum(shitpost_album_owner_id, shitpost_album_id, 300, 1)
	while True:
		photo = random.choice(album)
		photo = genPhotoAttachment(photo['owner_id'], photo['id'])
		print(sendToConf(chat_id, message, photo))
		time.sleep(delay)
