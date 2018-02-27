# flaskdynamicselectfield


This repository demonstrates how to dynamically fetch values from a database and fill it in SelectField in WTForms.

For simplicity I have ignored validators and assumed that the database contains one table (selectTable) which contains 
only two columns - id and names 

The settings.py file contains placeholders for the database.

And upon submit it returns the name that was selected.
