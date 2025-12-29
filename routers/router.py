'''coderadi &bull; Routes file of the Project.'''

# ? IMPORTING LIBRARIES
from flask import Blueprint, render_template, redirect, url_for, flash, request
from plugins import *

# ! INITIALIZING ROUTER
router = Blueprint('router', __name__)

# & LANDING ROUTE
@router.route('/')
def home():
    return render_template('pages/home.html')

# & PROJECTS ROUTE
@router.route('/achievements/')
def projects():
    projects = Project.query.all()
    count = Project.query.count()

    return render_template('pages/achievements.html', data={
        'achievements': projects,
        'count': count
    })

# | SPECIFIC PROJECT ROUTE
@router.route('/projects/<project_url>')
def project(project_url):
    return render_template(f'pages/{project_url}.html')

# & ABOUT ROUTE
@router.route('/about/')
def about():
    count = Project.query.count()
    return render_template('pages/about.html', data={
        'count': count
    })

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
        route = request.headers.get('Referer', '/contact/')

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
        flash("Your message has been sent successfully!", "check_circle")
        
        notify(f"""Someone has filled the contact form at your `portfolio site`.
Name: {name}
Email: {email}
Subject: {subject}
Message:
{message}

    - coderadi.in""")
        
        return redirect(route)