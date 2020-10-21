from Function import recog, get_key, cheek_ind
import speech_recognition as sr

name_obr = ["имя1", "имя2"]
wordKey = {"next": ["следующий", "next", "далее", "другой", "дальше", "следуящая"],
           "открыть": ["открыть", "открой", "открывать"],
           "выполнить": ["выполни", "сделай", "выполнить", "сделать"]}

r = sr.Recognizer()
r.energy_threshold = 4000

while 1:
    try:
        with sr.Microphone() as sourse:
            print("Speech")
            audio = r.listen(sourse)
        speechString = recog(r, audio, name_obr)
        comand = get_key(wordKey, speechString[1])
        cheek_ind(comand, speechString)

    except IOError:
        print("Не найден микрофон")
    except sr.UnknownValueError:
        print("не удалось распознать")
    except IndexError:
        print("длинна меньще 2")
