class AuthControlador:
    user_info = {}

    def __init__(self):
        self.usuarios = {
            "admin": {"password": "admin", "rol": "Admin"},
            "modd": {"password": "modd", "rol": "Editor"},
            "view": {"password": "view", "rol": "Viewer"},
        }

    def autenticar(self, username, password):
        usuario = self.usuarios.get(username)
        if usuario and usuario["password"] == password:
            AuthControlador.user_info = {"nombre_usuario": username, "rol": usuario["rol"]}
            return usuario["rol"] 
        return None

    @staticmethod
    def obtener_rol():
       
        return AuthControlador.user_info.get("rol", None)
