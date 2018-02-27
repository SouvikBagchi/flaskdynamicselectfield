#IMPORT APP 
from flask_app import app, db

from flask import render_template, flash, redirect, url_for, session, request

#IMPORT THE FORM
from forms import SelectionNameForm

#IMPORT THE MODEL FOR QUERY
from models import SelectTable

@app.route('/',methods = ['GET','POST'])
def index():
    
    #INITIALIZE THE FORM
    form = SelectNameForm()
    
    #CHECK WHICH IF GET
    if request.method == 'GET':
        
        #POPULATE THE LIST DYNAMICALLY FROM THE BACKEND
        form.names.choices = [(item,item) for item in db.session.query(SelectTable.name)]
        
    else :
        
        #GET THE VALUE FROM THE FORM FIELD
        name_selected = form.names.data
        
        return ("The name selected is %s")%(str(name_seleted))
        
    
    return render_template('index.html', form = form)
        