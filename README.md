#catalogService

## Disclaimer
    No me alcanzo el tiempo suficiente para realizar todos los cambios, 
    ya que me dedique solo el fin de semana

##Usar con venv
    python3.6 -m venv env
    python -m venv myenv
## Ejecutar test unitarios
     pytest tests

##Levantar localmente

    python db.py
    python run.py


## Usar docker
    docker build -t app .
    
    docker run -p 5000:5000 app


##TODO

    - Conectar a una base de datos MySQL o Postgres
    - Agregar test de integracion
    - cubrir casos bordes con test unitarios
    - manejo de excepciones


