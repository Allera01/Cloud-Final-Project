# Cloud-Final-Project

## 1.Description of the problem.
El objetivo principal del programa es analizar un conjunto de datos de reseñas de libros de Amazon. Utilizando herramientas de Big Data en Google Cloud Platform, se busca extraer la siguiente información de cada libro:
-El promedio de puntuaciones.
-El número total de reseñas.
-La proporción de votos útiles en cada reseña.
Este análisis proporcionará datos clave sobre la calidad de los libros y la percepción de los usuarios.

## 2.Necesidad de Big Data y Cloud
El conjunto de datos contiene millones de registros, lo que hace que su análisis y procesamiento sea prácticamente inviable en local o con recursos limitados. Usar herramientas de Big Data como Spark y Google Cloud Dataproc nos permite procesar esta cantidad de datos eficientemente, escalando recursos según las necesidades.Trabajar en la nube tiene la ventaja de acceso flexible a recursos y una alta disponibilidad para procesar grandes cantidades de datos.

## 3.Descripción de los datos

Usamos este dataset: https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews. 
Estos datos han sido adquiridos mediante el filtro de un dataset general de reseñas y metadatos de productos de Amazon.

Formato: Los datos están en formato .csv para facilitar el análisis.
Tamaño: El archivo tiene un peso aproximado de 2.7 GB y contiene los siguientes campos:

  -id: Identificador del libro.
  -Title: Título del libro.
  -price: Precio del libro.
  -user_id: Identificador del usuario que hizo la reseña.
  -profileName: Nombre del usuario.
  -helpfulness: Relación votos útiles/votos totales.
  -score: Puntuación otorgada al libro.
  -time: Marca temporal de la reseña.
  -summary: Resumen de la reseña.
  -text: Texto completo de la reseña.

## 4.Descripción de la aplicación, modelos de programación, plataforma e infraestructura
La aplicación se ha desarrollado en PySpark, un framework de procesamiento basado en Apache Spark, que permite trabajar con grandes volúmenes de datos de forma eficiente.

Infraestructura:
  Plataforma Cloud: Google Cloud Platform (GCP).
  Servicio: Dataproc, un servicio gestionado de clústeres de Spark y Hadoop.
  Almacenamiento: Google Cloud Storage, utilizado para almacenar el dataset de entrada y los resultados del análisis.

## 5.Diseño del software
Arquitectura:
  Input: Archivo CSV cargado en un bucket de Google Cloud Storage.
  Procesamiento: El script PySpark procesa los datos en un cluster de Dataproc, calculando:
      -Promedio de puntuaciones por libro.
      -Total de reseñas por libro.
      -Proporción promedio de votos útiles por libro (como porcentaje).
  Output: Resultados exportados en formato CSV al bucket.

Dependencias principales:
  PySpark.
  Google Cloud SDK.
  Acceso al dataset a través de Google Cloud Storage.

## 6.Uso
El uso es simple, consta de los siguientes pasos:
  1.primero hay que crear el cluster que queramos usar para la ejecucion:
  
![cluster creado](https://github.com/user-attachments/assets/25bf4370-03b7-4791-86c2-edcb2e82ddaa)

 2.Despues se guarda el csv mencionado antes a un bucket y se sube el archivo analisis.py a la cloud shell. una vez hecho ejecutamos los comandos: 

(hay que cambiar "psyched-canto-436812-e8" por el bucket que hayas creado tu)
~~~
BUCKET=gs://psyched-canto-436812-e8 
~~~
(hay que cambiar "mycluster" por el nombre de tu cluster)
~~~
gcloud dataproc jobs submit pyspark --cluster mycluster --region=europe-southwest1 analisis.py -- $BUCKET/Books_rating.csv $BUCKET/salidaLibros
~~~
![ejecucion1](https://github.com/user-attachments/assets/c7a3e0e8-83f9-47db-a783-b6c7def01ef8)

![ejecucion2](https://github.com/user-attachments/assets/0df2b6c4-2f1f-46c1-9f53-1f2498920cab)

  3.Una vez ejecutado se creara en el bucket una carpeta llamada "salidaLibros" donde podremos encontrar el resultado de nuestra ejecución

## 7 Evaluación de rendimiento
Se realizaron pruebas con diferentes configuraciones de clústeres para evaluar el rendimiento:
  a. 2 nodos, 2 cCPUs
  b. 3 nodos, 4 cCPUs
  c. 4 nodos, 8 cCPUs
Y se obtuvieron los siguientes resultados:
  a. 6 minutos. Cluster pequeño, mucho tiempo de procesamiento
  b. 3 minutos. Mejor rendimiento.
  c. 1 minutos. Estable y escalado efectivo.

Overheads:
  Tiempo de arranque del cluster: ~2 minutos.
  Latencia en lectura/escritura de Google Cloud Storage.

## 8.Características avanzadas
Han sido utilizadas tecnicas y herramientas vistas en clase para el desarrollo de la práctica.

## 9.Conclusiones
Objetivos alcanzados:
  Se ha conseguido el procesamiento exitoso de 2.7 GB de datos, permitiendo el análisis útil de las reseñas de libros integrando efectivamente herramientas de la nube.

Lecciones aprendidas:
  La configuración inicial de clústeres requiere tiempo y pruebas para optimizar el rendimiento del programa, además la distribución de datos impacta considerablemente el rendimiento.

Trabajos futuros:
A futuro sería posible gregar más análisis sobre los datos, como análisis de sentimiento en las reseñas o palabras más utilizadas para describir cada libro en las reseñas. También podrían incorporarse formas de visualizar mejor los datos.

## 10.References.
  Google Cloud Dataproc Documentation: https://cloud.google.com/dataproc/docs
  Dataset: Amazon Book Reviews - https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews
