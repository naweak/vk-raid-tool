# -*- coding: utf-8 -*-
# Import modules
import vk
import sys
import time
import argparse
import clipboard
import configparser

# Parse config
config 			= configparser.RawConfigParser()
config.read	('etc/main.conf')

# Get properties
v 						= config.get('Api', 'v')					# Get API version
delay	 				= config.get('Misc', 'delay')				# Get delay
docsdir		 			= config.get('Filesystem', 'docsdir') 		# Get docsdir
token					= config.get('User', 'accessToken')			# Get auth token
copypastedir		 	= config.get('Filesystem', 'copypastedir') 	# Get copypastedir
delay 					= int(delay)

# Create VK session
vksession 		= vk.Session()
vkapi 			= vk.API(vksession)

# Functions
def loaddoc (name): 												# Load documentation
	doc 		= open(docsdir + '/' + name, 'r')
	doc 		= doc.read()
	return doc
def loadcopypaste(name): 											# Load copypaste
	copypaste 	= open(copypastedir + '/' + name, 'r')
	copypaste	= copypaste.read()
	return copypaste
def createparser(): 												# Create command's arguments parser
	parser		= argparse.ArgumentParser()
	return parser
def wallposts(owner_id, count):										# Get posts in wall
	wallposts 	= vkapi.wall.get(
		owner_id 		= owner_id,
		count 			= count,
		access_token 	= token,
		v 				= v
	)
	return wallposts
def wallpostcomment(owner_id, post_id, message, attachments=''):	# Send comment to post in wall
	response = vkapi.wall.createComment(
		owner_id 		= owner_id,
		post_id			= post_id,
		message			= message,
		attachments		= attachments,
		v				= v,
		access_token	= token
	)
	return response

# Select attack type
argparser 		= createparser()
argparser.add_argument('--type')
argparser.add_argument('--count')
argparser.add_argument('--message')
argparser.add_argument('--owner-id')
argparser.add_argument('--attachments')
arguments		= argparser.parse_args()
seltype			= arguments.type
if seltype == 'wallcomments':
	# Wall comments attack
	int(arguments.count)
	int(arguments.owner_id)
	count 		= arguments.count
	owner_id 	= arguments.owner_id
	target		= wallposts(owner_id, count)
	message 	= arguments.message
	message		= loadcopypaste(message)
	attachments	= arguments.attachments
	while True:
		for post in target['items']:
			print(wallpostcomment(owner_id, post['id'], message))
			time.sleep(delay)
		time.sleep(10)