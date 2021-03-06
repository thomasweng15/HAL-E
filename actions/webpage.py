

class Webpage():
	"""
	Process jobs that request to open a specified webpage.
	
	"""
	def __init__(self, speaker, actions_helper):
		self.speaker = speaker
		self.helper = actions_helper

	def process(self, job, controller):
		"""Process open webpage job request."""
		phrase = job.query
		url = self.make_url(phrase)
		if url != "":
			self.speaker.say("opening " + url[12:])
			controller.open(url)
			return True
		else:
			self.speaker.say("Sorry, I couldn't find the web page.")
			return False

	def make_url(self, phrase):
		"""Create url using the query and check domain existence."""
		# remove spaces in the phrase
		phrase = self.remove_spaces(phrase)

		# if phrase does not end with .com or other suffix append .com
		if phrase.find('.com') == -1 \
		and phrase.find('.edu') == -1 \
		and phrase.find('.org') == -1:
			phrase = phrase + ".com"

		# test website existence, return "" if website doesn't exist
		return self.helper.test_url(phrase)

	def remove_spaces(self, phrase):
		"""Remove spaces from the phrase."""
		space = phrase.find(' ')
		while space != -1:
			phrase = phrase[:space] + phrase[space + 1:]
			space = phrase.find(' ')
		return "https://www." + phrase.lower()

	