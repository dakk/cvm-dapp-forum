# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from contractvmd.chain import message
from . import proto

class ForumMessage (message.Message):
	def post (title, body):
		m = ForumMessage ()
		m.Title = title
		m.Body = body
		m.DappCode = proto.ForumProto.DAPP_CODE
		m.Method = proto.ForumProto.METHOD_POST
		return m

	def comment (postid, body):
		m = ForumMessage ()
		m.PostID = postid
		m.Body = body
		m.DappCode = proto.ForumProto.DAPP_CODE
		m.Method = proto.ForumProto.METHOD_COMMENT
		return m


	def toJSON (self):
		data = super (ForumMessage, self).toJSON ()

		if self.Method == proto.ForumProto.METHOD_POST:
			data['title'] = self.Title
			data['body'] = self.Body
		elif self.Method == proto.ForumProto.METHOD_COMMENT:
			data['postid'] = self.PostID
			data['body'] = self.Body
		else:
			return None

		return data
