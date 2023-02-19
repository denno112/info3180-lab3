from app import app
from app import mail
from flask_mail import Message
from flask import render_template, request, redirect, url_for, flash
# Note: that when using Flask-WTF we need to import the Form Class that we created
# in forms.py
from .forms import ContactForm

###
# Routing for your application.
###
@app.route('/contact', methods =['GET','POST'])
def contact():
    contactform = ContactForm()
    if request.method == 'POST':
        if contactform.validate_on_submit():
            # Note the difference when retrieving form data using Flask-WTF
            # Here we use myform.firstname.data instead of request.form['firstname']
            name = contactform.name.data
            email = contactform.email.data
            subject = contactform.subject.data
            message = contactform.message.data

            msg = Message(subject,
                sender=(name,email),
                recipients=["dennismorrison2733@gmail.com"])
            msg.body = message
            mail.send(msg)
            
            flash('Your email has been sucessfully sent')
            return redirect(url_for('home'))
        flash_errors(contactform)
    return render_template('contact.html', form = contactform)

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Dennis Morrison")


###
# The functions below should be applicable to all Flask apps.
###


# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
