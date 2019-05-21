
import numpy as ny 
import random
import string
import nltk as n
from nltk.stem import WordNetLemmatizer
import warnings
#se importa directamente la libreria
from nltk.chat.util import Chat, reflections

##Se importan 2 cosas: la clase Chat (viene con la libreria) y reflections, su diccionario
from sklearn.feature_extraction.text import TfidfVectorizer



warnings.filterwarnings("ignore")


fin=open('FIA.txt','r',encoding='utf-8',errors='ignore')
raw= fin.read().lower() #El lower vuelve todas las letras en minuscula


sent_token=n.sent_tokenize(raw) #Las vuelve oraciones
word_token=n.word_tokenize(raw) #Las vuelve palabras

sent_token[:2] #Cuantas oraciones como maximo el bot puede enviar

word_token[:5] #Cuantas palabras en clave puede reconocer a la vez

l=WordNetLemmatizer()


#Se puede modificar el diccionario de la siguiente manera:
reflections={
    "yo soy" : "tu eres",
    "yo fui" : "tu fuiste",
    "yo seré" : "tu seras",
    "yo sere" : "tu seras",
    "yo":"tu",
    "mi":"tu",
    "tu eres" : "yo soy",
    "tu fuiste" : "yo fui",
    "tu seras" : "yo seré",
    "tu":"yo",
    "tuyo":"mio",
    "tu":"mio",
    "ellos":"ellos",
    "nosotros":"ustedes",
    "mio":"tuyo",
    "mi":"tu",
    "nos":"se",
    "ellas":"ellas",
    "me":"te",
    "mia":"tuya",
    "somos":"son",
    "fuimos":"fueron",
    "seremos":"seran",

}
#Puede agregar otros


def LemTokens(tks):
    return [l.lemmatize(t) for t in tks] 



Saludos={"hola","hey","habla","que tal","buenas"}
Respuestas=["Buenas","Bienvenido/a","Hola","Hey","Un gusto conocerte"]
Despedida=["Nos vemos","Adios","Un gusto hablar contigo","Cerrando sección"]
Desentendido=["Lo siento, puedes repetir eso?","Puedes decir otra cosa,porfa?","No se si lo entiendo","Como?","Otra pregunta,por favor","Habla español, por favor"]

#def saludo_usuario(oracion):
    #for word in oracion.words:
        



if(23>20):
    print('Cierto')
else:
    print('Falso')
