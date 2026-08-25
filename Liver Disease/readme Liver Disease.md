En este archivo documentaremos los cambios realizados en los conjuntos de datos de Liver Disease.

# Liver1 fedesoriano cirrhosis-prediction-dataset
    Cargamos las librerias
    Descargamos la base de datos
    Asignamos nombre para trabajar con mi base de datos, en este caso, Liver1
    Vemos el tamanio con .shape en este caso (418, 20)
    Vemos valores faltantes con .isnull().sum()
    Vemos el total de datos faltantes con ,snull().sum().sum()
    Cargamos la informacion de las columnas con .info() ahi vemos datos faltantes y el tipo de variable
    En esta caso trabajamos  con datos faltantes por cada variable, vemos que tipo de vairiable tiene cada columna para decidir que metodo usar para remplazar o agregar una nueva columna y dejarlo como dato faltante.
    Convertimos las variables object a Int64
    Las variables faltantes las remplazamos por 2, aqui aun no aplicamos one-hot encoding
    continuamos este proceso con las siguientes variables, las variables que solo tienen 2 valores como datos, las cambiamos a 1 y 0
    En el caso de la variable Cholesterol, agregamos los valores nulos con la mediana
    Verificamos que todos los valores se ayan normalizado y tener todos los valores con int64
    vemos si hay duplicados con .drop_duplicates(inplace=True)
    Vemos una descripcion con .describe()
    Le pedimos a la ia que nos creara una descripcion de cada columna
    Guardamos el dataset como Liver1_prossed.csv

# Liver2 dataset 878 cirrhosis+patient+survival+prediction+dataset-1
    Cargamos las librerias
    Descargamos la base de datos y le asignamos el nombre de Liver2
    Vemos el tamanio del dataset en este caso es (418, 18)
    Vemos si hay datos faltantes
    Vemos informacion de las variables con .info()
    Comenzamos a trabajar con las variables que tienen datos faltantes, en este caso aplicamos one-hot encoding
    Para algunas variables se tomaron decisiones si trabajar con media, mediana o moda, en algunos casos no convenia usar ninguna, en estos casos se dejaron como valores nulos
    Se siguio valorando con que metodo llenar los datos faltantes o dejarlos como nulos para las demas variables
    Le pedimos a la ia que nos cargara una descripcion para cada columna y nos creara una tabla
    Guardamos el dataset como Liver2_prossed_data.csv

# Liver3 dataset sunilsah905 non-alcoholic fatty liver disease

    Cargamos las librerias
    Descargamos la base de datos y le asignamos el nombre de Liver3
    Revisamos informacion general con .info()
    Vemos el tamanio de la base de datos en este caso es de (605, 50)
    Vemos datos faltantes 
    En este caso no hay datos faltantes
    Verificamos si existen duplicados
    vemos informacion general con .info()
    Le pedimos a la ia que nos creara una descripcion de cada columna
    Descargamos nuestro dataset y lo guardamos como Liver3_final.csv

# Liver4 dataset 60 liver+disorder

    Cargamos las librerias
    Descargamos el dataset y le asignamos el nombre de Liver4
    Revisamos la informacion general
    Vemos el tamanio de la base de datos en este caso (345, 6)
    Vemos si hay duplicados
    Eliminamos duplicados
    Vemos una descripcion general con .describe()
    Le pedimos a la ia que nos creara una descripcion de las variables
    Descargamos nuestro dataset y lo guardamos como Liver4_prossed.csv

# Liver5 dataset 423 hcc+survival

    # En este caso, tuve complicaciones para descargar este dataset


