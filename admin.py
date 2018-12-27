from flask_admin import Admin
from flask_admin.contrib.pymongo import ModelView
from wtforms import fields, form

class ContactForm(form.Form):
    name_person = fields.StringField()
    phone = fields.StringField()

class ContactView(ModelView):
    form=ContactForm
    column_list = ('name_person','phone',)

def configure(app):
    app.admin = Admin(app, name='Lista Telefônica')
    app.admin.add_view(ContactView(app.db.contact, 'Contatos'))