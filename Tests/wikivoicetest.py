import wikipedia # módulo do Wikipédia
wikipedia.set_lang('en') # Define lingua da pesquisa pelo wikipedia


def get_wiki(text):
    result = None
    results = None
    results = wikipedia.search(result)
    result = wikipedia.summary(results[0], sentences = 2)

    return result

while True:
    quest = input('search: ')
    
    resp = get_wiki(quest)

    print("BOT: " + resp)
