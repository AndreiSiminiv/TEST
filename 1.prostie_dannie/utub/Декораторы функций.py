import webbrowser

def validator(func):
    def wraper(url):
        if '.' is url:
            func(url)
        else:
             print('Не верный url')
    return wraper

@validator

def open_url(url):
    webbrowser.open(url)

open_url('https://itproger.com')