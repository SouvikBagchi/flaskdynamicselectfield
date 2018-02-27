from flask_wtf import FlaskForm
from wtforms import SelectField

class SelectNameForm(FlaskForm):
    
    #HERE WE ASSUME THAT THE SQL TABLE HAS JUST ONE FIELD NAMES AND WE WILL CREATE A DYNAMIC LIST FETCHING THE DATA FROM THE DATABASE
    
    names = SelectField("Names", coerce = str)
    #NOTICE HOW CHOICES IS NOT MENTIONED ABOVE  