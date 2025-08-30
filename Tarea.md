# Tarea docker compose

Esta aplicación utiliza el mismo stack tecnológico que el Movie Shop, con la diferencia de que en lugar de usar un archivo local como persistencia de datos, utiliza una base de datos PostgreSQL.

Para lograr ejecutarla, deberán no sólo escribir el archivo Dockerfile para la API de Gameshelf, sino también escribir el archivo docker-compose-yml para que orqueste la ejecución de los dos contenedores (API y DB) y Gameshelf ejecute sin problemas.

Espero dudas, comentarios y porque no, propuestas de mejora en el Teams.

## Bonus tip
Pueden ejecutar el docker-compose.yml usando el siguiente comando:

    docker compose up --build

Si utilizan --build en el comando, docker compose primero buscará referencias a alguna instrucción de build (por ejemplo un Dockerfile) entre los "services" que hayan definido e intentará construir una imagen a partir de esa referencia, siempre y cuando dicha imagen no existe localmente, o exista pero sea más vieja que el cambio en la instrucción del archivo docker-compose.

De esta forma, si hacen bien el docker-compose-yml, se ahorran hacer un docker build cada vez que cambian la imagen.