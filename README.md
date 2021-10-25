#catalogService

## Disclaimer
    este proyecto se realizo en un fin de semana, por lo que hay cosas que faltan que 
    no se alcanzaron a hacer 

##Usar con venv
    python3.6 -m venv env
    python -m venv myenv

## Ejecutar test unitarios
     pytest tests

##Levantar localmente

    python db.py
    python run.py


## REST 

### Auth Basico
 

para usar basic auth seguir este [tutorial](https://dev.to/lucasg/how-to-use-basic-authentication-with-curl-1j6j)
 , al levantar la app se crea el usuario admin:admin

### Crear producto
    curl --request POST \
      --url http://localhost:5000/ \
      --header 'Authorization: Basic YWRtaW46YWRtaW4=' \
      --header 'Content-Type: application/json' \
      --data '{
        "name":"felipe2",
        "sku":"sku",
        "price":23.0,
        "brand":"brand"
    }'


### Listar productos
    curl --request GET \
      --url http://localhost:5000/ \
      --header 'Content-Type: application/json'

### Editar producto
    curl --request POST \
      --url http://localhost:5000/1 \
      --header 'Authorization: Basic YWRtaW46YWRtaW4=' \
      --header 'Content-Type: application/json' \
      --data '{
        "name":"felipe4",
        "sku":"sku",
        "price":23.0,
        "brand":"brand"
    }'
### Eliminar producto
        curl --request DELETE \
      --url http://localhost:5000/3

## Usar docker
    docker build -t app .
    docker run -p 5000:5000 app






##TODO

    - Conectar a una base de datos MySQL o Postgres
    - Agregar test de integracion
    - cubrir casos bordes con test unitarios
    - manejo de excepciones
    - roles de usuario
    - registro de usuario
    - ci/cd?




