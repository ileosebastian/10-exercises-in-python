# import sys
# sys.path.append('../')
# from message import general_message

"""
    Cree una clase llmada SmartPhone, la cual debe tener una herencia multiple de
    las sigueitnes clases
        - Camara(App)
        - Llamadas(App, persona[])
        - Reproductor(App)
        - Tienda de apps(App)
    
    debe mostrar al final una instancia de la clase SmartPhone, a la cual mostrara
    cada accion que puede realizar
"""

class App:
    def __init__(self, name_app, size_app, version, desciption):
        self.__name_app = name_app 
        self.__size__app = float(size_app)
        self.__version = version
        self.__description = desciption 
    
    # Methods
    def aboutThisApp(self):
        return """
                La app {}, que pesa {} MB esta en la version {}. {}
            """.format(
                self.get_name_app(),
                self.get_size_app(),
                self.get_version(),
                self.get_description()
            )   

    def get_all_in_a_tuple(self):
        return tuple(self.__name_app, self.__size_app, self.__version, self.__description)
    # Getters and setters
    def get_name_app(self):
        return self.__name_app
    def set_name_app(self, value):
        self.__name_app = value
    
    def get_size_app(self):
        return self.__size__app
    def set_size_app(self, value):
        self.__size__app = value
    
    def get_version(self):
        return self.__version
    def set_version(self, value):
        self.__version = value
    
    def get_description(self):
        return self.__description
    def set_description(self, value):
        self.__description = value

from collections import namedtuple
class ManagerApp:
    __apps = namedtuple('Apps', ['name', 'size', 'version', 'description'])
    # args:
    #   list = [App1, App2]
    def __init__(self, apps_by_default):
        self.__list_app = self.new_apps_init(apps_by_default) 
    
    def new_apps_init(self, apps):
        new_list = []
        for app in apps:
            a = self.__apps(*app)
            new_list.append(App(a.name, a.size, a.version, a.description))
        return new_list
     
    def new_app(self, app):
        a = self.__apps(*app)
        self.__list_app.append(App(a.name, a.size, a.version, a.description))
    
    def find_app_by_name(self, name):
        for app in self.__list_app:
            if app.get_name_app() == name:
                return app
        return -1
    
    def desctibe_each_app(self):
        for app in self.__list_app:
            print(app.aboutThisApp())
    
    # Getters and setters
    def get_list_app(self):
        return self.__list_app
    def set_list_app(self, value):
        self.__list_app = self.new_apps_init(value) 
   
class Camera:
    __location = ["frontal", "trasera"]
    def __init__(self, resolution_camera):
        self.__resolution_camera = resolution_camera

    # Methods
    def CameraLocation(self):
        while True:
            cam = int(input("\tEscoja la camara: Frontal[1] Trasera[2]:"))
            if cam == 1 or cam == 2:
                break
        return cam -1
        
    def takeAPhoto(self):
        location = self.CameraLocation() 
        print("Tomando foto... con la camara {}".format(self.get_location(location)))
    
    def takeAVideo(self):
        location = self.CameraLocation() 
        print("Tomando video... con la camara {}".format(self.get_location(location)))

    # Getters and setters
    def get_resolution_camera(self):
        return self.__resolution_camera
    def set_resolution_camera(self, value):
        self.__resolution_camera = value
        
    def get_location(self, index):
        return self.__location[index]
    def set_location(self, value):
        self.__location = value    
    
class SmartPhone(Camera, ManagerApp):
    def __init__(self, apps_by_default, resolution_camera):
        super(ManagerApp, self).__init__() 
        self.set_list_app(apps_by_default)
        self.set_resolution_camera(resolution_camera)

    def aboutCamera(self):
        print(
            """
                La camara tiene {} megapixeles, y es asi tanto para la frontal, como
                la trasera.
            """.format(
                self.get_resolution_camera()
            )
        )    
        while True:
            decision = int(input("Desea tomar un video[1] o una foto[2] o no[0]?"))
            if decision == 1 or 2 or 0:
                break
        if decision == 1:
            self.takeAVideo()
        elif decision == 2:
            self.takeAPhoto() 
    


if __name__ == "__main__":
    # general_message()

    apps_by_default = [
        ("WhatsApp", 22, "a12.0.13", "Es una app de mensajeria instantanea."),
        ("Telegram", 23, "a1.4.2", "Es una app de mensajeria instantanea."),
        ("Google", 221, "a40.12.1", "Es una motor de busqueda y demas servicios."),
        ("Linkdin", 204, "a3.0.7", "Es una app para buscar empleo en empresas."),
        ("Facebook", 160, "a66.3.2", "Es una red social."),
    ]    
    
    phone_1 = SmartPhone(apps_by_default, 34) 

    print("\nAcerca de la camara del telefono inteligente.")
    phone_1.aboutCamera()

    phone_1.new_app(("Youtube", 122, "1.2.3A", "Es una app para ver videos online."))

    print("\nDescripcion de todas las apps del telefono inteligente")
    phone_1.desctibe_each_app()

    