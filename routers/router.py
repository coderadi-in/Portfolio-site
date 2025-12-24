'''coderadi &bull; Routes file of the Project.'''

# ? IMPORTING LIBRARIES
from flask import Blueprint, render_template, redirect, url_for, flash, request
from plugins import *

# ! INITIALIZING ROUTER
router = Blueprint('router', __name__)

# & LANDING ROUTE
@router.route('/')
def index():
    return render_template('pages/index.html')

# & PROJECTS ROUTE
@router.route('/projects/')
def projects():
    projects = Project.query.all()
    count = Project.query.count()

    return render_template('pages/projects.html', data={
        'projects': projects,
        'count': count
    })

# | SPECIFIC PROJECT ROUTE
@router.route('/projects/<project_url>')
def project(project_url):
    return render_template(f'pages/{project_url}.html')

# & ABOUT ROUTE
@router.route('/about/')
def about():
    return render_template('pages/about.html')

# & OFFERS ROUTE
@router.route('/offers/')
def offers():
    offers = Offer.query.all()
    count = Offer.query.count()

    return render_template('pages/offers.html', data={
        'offers': offers,
        'count': count
    })

# & CONTACT ROUTE
@router.route('/contact/', methods=['GET', 'POST'])
def contact():
    if (request.method == 'GET'): 
        return render_template('pages/contact.html')
    
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        new_contact = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        db.session.add(new_contact)
        db.session.commit()
        flash("Your message has been sent successfully!", "success")
        return redirect(url_for('router.contact'))