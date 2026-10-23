# Aplicación Web Hola Mundo

Esta es una aplicación web sencilla ("Hola Mundo") escrita en Python utilizando el framework Flask. La aplicación se conecta a una base de datos MySQL para verificar la conectividad.

Todo el entorno está contenerizado y orquestado utilizando Docker y Docker Compose.

## Requisitos

* Docker
* Docker Compose

## Cómo ejecutar la aplicación

1. Abre una terminal en la raíz de este proyecto.
2. Ejecuta el siguiente comando para construir y levantar los contenedores en segundo plano:

   ```bash
   docker-compose up -d --build
   ```

3. Espera unos segundos a que la base de datos MySQL se inicialice correctamente.
4. Abre tu navegador web y visita: [http://localhost:5000](http://localhost:5000)

Deberías ver un mensaje de "Hola Mundo" indicando que la conexión a la base de datos fue exitosa.

## Detener la aplicación

Para detener y eliminar los contenedores, puedes ejecutar:

```bash
docker-compose down
```
