import texttospeech
import speechtotext
import datetime
import webbrowser
import weather
def Action(data):
    # user_data=speechtotext.speechtotext()
    user_data=data.lower()

    if "what is your name" in user_data:
        texttospeech.texttospeech("My name is Virual Assistant")
        return "My name is Virual Assistant"
    elif "hello" in user_data or "hye" in user_data:
        texttospeech.texttospeech("hey,Sir How I can help you")
        return "hey,Sir How I can help you"
    elif "good morning" in user_data:
        texttospeech.texttospeech("good morning sir")
        return "good morning sir"
    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time= (str)(current_time)+ "Hour", (str)(current_time.minute)+"Minute"
        texttospeech.texttospeech(Time)
        return Time
    elif "shutdown" in user_data:

        texttospeech.texttospeech("ok sir")
        return "ok sir"
    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        texttospeech.texttospeech("gaana.com is now ready for you")
        return "gaana.com is now ready for you"

    elif "open chatgpt" in user_data:
        webbrowser.open("https://chatgpt.com/")
        texttospeech.texttospeech("chatgpt is now ready for you")
        return "chatgpt is now ready for you"
    elif "open google" in user_data:
        webbrowser.open("https://www.google.com/")
        texttospeech.texttospeech("Google is now ready for you")
        return "Google is now ready for you"
    elif "open Youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        texttospeech.texttospeech("Youtube is now ready for you")
        return "Youtube is now ready for you"
    elif "weather" in user_data:
        ans=weather.weather()
        texttospeech.texttospeech(ans)
        return ans

    else:
        texttospeech.texttospeech("I am not able to Understand")
        return "I am not able to Understand"
