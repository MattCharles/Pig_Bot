"""

Pig_Bot by MattCharles
Inspired by /u/thegreaterrobot on /r/RequestABot

TODO
 * Put this bot on a server!
 *
 * Store already_done on a file so we don't duplicate comments on reboot
 *
 * Handle punctuation - Done!
 *
 * Run on bot friendly subreddits
 *
"""

import praw, re

#Password hidden in extremely secure text file
with open('pass.txt', 'r') as pass_file:
	password = pass_file.read()

r = praw.Reddit('Pig Latin Translator by /u/just_another_sheep v0.2. ')
r.login('Pig_Bot', str(password)[:-1])

#main loop - look at posts from /r/all - switch to /r/test for debugging

all_comments = r.get_comments('test')
#flat_comments = praw.helpers.flatten_tree(all_comments)

#Maintain a list of comments that have been translated so we don't spam
already_done = set()
our_comment = ''
punct = ''
signature = '\n\n>I\'m [Pig_Bot](https://github.com/MattCharles/Pig_Bot), Pig translator extraordinaire.'
VOWELS = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
PUNCTUATION = (".", ",", ":", "?", "!", ";")

#while True:

#evaluate comments without worrying about their rank
for comment in all_comments:

	#Find comments containing "Pig Latin"
	if "Pig Latin" in comment.body and comment.id not in already_done:
		words = re.split(' ', comment.body)
		#words is a list of the words in the comment

		for entry in words:
			#translate into Pig Latin

			#handle punctuation
			if entry[-1] in PUNCTUATION:
				punct = entry[-1]
				entry = entry[:-1]

			#if it starts with a vowel, just add -ay
			if entry[0] in VOWELS:
				our_comment += entry + "ay" + punct  + " "

			else:
				our_comment += entry[1:] + entry[0] + "ay" + punct + " "
			
			#clear punctuation for next word
			punct = ''

		#comment result
		comment.reply(our_comment + signature)

		#clear for next comment
		our_comment = ''

		already_done.add(comment.id)
