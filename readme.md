Install requirements.txt 
　　　run command pip install requirements.txt
Configure the database 
　　　edit database name in settings.py file
Apply migrations 
　　　Run py manage.py makemigrations 
　　　Run py manage.py migrate
Run the server 
　　　Run py manage.py runserver


Testing endpoints 

1) register a user 
endpoint - http://127.0.0.1:8000/pizza/register/
Request - POST request 
request data - {"username":,"password":} 
Response - 	{"user":{"username":},"token":} 
save the token

2) login 
endpoint - http://127.0.0.1:8000/pizza/login/ 
Request - POST request 
request data - {"username":,"password":} 
Response - {"user":{"username":},"token":}

3) logout 
endpoint - http://127.0.0.1:8000/pizza/logout/ 
Request - POST request
Response - {"logout": "User logged out"}

Place the saved token in authorization headers for every request.
Ex - 

4) create square pizza 
endpoint - http://127.0.0.1:8000/pizza/square/ 
Request - POST request 
request data - 	{"size":"small","toppings":["cheese","corn"]} 
Response - {"id": 6,"toppings": [{"name": 	"cheese"},{"name": "corn"}],"created_by": 	{"username": "admin21"},"type": "square","size": 	"small"}


5) create regular pizza 
endpoint - http://127.0.0.1:8000/pizza/regular/ 
Request - POST request 
request data - 	{"size":"small","toppings":["cheese","corn"]}
 Response - {"id": 7,"toppings": [{"name": 	"cheese"},{"name": "corn"}],"created_by": 	{"username": "admin21"},"type": "regular","size": 	"small"}


6) list all pizzas 
endpoint - http://127.0.0.1:8000/pizza/all/ 
Request - GET request
	Response - [{"id": 1,"toppings": [],"created_by": 				{"username": "admin1"},"type": 					"regular","size": 	"medium"},{"id": 				3,"toppings": [{"name": 							"cheese"},{"name": "onion"},{"name": 			"tomato"}],"created_by": {"username": 			"admin1"},"type": "regular","size": 				"small"}]


7) update pizza 
endpoint - 						http://127.0.0.1:8000/pizza/update/##id##/
Ex - http://127.0.0.1:8000/pizza/update/10/ 
Request - PUT request 
request data - 		{"type":"square","size":"small","toppings":["cheese	"]}
 Response - {"id": 1,"toppings": [{"name": 					"cheese"}],"created_by": {"username": 				"admin21"},"type": "square","size": 				"small"}



8) delete pizza
 endpoint - http://127.0.0.1:8000/pizza/update/##id##/ 
Ex - http://127.0.0.1:8000/pizza/update/10/
Request - DELETE request
	Response - {"message": "Deleted"}

9) filter by type 
endpoint - http://127.0.0.1:8000/pizza/filterByType/##value##/ 
Ex - http://127.0.0.1:8000/pizza/filterByType/square/
Request - GET request
	Response - [{"id": 3,"toppings": [{"name": 		"cheese"},{"name": "onion"},{"name": 	"tomato"}],"created_by": {"username": 	"admin1"},"type": "regular","size": "small"}, {"id": 	9,"toppings": [{"name": "cheese"}],"created_by": 	{"username": "admin21"},"type": "regular","size": 	"small"}]




10) filter by size 
endpoint - http://127.0.0.1:8000/pizza/filterBySize/##value##/
Ex - http://127.0.0.1:8000/pizza/filterBySize/small/
Request - GET request
Response - [{"id": 3,"toppings": [{"name": 	"cheese"},{"name": "onion"},{"name": 	"tomato"}],"created_by": {"username": 	"admin1"},"type": "regular","size": "small"}, {"id": 	8,"toppings": [{"name": "cheese"}],"created_by": 	{"username": "admin21"},"type": "square","size": 	"small"},{"id": 9,"toppings": [{"name": 	"cheese"}],"created_by": {"username": 	"admin21"},"type": "regular","size": "small"}]