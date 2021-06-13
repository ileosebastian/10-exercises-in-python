# import sys
# sys.path.append('../')
# from message import general_message 

"""
        
"""

class Person:
    def __init__(self, names):
        self.__fname = names
    
    # Methods
    def get_fname(self):
        return self.__fname
    def set_fname(self, value):
        self.__fname = value

class Language:
    def __init__(self):
        self.__lang_names = "" 
        self.__origin = "" 
    
    # Methods
    def speak(self, lan):
        return "esta hablando en el idioma {}".format(lan) 
    def write(self, lan):
        return "esta escribiendo en el idioma {}".format(lan) 
    def listen(self, lan):
        return "esta escuchando el idioma {}".format(lan) 
    def read(self, lan):
        return "esta leyendo en el idioma {}".format(lan) 


    # Getter and setter
    def get_lang_names(self):
	    return self.__lang_names
    def set_lang_names(self, value):
	    self.__lang_names = value
    
    def get_origin(self):
	    return self.__origin
    def set_origin(self, value):
	    self.__origin= value

class Boxing:
    def __init__(self):
        self.__sport_name - ""
        self.__years_playing = 0
     
    # Methods
    def kick(self):
        return "esta entrenando golpes en el saco"
    def run(self):
        return "esta corriendo al rededor del campo"
    
    # Getter and setter
    def get_sport_name(self):
	    return self.__sport_name
    def set_sport_name(self, value):
	    self.__sport_name = value
    
    
    def get_years_playing(self):
	    return self.__years_playing
    def set_years_playing(self, value):
	    self.__years_playing = value

class Music:
    def __init__(self):
        self.__music_genre = ""
        self.__instrument = ""
    
    # Methods
    def play_song(self, song):
        return "esta tocando la cancion {} con su {}".format(song, self.get_instrument())
    
    # Getter and setter
    def get_music_genre(self):
	    return self.__music_genre
    def set_music_genre(self, value):
	    self.__music_genre = value
    
    def get_instrument(self):
	    return self.__instrument
    def set_instrument(self, value):
	    self.__instrument = value


class MultiFaceted(Person, Language, Boxing, Music):
    def __init__(self, names):
        super().__init__(names)
        self.__opinion = "Ninguna" 
    
    def description(self):
        print(
            """
                Hola! soy {}, soy una muy versada en diferentes disciplinas, como:
                    La musica:
                        Soy experto en musica {} y toco el instrumento {}.
                    Lenguas:
                        Se varios idiomas, entre ellos el {}, de origen {}.
                    Boxeo:
                        Conozo dicho deporte, pues llevo practicandolo hace {} anios.
                Puedo hacer una demostracion y dar mi opinion experta sobre estos temas.
            """.format(
                self.get_fname(),
                self.get_music_genre(),
                self.get_instrument(),
                self.get_lang_names(),
                self.get_origin(),
                self.get_years_playing(),
            )
        )
    
    def performance(self):
        print(
            """
            Demostracion de las facetas
                {} {}.
                {} {}.
                {} {}.
                {} {}.
                {} {}.
            """.format(
                self.get_fname(), self.read(self.get_lang_names()),
                self.get_fname(), self.write(self.get_lang_names()),
                self.get_fname(), self.kick(),
                self.get_fname(), self.play_song("Las cuatro estaciones"),
                self.get_fname(), self.speak(self.get_lang_names())
            )
                
        )
    
    def get_opinion(self):
        return self.__opinion
    def set_opinion(self, value):
        self.__opinion = value



if __name__ == "__main__":
    # general_message()
    
    a_multi_faceted = MultiFaceted("Sherlock Holmes")

    a_multi_faceted.set_music_genre("Clasica")
    a_multi_faceted.set_instrument("Violin")
    
    a_multi_faceted.set_lang_names("aleman")
    a_multi_faceted.set_origin("germanico")
    
    a_multi_faceted.set_sport_name("Boxeo")
    a_multi_faceted.set_years_playing(10)

    a_multi_faceted.description()
    
    a_multi_faceted.performance()
