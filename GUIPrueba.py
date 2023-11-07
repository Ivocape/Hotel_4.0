  
import tkinter as tk
from managers import *

class HotelGUI:
    """
    A class representing the graphical user interface of a hotel management system.
    """

    def __init__(self, master):
        """
        Initializes the HotelGUI object.

        Parameters:
        master (tk.Tk): The root window of the GUI.
        """


        self.master = master
        master.title("Hotel Management System")

        # Initialize the managers for clients, personnel, administrators, rooms, reservations, and users
        self.clienteManager=clienteManager()
        self.personalManager=personalManager()
        self.adminManager=adminManager()
        self.roomManager=roomManager()
        self.reservaManager=reservaManager()
       

        # Create a label with the text "Bienvenido al hotel" and pack it into the master window
        self.label = tk.Label(master, text="Bienvenido al hotel")
        self.label.pack()
        # Add photo

        # Create a button with the text "Registrar" and a command to call the register method, then pack it into the master window
        self.register_button = tk.Button(master, text="Registrar", command=self.register)
        self.register_button.pack()

        # Create a button with the text "Iniciar sesión" and a command to call the start_session method, then pack it into the master window
        self.login_button = tk.Button(master, text="Iniciar sesión", command=self.start_session)
        self.login_button.pack()

        # Create a button with the text "Modificar" and a command to call the modify method, then pack it into the master window
        self.modify_button = tk.Button(master, text="Modificar", command=self.modify)
        self.modify_button.pack()

        # Create a button with the text "Salir" and a command to quit the master window, then pack it into the master window
        self.quit_button = tk.Button(master, text="Salir", command=master.quit)
        self.quit_button.pack()

    def register(self):
        """
        Initializes the registration screen.
        """

        # Change the label text to "Registro"
        self.label.config(text="Registro")

        # Remove the "Registrar", "Iniciar sesión", "Modificar", and "Salir" buttons from the master window
        self.register_button.pack_forget()
        self.login_button.pack_forget()
        self.modify_button.pack_forget()
        self.quit_button.pack_forget()

        # Create a label with the text "Nombre:" and pack it into the master window
        self.name_label = tk.Label(self.master, text="Nombre:")
        self.name_label.pack()

        # Create an entry field for the name and pack it into the master window
        self.name_entry = tk.Entry(self.master)
        self.name_entry.pack()

        # Create a label with the text "Apellido:" and pack it into the master window
        self.surname_label = tk.Label(self.master, text="Apellido:")
        self.surname_label.pack()

        # Create an entry field for the surname and pack it into the master window
        self.surname_entry = tk.Entry(self.master)
        self.surname_entry.pack()

        # Create a label with the text "Email:" and pack it into the master window
        self.email_label = tk.Label(self.master, text="Email:")
        self.email_label.pack()

        # Create an entry field for the email and pack it into the master window
        self.email_entry = tk.Entry(self.master)
        self.email_entry.pack()

        # Create a label with the text "Contraseña:" and pack it into the master window
        self.password_label = tk.Label(self.master, text="Contraseña:")
        self.password_label.pack()

        # Create an entry field for the password and pack it into the master window
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        # Create a label with the text "Tipo de usuario:" and pack it into the master window
        self.typeUser_label = tk.Label(self.master, text="Tipo de usuario:")
        self.typeUser_label.pack()

        # Create an entry field for the typeUser and pack it into the master window
        self.typeUser_entry = tk.Entry(self.master)
        self.typeUser_entry.pack()

        # Create a button with the text "Registrar" and a command to call the register_user method, then pack it into the master window
        self.register_user_button = tk.Button(self.master, text="Registrar", command=self.register_user)
        self.register_user_button.pack()
    def register_user(self):
        """
        Registers a new user with the given information.
        """

        # Get the name, surname, email, and password from the entry fields
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        typeUser = self.typeUser_entry.get()
        # Register the new user with the user manager
        if typeUser == "admin 1234":
            self.adminManager.createAdmin(typeUser,name,surname,email,password)
        elif typeUser == "cliente": 
            self.clienteManager.createCliente(typeUser,name,surname,email,password)
        elif typeUser == "personal 1234":
            self.personalManager.createPersonal(typeUser,name,surname,email,password)
        # Usuario registrado con éxito, por favor inicie sesión
        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.surname_label.pack_forget()
        self.surname_entry.pack_forget()
        self.email_label.pack_forget()
        self.email_entry.pack_forget()
        self.password_label.pack_forget()
        self.password_entry.pack_forget()
        self.typeUser_label.pack_forget()
        self.typeUser_entry.pack_forget()
        self.register_user_button.pack_forget()

        # Change the label text to "Iniciar sesión"
        self.label.config(text="Iniciar sesión")
        
        # Create a button with the text "Iniciar sesión" and a command to call the start_session method, then pack it into the master window
        self.login_button = tk.Button(self.master, text="Iniciar sesión", command=self.start_session)
        self.login_button.pack()

        # Create a button with the text "Salir" and a command to quit the master window, then pack it into the master window
        self.quit_button = tk.Button(self.master, text="Salir", command=self.master.quit)
        self.quit_button.pack()

    def start_session(self):
        """
        Initializes the login screen.
        """

        # Change the label text to "Iniciar sesión"
        self.label.config(text="Iniciar sesión")

        # Remove the "Iniciar sesión" and "Salir" buttons from the master window
        self.login_button.pack_forget()
        self.quit_button.pack_forget()

        # Create a label with the text "Nombre de usuario:" and pack it into the master window
        self.email_label = tk.Label(self.master, text="Email:")
        self.email_label.pack()

        # Create an entry field for the username and pack it into the master window
        self.email_entry = tk.Entry(self.master)
        self.email_entry.pack()

        # Create a label with the text "Contraseña:" and pack it into the master window
        self.password_label = tk.Label(self.master, text="Contraseña:")
        self.password_label.pack()

        # Create an entry field for the password and pack it into the master window
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        # Create a button with the text "Iniciar sesión" and a command to call the login method, then pack it into the master window
        self.login_button = tk.Button(self.master, text="Iniciar sesión", command=self.login)
        self.login_button.pack()

    def login(self):
        """
        Validates the user's login credentials.
        """

        # Get the username and password from the entry fields
        email= self.email_entry.get()
        password = self.password_entry.get()

        # If the user's credentials are valid, change the label text to "Bienvenido"
        if self.userManager.validateUser(email, password):
            self.label.config(text="Bienvenido")
        # Otherwise, change the label text to "Nombre de usuario o contraseña incorrectos"
        else:
            self.label.config(text="Nombre de usuario o contraseña incorrectos")
        
    def modify(self):
        """
        Initializes the modification screen.
        """
        pass

   
# Create the root window for the GUI
root = tk.Tk()

# Create a HotelGUI object with the root window as its master, then run the main loop for the GUI
gui = HotelGUI(root)
root.mainloop()
