#!/usr/bin/python3
# Copyright (c) 2015 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from libcontractvm import Wallet, WalletExplorer, ConsensusManager
from forum import ForumManager
import sys
import config

consMan = ConsensusManager.ConsensusManager ()
consMan.bootstrap ("http://127.0.0.1:8181")

wallet = WalletExplorer.WalletExplorer (wallet_file='test.wallet')
fMan = ForumManager.ForumManager (consMan, wallet=wallet)

if __name__ == "__main__":
	if len (sys.argv) > 1:
		if sys.argv[1] == 'post':
			fMan.post (input ('Title: '), input ('Body: '))
			sys.exit (0)

		elif sys.argv[1] == 'getpostlist':
			pl = fMan.getPostList ()
			for p in pl:
				print (p['id'], '\t', p['title'])
			sys.exit (0)

		elif sys.argv[1] == 'getpost':
			p = fMan.getPost (input ('Post ID: '))
			print ('ID:', p['postid'], '\nTitle:', p['title'])
			print ('Sender:', p['player'])
			print (p['body'])
			for c in p['comments']:
				print ('\t', c['player'], '->', c['body'])
			sys.exit (0)

		elif sys.argv[1] == 'comment':
			fMan.comment (input ('Post ID: '), input ('Body: '))
			sys.exit (0)

	print ('usage:', sys.argv[0], 'post|getpostlist|comment|getpost')
