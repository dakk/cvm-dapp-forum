# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import logging
from contractvmd import dapp, config

logger = logging.getLogger(config.APP_NAME)

class ForumCore (dapp.Core):
	def __init__ (self, chain, database):
		database.init ('postlist', [])
		super (ForumCore, self).__init__ (chain, database)

	def post (self, pid, player, title, body):
		self.database.listappend ('postlist', {'id': pid, 'title': title})
		self.database.set (pid, {'postid': pid, 'player': player, 'title': title, 'body': body, 'comments': []})

	def comment (self, cid, player, pid, body):
		if not self.database.exists (pid):
			return False
		else:
			p = self.database.get (pid)
			p['comments'].append ({'commentid': cid, 'player': player, 'body': body})
			self.database.set (pid, p)
			return True

	def getPostList (self):
		return self.database.get ('postlist')

	def getPost (self, postid):
		if not self.database.exists (postid):
			return None
		else:
			return self.database.get (postid)
