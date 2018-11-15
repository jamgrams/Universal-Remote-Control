#!/usr/bin/python

#This opens a tab on macOS



import webbrowser

url = 'http://www.mixer.com/thekillagrams'

chromePath = 'open -a /Applications/Google\ Chrome.app%s'

webbrowser.get(chromePath).open_new_tab(url)

browserStats = webbrowser.register('google-chrome',instance=None)

print(browserStats)