from database.dataSource import DataSource
from database.settings import conexion

con = DataSource(
    conexion["host"],
    conexion["user"],
    conexion["passw"],
    conexion["database"],
    conexion["port"],
    conexion["tipo_bd"]
)

# seleccionar usuario o usuarios ********************
def verUsuariosModel(id=""):
    sql = """ 
        SELECT 
            id, 
            name,
            user,
            password 
        FROM 
            usuarios
    """
    # en caso de seleccionar un solo usuario
    if len(id) != 0:
        sql += """
            where id like {0}
        """.format(id)
    
    return con.getData(sql)
    

# Crear usuarios ************************************
def crearUsuariosModel(datos):
 
    sql = """ 
        INSERT INTO usuarios 
            (id, name, user, password) 
        VALUES 
            (NULL, '{0}', '{1}', '{2}');
    """.format(datos[0], datos[1], datos[2])
    return con.query(sql)





# Modificar Usuarios *******************************
def modificarUsuariosModel(datos):
    
    sql = """
        UPDATE usuarios 
        SET 
            name = '{1}', 
            user = '{2}', 
            password = '{3}' 
        WHERE 
            usuario.id = {0};
    """.format(datos[0], datos[1], datos[2], datos[3])
    
    return con.query(sql)

# Borrar usuarios *********************************
def borrarUsuariosModel(id):
    
    sql = """ 
        DELETE FROM usuarios 
        WHERE 
            usuarios.id = {0}
    """.format(id)
    
    return con.query(sql)