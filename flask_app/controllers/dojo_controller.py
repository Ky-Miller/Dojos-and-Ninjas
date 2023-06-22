from flask import render_template, redirect, request, session, flash
from flask_app import app

from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/dojos')
def home_route():

    all_dojos = Dojo.get_all_dojos()

    print(all_dojos)

    return render_template('dojos.html', all_dojos = all_dojos)

@app.route('/dojos/<int:dojo_id>')
def show(dojo_id):

    one_dojo = Dojo.get_dojo_with_ninjas({ 'dojo_id' : dojo_id })

    return render_template('show_dojo.html', one_dojo = one_dojo)

@app.route('/dojos/submit_new_dojo', methods= ['POST'])
def submit_dojo():

    Dojo.add_dojo(request.form)
    
    return redirect('/dojos')

@app.route('/dojos/create_ninja')
def create_ninja():

    all_dojos = Dojo.get_all_dojos()

    return render_template('ninja_form.html', all_dojos = all_dojos)


#post route for submitting a new user
@app.route('/dojos/submit_new_ninja', methods= ['POST'])
def submit_ninja():

    Ninja.add_ninja(request.form)
    
    return redirect('/dojos')
