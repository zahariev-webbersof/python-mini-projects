def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    import requests
    import json

    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = " https://newsapi.org/v1/articles"
    res = requests.get(main_url, params=query_params)
    load = json.loads(res.text)
    speak('Here you listen top BBC news from SoftUni Fundamentals Team. Lets began')
    speak('first news')

    for i in range(4):
        print(load['articles'][i]['title'])
        speak(load['articles'][i]['title'])
        if i < 3:
            speak('next news')
        else:
            speak('This was top 4 BBC news from SoftUni Fundamentals Team.See you Soon')