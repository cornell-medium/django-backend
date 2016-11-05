# Medium Design Collective
The _Django_ powered web platform for Medium, a student design organization based at Cornell University. 

## Active Tasks

- [ ] Finish design mockups for basic info pages (events, course roster, resources) - _Cindy_
- [ ] Setup the base for the backend, basic website management - _Julian_
- [ ] Put together the backend for serving the course roster - _Sarvar_
- [ ] Get working templates for the front-end going and displaying content - _Harrison and Fawn_
- [ ] Setup the web server and production environment - _Sujay_

## Setting up the Development Environment

1. Install [pip](https://pip.pypa.io/en/stable/)

2. Install [virtualenv](https://virtualenv.pypa.io/en/stable/)
  * _virtualenv_ is a tool for creating isolated Python environments

3. In the base folder of the repo, call `virtualenv env`
  * This creates a virtual environment stored in the _env_ folder, which is already in the _.gitignore_

4. Open up the virtual environment by calling `source env/bin/activate`

5. Install _Django_ by calling `pip install Django`

6. Run the server by calling `python manage.py runserver`
  * The site is now accessible in your browser at [localhost:8000](http://localhost:8000)