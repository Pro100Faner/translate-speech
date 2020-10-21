import speech_recognition as sr
import pyaudio

open_comand = ["браузер", "страницу", "страница", "сайт"]
curr_process = []


def recog(r: sr.Recognizer(), audio: sr.AudioData, name_obr: list):
    a: str
    a = r.recognize_google(audio, language="Ru-ru")
    if a.split()[0] in name_obr and len(a.split()) >= 2:
        return a.split()
    else:
        raise sr.UnknownValueError


def get_key(lst: dict, wor: str):
    for key, var in lst.items():
        if wor in var:
            return key
    raise sr.UnknownValueError


def cheek_ind(key: str, speach_list: list):
    try:
        if key == "открыть":
            comand = speach_list[2]
            if comand in open_comand:
                oppen(speach_list[3:])
        elif key == "next":
            next_any()
        elif key == "выполнить":
            run_any()

    except:
        raise sr.UnknownValueError


def oppen(speach: list):
    """
    какой то код для открытия чего либо
    """
    pass


def next_any():
    """
    какой то код который переключает следующий элемент
    """
    pass


def run_any():
    """
    какой то код который что то выполняет
    """
    pass
