#URL's
En cada caso probar en el url primero el '/create' para actualizar la BD y luego usar '/list' para buscar en la BD

##Error en models
Agregue un atributo nuevo a la clase de Mascotas en este caso pero al hacer la migración obtuve este error, lo tuve que dejar como estaba. El error es el siguiente:

'It is impossible to add a non-nullable field 'owner' to mascotas without specifying a default. This is because the database needs something to populate existing rows.'