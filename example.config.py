# =====
# BASE_URL
# =====
# Used to generate redirect URL
#
### BASE_URL = 'http://django.localhost/ilt_client/'
## 2015/04/27 edit by lego
## This variable to not use in this application

# =====
# REDIRECT_URL
# =====
# If you just want to use default setting,
# 	1. please DO NOT change this  
# 	2. paste it your project "Redirect uri" in the ilt server
#
REDIRECT_URL = 'http://django.localhost/ilt_client/run'

# =====
# HOST_URL
# =====
# The ILT system oath base should be fixed to
# https://ilt.nchusg.org/oauth
#
HOST_URL = 'https://ilt.nchusg.org/oauth'

# =====
# CLIENT_KEY
# =====
# Go to https://ilt.nchusg.org/dev#projects to get one
#
CLIENT_KEY = 'TODO'

# =====
# CLIENT_SECRET
# =====
# Go to https://ilt.nchusg.org/dev#projects to get one
#
CLIENT_SECRET = 'TODO'

# =====
# SCOPE
# =====
# Go to https://github.com/NCHUSG/ilts#scopes to see avaible scoops
#
SCOPE = 'user.login.basic+user.isIn.dev'
