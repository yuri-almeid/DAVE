import wolframalpha

app_id = "5H3AXG-4PHL3HT6YJ"
client = wolframalpha.Client(app_id)

while True:
    q = input('You: ')
    res = client.query(str(q))
    ans = next(res.results).text

    print('BOT: ', ans)
