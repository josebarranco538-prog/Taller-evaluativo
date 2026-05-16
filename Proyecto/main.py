


from Sistema import Sistema
from Producto import Producto
from Carrito import Carrito
from Usuario import Usuario
from MG_Producto import definir_archivo, cargar_productos, guardar_productos
from MG_Usuarios import definir_archivo as definir_archivo_usuarios, crear_archivo_si_no_existe, cargar_usuarios, registrar_usuario, login_usuario


# Gestión de Usuarios
archivo_usuarios = definir_archivo_usuarios()
crear_archivo_si_no_existe(archivo_usuarios)
usuarios = cargar_usuarios(archivo_usuarios)
usuarios = registrar_usuario(archivo_usuarios, usuarios)
usuario_nombre = login_usuario(usuarios)
if usuario_nombre:
    Usuario.usuario_actual = Usuario(usuario_nombre, usuarios[usuario_nombre])

# Cargar Productos desde json
archivo = definir_archivo()
productos_cargados = cargar_productos(archivo)

sistema = Sistema()

# Agregar productos cargados
for producto in productos_cargados:
    sistema.productos().append(producto)

# Si no hay productos, agregar los productos
if not productos_cargados:
    sistema.productos().append(Producto("Hamburguesa clásica", 36000))
    sistema.productos().append(Producto("Papas fritas", 18000))
    sistema.productos().append(Producto("Refresco cola", 10000))
    sistema.productos().append(Producto("Hot dog", 29000))
    
    # Guardar productos en JSON
    guardar_productos(archivo, sistema.productos())

sistema.run()



