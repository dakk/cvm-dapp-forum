# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import logging

from contractvmd import dapp, config
from . import api, core, proto, message

logger = logging.getLogger(config.APP_NAME)

class forum (dapp.Dapp):
	def __init__ (self, chain, db, dht, apiMaster):
		self.core = core.ForumCore (chain, db)
		apiprov = api.ForumAPI (self.core, dht, apiMaster)
		super (forum, self).__init__(proto.ForumProto.DAPP_CODE, proto.ForumProto.METHOD_LIST, chain, db, dht, apiprov)

	def handleMessage (self, m):
		if m.Method == proto.ForumProto.METHOD_POST:
			logger.pluginfo ('Found new message %s: post %s', m.Hash, m.Data['title'])
			self.core.post (m.Hash, m.Player, m.Data['title'], m.Data['body'])
		elif m.Method == proto.ForumProto.METHOD_COMMENT:
			logger.pluginfo ('Found new message %s: comment on post %s', m.Hash, m.Data['postid'])
			self.core.comment (m.Hash, m.Player, m.Data['postid'], m.Data['body'])
