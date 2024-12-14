# Cloud-Final-Project

## 1.Description of the problem.



## 2.Need for Big Data and Cloud.



## 3.Description of the data (Where does it come from? How was it acquired? What does it mean? What format is it? How big is it? 1 GB minimum). 

Usamos este dataset: https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews. Estos datos han sido adquiridos mediante el filtro de un Amazon review dataset que contenia products review y metadata de Amazon. Los datos esta en formato .csv para facilitarnos el analisis y tiene un peso de 2.7 GB.

## 4.Description of the application, programming model(s), platform and infrastructure.


## 5.Software design (architectural design, code baseline, dependencies…)



## 6.Usage (including screenshots that demonstrate how it works).

Su uso es bastante simple, primero hay que crear el cluster que queramos usar para la ejecucion:

![cluster creado](https://github.com/user-attachments/assets/25bf4370-03b7-4791-86c2-edcb2e82ddaa)

Despues se guarda el csv mencionado antes a un bucket y se sube el archivo analisis.py a la cloud shell. una vez hecho ejecutamos los comandos: 

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

Una vez ejecutado se creara en el bucket una carpeta llamada "salidaLibros" donde podremos encontrar el resultado de nuestra ejecución

## 7.Performance evaluation (speed-up with different number of vCPUs and nodes, identified overheads, optimizations done…).



## 8.Advanced features (tools/models/platforms not explained in class, advanced functions, techniques to mitigate overheads, challenging implementation aspects…).



## 9.Conclusions (goals achieved, improvements suggested, lessons learnt, future work, interesting insights…).



## 10.References.

