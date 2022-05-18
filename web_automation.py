import webbrowser as wbb

def web_automation():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    urls = ('apple.com', 'github.com', 'google.com', 'youtube.com')

    for url in urls:
        print('Opening: ' + url)
        wbb.get(chrome_path).open(url)

web_automation()