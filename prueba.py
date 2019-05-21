
import numpy as ny 
import random
import string
import nltk as n
from nltk.stem import WordNetLemmatizer
import warnings
#se importa directamente la libreria
from nltk.chat.util import Chat, reflections

##Se importan 2 cosas: la clase Chat (viene con la libreria) y reflections, su diccionario


from sklearn.feature_extraction.text import TfidfVectorizer as tfd

#Se lee la respuesta del usuario y las compara con las palabras del corpus (el archivo que lee)
from sklearn.metrics.pairwise import cosine_similarity as cs


warnings.filterwarnings("ignore")


fin=open('FIA.txt','r+',encoding='utf-8',errors='ignore')
raw= fin.read().lower() #El lower vuelve todas las letras en minuscula


sent_token=n.sent_tokenize(raw) #Las vuelve oraciones
word_token=n.word_tokenize(raw) #Las vuelve palabras

sent_token[:2] #Cuantas oraciones como maximo el bot puede enviar

word_token[:5] #Cuantas palabras en clave puede reconocer a la vez

l=WordNetLemmatizer()


#Se puede modificar el diccionario de la siguiente manera:
#Puede agregar otros


#Se procesan los tokens y devuelve tokens normalizados
def LemTokens(tks):
    return [l.lemmatize(t) for t in tks] 
#Se crea el diccionario
punt=dict((ord(p),None) for p in string.punctuation)

#Se ejecuta la normalizacion (se traduce de tal forma que se eviten problemas)
def LemNormalizacion(text):
    return LemTokens(n.word_tokenize(text.lower().translate(punt)))



Saludos={"hola","hey","habla","que tal","buenas"}
Respuestas=["Buenas","Bienvenido/a","Hola","Hey","Un gusto conocerte"]
Despedida=["Nos vemos","Adios","Un gusto hablar contigo","Cerrando sección"]
Desentendido=["Lo siento, puedes repetir eso?","Puedes decir otra cosa,porfa?","No se si lo entiendo","Como?","Otra pregunta,por favor","Habla español, por favor"]
Agradecimiento=["De nada","A tu servicio","No hay de que"]

def saludo_usuario(oracion):
    for word in oracion.split():
        if word.lower() in Saludos:
            return random.choice(Respuestas)
        
def conversacion(respuesta):
    resRob=''
    sent_token.append(respuesta)
    fv=tfd(tokenizer=LemNormalizacion)
    fid=fv.fit_transform(sent_token)
    valores=cs(fid[-1],fid)
    index=valores.argsort()[0][-2]
    flat=valores.flatten()
    flat.sort()
    request=flat[-2]
    if(request==0):
        resRob+=random.choice(Desentendido)
        return resRob
    else:
        resRob+=sent_token[index]
        return resRob

flag=True
print("Bienenido/a a esta prueba de chatbot en Python. Algunas funciones siguen en desarrollo. Si lo que quieres es salir, escribe 'adios'")
while (flag==True):
    respuesta=input()
    respuesta=respuesta.lower()
    if(respuesta!='adios'):
        if(respuesta=='gracias'):
            print("EDI:"+random.choice(Agradecimiento))
        elif(respuesta=='jojo'):
            print("EDI: So no chi no sadame\nEDI: JOOOOOOOOOOOOOOOJO")
        else:
            if(saludo_usuario(respuesta)!=None):
                print("EDI:"+saludo_usuario(respuesta))

            else:
                print("EDI:",end="")
                print(conversacion(respuesta))
                sent_token.remove(respuesta)

    else:
        flag=False
        print("EDI:"+random.choice(Despedida))
        
    

