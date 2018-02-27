# flaskdynamicselectfield


This repository demonstrates how to dynamically fetch values from a database and fill it in SelectField in WTForms.

For simplicity I have ignored validators and assumed that the database table (selectTable) contains 
only two columns - id and names 

And upon submit it returns the name of the column that was selected.