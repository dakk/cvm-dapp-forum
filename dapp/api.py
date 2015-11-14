# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import logging
from . import message
from contractvmd import dapp, config, proto

logger = logging.getLogger(config.APP_NAME)

class ForumAPI (dapp.API):
	def __init__ (self, core, dht, api):
		self.api = api
		rpcmethods = {}

		rpcmethods["post"] = {
			"call": self.method_post,
			"help": {"args": ["key"], "return": {}}
		}

		rpcmethods["comment"] = {
			"call": self.method_comment,
			"help": {"args": ["key", "value"], "return": {}}
		}

		rpcmethods["getpost"] = {
			"call": self.method_getpost,
			"help": {"args": ["key", "value"], "return": {}}
		}

		rpcmethods["getpostlist"] = {
			"call": self.method_getpostlist,
			"help": {"args": ["key", "value"], "return": {}}
		}

		errors = { }
		super (ForumAPI, self).__init__(core, dht, rpcmethods, errors)


	def method_getpost (self, postid):
		v = self.core.getPost (postid)
		if v == None:
			pass #return self.createErrorResponse ('KEY_IS_NOT_SET')
		else:
			return v

	def method_getpostlist (self):
		v = self.core.getPostList ()
		return v

	def method_post (self, title, body):
		msg = message.ForumMessage.post (title, body)
		return self.createTransactionResponse (msg)

	def method_comment (self, postid, body):
		msg = message.ForumMessage.comment (postid, body)
		return self.createTransactionResponse (msg)
