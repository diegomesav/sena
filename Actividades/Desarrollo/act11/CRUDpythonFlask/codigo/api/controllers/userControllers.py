from models.usersModels import *
from flask import jsonify   # libreria que convierte a JSON

# ver usuarios *****************************************
def verUsuariosControllers(id=""):
    
    data = verUsuariosModel(id)
    
    result = []
    
    # creamos estructura para formato JSON
    for row in data:
        content = {
                'id':row[0],
                'name': row[1],
                'user': row[2],
                'password': row[3]
            }
        result.append(content)
        
    return jsonify(result)

# crear usuarios ***************************************
def crearUsuariosController(datos):
    
    result = [True]
    
    # validamos si la operacion se puede realizar
    if crearUsuariosModel(datos):
        result.append("True")
    else:
        result.append("False")
    
    return jsonify(result)










# Modificar usuarios ***************************************
def modificarUsuariosController(datos):
    
    result = []
    
    # validamos si la operacion se puede realizar
    if modificarUsuariosModel(datos):
        result.append("True")
    else:
        result.append("False")
    
    return jsonify(result)

# Borrar Usuario
def borrarUsuarioController(id):
    result = []
    
    # validamos si la operacion se puede realizar
    if borrarUsuariosModel(id):
        result.append("True")
    else:
        result.append("False")
    
    return jsonify(result)
    