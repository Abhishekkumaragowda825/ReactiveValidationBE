Steps to run the Project:



To Run angular FE:

1. Go to "reactiveValidationFE" file folder open Cmd prompt run
	"npm start"




To Run BE:

1. Install python
2. Go to "userDataBE" file folder open cmd prompt run:
	-"pip install pipenv"
	-"pipenv install"
	-"pip install djangorestframework-jsonapi"
	-"pipenv shell"
	-"python manage.py runserver"
3. If you got any errors in BE:
	a. delete "db.sqlite3" file
	b. Run following command
		-"python manage.py makemigrations"
		-"python manage.py migrate"
		-"python manage.py runserver"
	


