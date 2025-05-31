import webbrowser

## Öffnen Sie eine URL im Standardbrowser
webbrowser.open('https://www.labex.io')

## Öffnen Sie einen bestimmten Browser
chrome_path = webbrowser.get('chrome')
chrome_path.open('https://www.labex.io')
