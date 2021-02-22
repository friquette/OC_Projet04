# OC_Projet_04
Développez un programme logiciel en Python

## Set up the project
This project runs in python 3

Make a copy of this project on your hard drive <br>
`git clone https://github.com/friquette/OC_Projet_04.git`

Go in the root project and create a virtual environment <br>
`cd OC_Projet_04` <br>
`python -m venv env`

Activate your virtual environment <br>
- On Windows `env\Scripts\activate.bat`
- On Mac OS/Linux `source env/bin/activate`

Install the packages <br>
`pip install -r requirements.txt`

## How to use it
Simply execute the main.py file.</br>
`python ct_manager.py` </br>

The database will be created in the root folder of the project and 
is named database.json. </br>
In the database, the players are saved under the table 'players' and
the tournaments are saved under the table 'tournaments'.

## Generate a flake8 report
Simply enter the following command: </br>
`flake8`

An html file will be created in the flake8_rapport foler. Open the index.html
file in a browser to see the report.