# Cloud-Final-Project

## 1.Description of the problem.
El objetivo principal del programa es analizar un conjunto de datos de reseñas de libros de Amazon. Utilizando herramientas de Big Data en Google Cloud Platform, se busca extraer la siguiente información de cada libro:<br/>
- El promedio de puntuaciones.<br/>
- El número total de reseñas.<br/>
- La proporción de votos útiles en cada reseña.<br/>

Este análisis proporcionará datos clave sobre la calidad de los libros y la percepción de los usuarios.

## 2.Necesidad de Big Data y Cloud
El conjunto de datos contiene millones de registros, lo que hace que su análisis y procesamiento sea prácticamente inviable en local o con recursos limitados. Usar herramientas de Big Data como Spark y Google Cloud Dataproc nos permite procesar esta cantidad de datos eficientemente, escalando recursos según las necesidades.Trabajar en la nube tiene la ventaja de acceso flexible a recursos y una alta disponibilidad para procesar grandes cantidades de datos.

## 3.Descripción de los datos

Usamos este dataset: https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews. <br/>
Estos datos han sido adquiridos mediante el filtro de un dataset general de reseñas y metadatos de productos de Amazon.<br/>

**Formato:** Los datos están en formato .csv para facilitar el análisis.<br/>
**Tamaño:** El archivo tiene un peso aproximado de 2.7 GB y contiene los siguientes campos:<br/>

  >-id: Identificador del libro.<br/>
  -Title: Título del libro.<br/>
  -price: Precio del libro.<br/>
  -user_id: Identificador del usuario que hizo la reseña.<br/>
  -profileName: Nombre del usuario.<br/>
  -helpfulness: Relación votos útiles/votos totales.<br/>
  -score: Puntuación otorgada al libro.<br/>
  -time: Marca temporal de la reseña.<br/>
  -summary: Resumen de la reseña.<br/>
  -text: Texto completo de la reseña.<br/>

## 4.Descripción de la aplicación, modelos de programación, plataforma e infraestructura
La aplicación se ha desarrollado en PySpark, un framework de procesamiento basado en Apache Spark, que permite trabajar con grandes volúmenes de datos de forma eficiente.<br/>

**Infraestructura:**<br/>
  &nbsp;&nbsp;**Plataforma Cloud:** Google Cloud Platform (GCP).<br/>
  &nbsp;&nbsp;**Servicio:** Dataproc, un servicio gestionado de clústeres de Spark y Hadoop.<br/>
  &nbsp;&nbsp;**Almacenamiento:** Google Cloud Storage, utilizado para almacenar el dataset de entrada y los resultados del análisis.<br/>

## 5.Diseño del software
&nbsp;**Arquitectura:**<br/>
  >**Input:** Archivo CSV cargado en un bucket de Google Cloud Storage.<br/>
  **Procesamiento:** El script PySpark procesa los datos en un cluster de Dataproc, calculando:<br/>
   &nbsp; - Promedio de puntuaciones por libro.<br/>
   &nbsp; - Total de reseñas por libro.<br/>
   &nbsp; - Proporción promedio de votos útiles por libro (como porcentaje).<br/>
  **Output:** Resultados exportados en formato CSV al bucket.<br/>

&nbsp;**Dependencias principales:**<br/>
  - PySpark.<br/>
  - Google Cloud SDK.<br/>
  - Acceso al dataset a través de Google Cloud Storage.<br/>

## 6.Uso
El uso es simple, consta de los siguientes pasos:<br/>
  1.primero hay que crear el cluster que queramos usar para la ejecucion:<br/>
  
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
Se realizaron pruebas con diferentes configuraciones de clústeres para evaluar el rendimiento:<br/>
  &nbsp;&nbsp;a. 2 nodos, 2 cCPUs<br/>
  &nbsp;&nbsp;b. 2 nodos, 4 cCPUs<br/>
  &nbsp;&nbsp;c. 4 nodos, 4 cCPUs<br/>
  
Y se obtuvieron los siguientes resultados:<br/>

  &nbsp;&nbsp;a. 6 minutos. Cluster pequeño, mucho tiempo de procesamiento<br/>
  &nbsp;&nbsp;![image](https://github.com/user-attachments/assets/53e7ebd4-3431-4cde-9883-df47c069d802)<br/>
  &nbsp;&nbsp;![image](https://github.com/user-attachments/assets/5d0094f9-8c7a-4b93-9f79-0c5a233789a3)<br/>
  &nbsp;&nbsp;![image](https://github.com/user-attachments/assets/7d7de81e-d6a6-46e7-8680-4886371118f6)<br/>
  
  &nbsp;&nbsp;b. 3 minutos. Mejor rendimiento.<br/>
  &nbsp;&nbsp;![image](https://github.com/user-attachments/assets/191d67f8-aa59-4ef0-88bb-a4fa7e957cdd)<br/>
  &nbsp;&nbsp;![image](https://github.com/user-attachments/assets/77d1d7e9-ec98-43fc-ab28-1802b0877f25)<br/>
  &nbsp;&nbsp;![image](https://github.com/user-attachments/assets/8050e6e4-cc8e-4b4d-a230-373056b63d98)<br/>
  
  &nbsp;&nbsp;c. 1 minutos. Estable y escalado efectivo.<br/>
  &nbsp;&nbsp;![image](https://github.com/user-attachments/assets/cbb85a24-3090-408e-9040-9c49358b1780)<br/>
  &nbsp;&nbsp;![image](https://github.com/user-attachments/assets/28bc4a0b-e809-46ef-b6d2-c3f65c4237c3)<br/>
  &nbsp;&nbsp;![image](https://github.com/user-attachments/assets/3d0e0c50-65de-4ea0-ab3e-4f5ac7f8258e)<br/>

**Overheads:**<br/>
  - Tiempo de arranque del cluster: ~2 minutos.<br/>
  - Latencia en lectura/escritura de Google Cloud Storage.<br/>

## 8.Características avanzadas
Han sido utilizadas tecnicas y herramientas vistas en clase para el desarrollo de la práctica.

## 9.Conclusiones
&nbsp;**Objetivos alcanzados:**<br/>
- Se ha conseguido el procesamiento exitoso de 2.7 GB de datos, permitiendo el análisis útil de las reseñas de libros integrando efectivamente herramientas de la nube.<br/>

&nbsp;**Lecciones aprendidas:**<br/>
- La configuración inicial de clústeres requiere tiempo y pruebas para optimizar el rendimiento del programa, además la distribución de datos impacta considerablemente el rendimiento.<br/>

&nbsp;Trabajos futuros:<br/>
- A futuro sería posible gregar más análisis sobre los datos, como análisis de sentimiento en las reseñas o palabras más utilizadas para describir cada libro en las reseñas. También podrían incorporarse formas de visualizar mejor los datos.<br/>

## 10.References.
&nbsp;Google Cloud Dataproc Documentation: https://cloud.google.com/dataproc/docs<br/>
&nbsp;Dataset: Amazon Book Reviews - https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews
