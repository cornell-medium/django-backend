# Medium Design Collective
The _Django_ powered web platform for Medium, a student design organization based at Cornell University. 

## Setting up the Development Environment

### Prerequisites
* Python 2.7.x (you can check this with `python --version`)
* pip (it is recommended to use the `get-pip.py` script, which can be found [here](https://pip.pypa.io/en/stable/installing/))
* virtualenv (this can be setup using pip, `pip install virtualenv`)
* Ruby (should be preinstalled on Macs, you can check this with `ruby -v`)
* Gem, the Ruby package manager (should also be preinstalled on Macs, you can check this with `gem -v`)

### Setting up Django

1. Clone this repo by executing:

`git clone https://github.com/cornell-medium/django-backend`

2. Setup the `static` submodule, which connects this repo to the [frontend repo](https://github.com/cornell-medium/medium-frontend). All HTML documents, stylesheets, and client-side scripts are managed in the frontend repo. You can setup the submodule with:

`git submodule update --init --recursive`

3. Navigate into the backend directory:

`cd django-backend`

4. Setup a virtual environment for the project by running:

`virtualenv venv`

5. Now go ahead and activate the virtual environment:

`source venv/bin/activate`

6. With the virtual enviornment setup and activated, install the project dependencies:

`pip install -r requirements.txt`

7. Add the Django secret key to the project - you'll have to talk to somebody who already has it setup. Put the secret key in the file `secret.py` in the root of the project.

8. Run the database migrations:

`python manage.py migrate --run-syncdb`

### Setting up frontend development

1. Install the Sass processor:

`gem install sass`

(if this command gives you trouble, try running it as sudo: `sudo gem install sass`)

### Developing the projet

1. Launch the development server with:

`python manage.py runserver`

This should start a server at the url `http://localhost:8000`

2. Open a seperate terminal tab, navigate into the static directory, then run:

`sass --watch scss:css`

3. Code away!