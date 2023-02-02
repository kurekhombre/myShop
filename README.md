# myShop
Simple shop using Django MVT builded with Tailwind CSS & HTMX and Stripe payment processing.
## Stack
![Build with](https://skills.thijs.gg/icons?i=python,django,postgres,tailwind,javascript,docker)


## Setup and Run
You need to have installed [Docker](https://www.docker.com/) and [Python](https://www.python.org/).

- Clone or download repo.
```
git clone https://github.com/kurekhombre/myShop
```
- Create virtual environment  `` virtualenv venv`` 
  and activate it
  - Linux/Mac ``` source venv/bin/activate ```
  - Windows ``` venv\Scripts\activate.bat ```

- Generate SECRET KEY with 
  - https://djecrety.ir/ or 
  - ``` python manage.py shell ``` 
   ``` >>> from django.core.management.utils import get_random_secret_key``` 
  ``` print(get_random_secret_key) ```
- Get your STRIPE_API_KEY_PUBLISHABLE and  STRIPE_API_KEY_HIDDEN on the [Stripe website](https://stripe.com/)
- Create a new file '.env' in the project folder and paste 
```
SECRET_KEY='<your_key>'
STRIPE_API_KEY_PUBLISHABLE='<your_key>' 
STRIPE_API_KEY_HIDDEN='<your_key>' 
```

- Up containers with this command:
```
docker-compose up
```
- Go to http://localhost:8000/ and start using the application

## Credentials
Admin credentials:

- username: admin
- password: 1234

User credentials:

- username: exampleuser
- password: ZAQ!@3

Stripe test card:
- 4000 0027 6000 3184

## Demo
<img src="https://i.postimg.cc/2rk5xnNh/front.jpg">
<img src="https://i.postimg.cc/Xv7gsJf9/shop-categories.jpg">
<img src="https://i.postimg.cc/fwGL7FMR/cart.jpg">
<img src="https://i.postimg.cc/Qskt50wj/checkout.jpg">
<img src="https://i.postimg.cc/5yN108L6/stripe.jpg">


## UML diagram
<img src="https://i.postimg.cc/rV7pJHcp/visualed2.png">
<img src="https://i.postimg.cc/rV7pJHcp/visualed2.png">


## [TODO here](https://github.com/kurekhombre/myShop/blob/main/TODO.md)