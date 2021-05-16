
# drf-ecom-api
> As a django beginer project.
---

## Features


#### Ecom

 * Shop
 * Wallet
---

#### Custom user
* Login
* Registration
---

#### Name of App
* base
* user
* shop
* wallet
---

#### Used Technologies
* Docker
* Python
* Django
* Django-Rest-Framework
* JWT
* PostgreSQL
* Redis
* Postman/Insomnia 

---
## installation

#### Linux
#### Step 1
```
install Docker & Docker-compose
install virtualenv
create env
workon env
git clone https://github.com/anowar143/drf-ecom-api.git
pip install -r requirements.txt
```
---
#### Step 2

```
docker-compose up --build
```
---

#### Step 3

```
docker-compose exec app bash
cd src
./manage.py makemigrations
./manage.py migrate
```



