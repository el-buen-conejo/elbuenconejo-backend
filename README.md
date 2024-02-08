### Download Python

Go to [python.org/downloads](https://www.python.org/downloads/)

### Install

Don't forget to check ✅ `Add python.exe to PATH`
![python installer](https://res.cloudinary.com/dzc8agefr/image/upload/v1696907584/1_efwa83.png)



![python installer](https://res.cloudinary.com/dzc8agefr/image/upload/v1696907584/2_vtuyh3.png)


### Create and activate a virtual environment

1. Move to **backen** folder
`cd ../backend`
2. Create virtual environment
`python3 -m venv env`
3. Activate virtual environment
  Mac: `source ./env/bin/activate`
  Windows: `.\env\Script\activate`
4. Install all the dependencies 
`pip install -r requirements.txt`



## API



### Profiles Schema

|**KEY**|**TYPE**|**REQUIRED**|
|-|-|-|
|`id`|string|not|
|`is_producer`|bool|not|
|`first_name`|string|not|
|`last_name`|string|not|
|`photo`|string|not|
|`address`|string|not|
|`qualification`|float|not|
|`is_active`|bool|not|
|`created`|timestamp|not|
|`opdated`|timestamp|not|
|`user_id_id`|timestamp|yes|

### Users Schema

|**KEY**|**TYPE**|**REQUIRED**|
|-|-|-|
|`id`|string|not|
|`user_name`|string|yes|
|`email`|string|yes|
|`password`|string|yes, unique|
|`is_superuser`|bool|not|
|`is_staff`|bool|not|
|`is_active`|bool|not|

### Farms Schema

|**KEY**|**TYPE**|**REQUIRED**|
|-|-|-|
|`id`|string|not|
|`name`|string|yes|
|`address`|string|yes|
|`is_active`|bool|not|
|`created`|timestamp|not|
|`updated`|timestamp|not|

### Cages Schema

|**KEY**|**TYPE**|**REQUIRED**|
|-|-|-|
|`id`|string|not|
|`photo`|string|not|
|`count_rabbits`|int|yes|
|`price`|float|yes|
|`is_public`|bool|not|
|`is_active`|bool|not|
|`farm_id_id`|string|yes|
|`created`|timestamp|not|
|`updated`|timestamp|not|

### Rabbits Schema

|**KEY**|**TYPE**|**REQUIRED**|
|-|-|-|
|`id`|string|not|
|`photo`|string|not|
|`breed`|enum|yes|
|`genre`|enum|yes|
|`price`|float|yes|
|`tag`|string|yes, unique|
|`weight`|float|yes|
|`is_active`|float|yes|
|`created`|timestamp|not|
|`updated`|timestamp|not|
|`cage_id_id`|string|yes|



**Enums**
- breed: ['Azteca', 'Cabeza de León', 'California','Chinchilla', 'Gigante de Flandes', 'Mariposa', 'Nueva Zelanda', 'Rex', 'Otro']
- genre: ['Macho', 'Hembra']
