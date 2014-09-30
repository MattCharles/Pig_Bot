import praw
import re

r = praw.Reddit('Pig Latin Translator by /u/just_another_sheep v0.1. ')
r.login('Pig_Bot', 'readfromtext')

#main loop - look at posts from /r/all - switch to /r/test for debugging

all_comments = r.get_comments('all')
#flat_comments = praw.helpers.flatten_tree(all_comments)

#Maintain a list of comments that have been translated so we don't spam
already_done = set()
our_comment = ''
VOWELS = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
PUNCTUATION = (".", ",", ":", "?", "!", ";")

while True:

#evaluate comments without worrying about their rank
	for comment in all_comments:
	
		#Find comments containing "Pig Latin"
		if "Pig Latin" in comment.body and comment.id not in already_done:

			words = re.split(' ', comment.body)
			#words is a list of the words in the comment
		
			for entry in words:
				#translate into Pig Latin
	
				#if it starts with a vowel, just add -ay
				if entry[0] in VOWELS:
					our_comment += entry + "ay" + " "
	
				else:
					our_comment += entry[1:] + entry[0] + "ay" + " "
			
			#comment result
			comment.reply(our_comment)
	
			already_done.add(comment.id)
