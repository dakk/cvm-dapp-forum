# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from libcontractvm import Wallet, ConsensusManager, DappManager

class ForumManager (DappManager.DappManager):
	def __init__ (self, consensusManager, wallet = None):
		super (ForumManager, self).__init__(consensusManager, wallet)

	def post (self, title, body):
		return self.produceTransaction ('forum.post', [title, body])

	def comment (self, postid, body):
		return self.produceTransaction ('forum.comment', [postid, body])

	def getPost (self, postid):
		return self.consensusManager.jsonConsensusCall ('forum.getpost', [postid])['result']

	def getPostList (self):
		return self.consensusManager.jsonConsensusCall ('forum.getpostlist', [])['result']
