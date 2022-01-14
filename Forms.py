from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
import hashlib
#from wtforms.fields.html5 import EmailField, DateField
from wtforms import EmailField, DateField

# class CreateUserForm(Form):    #CreateUserForm inherits from class Form
#     first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
#     last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
#     gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
#     membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
#     remarks = TextAreaField('Remarks', [validators.Optional()])
#
# class CreateCustomerForm(Form):
#     first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
#     last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
#     gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
#     email = EmailField('Email', [validators.Email(), validators.DataRequired()])
#     date_joined = DateField('Date Joined', format='%Y-%m-%d')
#     address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
#     membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
#     remarks = TextAreaField('Remarks', [validators.Optional()])
class CreateCustomerForm(Form):
      first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
      last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
      mobile_no = StringField('Mobile Number', [validators.Length(min=1, max=150), validators.DataRequired()])#unsolved
      address = TextAreaField('Address', [validators.length(max=200), validators.DataRequired()])
      username = StringField('Username', [validators.Length(min=1, max=15), validators.DataRequired()])
      # password = hashlib.md5('Password')
      password= StringField('Password', [validators.Length(min=1, max=15), validators.DataRequired()])

class LoginCustomerForm(Form):

      username = StringField('Username', [validators.Length(min=1, max=15), validators.DataRequired()])
      # password = hashlib.md5('Password')
      password= StringField('Password', [validators.Length(min=1, max=15), validators.DataRequired()])

class LoginStaffForm(Form):

      username = StringField('Username', [validators.Length(min=1, max=15), validators.DataRequired()])
      # password = hashlib.md5('Password')
      password= StringField('Password', [validators.Length(min=1, max=15), validators.DataRequired()])

class CreateStaffForm(Form):
      staff_id = StringField('Staff ID', [validators.Length(min=1, max=150), validators.DataRequired()])
      username = StringField('Username', [validators.Length(min=1, max=15), validators.DataRequired()])
      # password = hashlib.md5('Password')
      password= StringField('Password', [validators.Length(min=1, max=15), validators.DataRequired()])

class CreateCartForm(Form):     # CreateUserForm inherits from class form
    product_name = StringField('Product Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.Optional()])
    quantity = SelectField('Quantity', [validators.DataRequired()],choices=[('1'), ('2'), ('3'), ('4'), ('5')], default='1')
    sugar_lvl = RadioField('Sugar Level', choices=[('0%'), ('25%'), ('50%'), ('75%'), ('100%')], default='25%')

class CreateOrderForm(Form):
    name = StringField('Name on card', [validators.Length(min=1, max=150), validators.DataRequired()])
    card_number = StringField('Card Number', [validators.Length(min=1, max=150), validators.DataRequired()])
    expiry_date = DateField('Expiry Date', format='%Y-%m-%d') #%m-%y
    cvv = StringField('CVV', [validators.Length(min=3, max=3), validators.DataRequired()])
    address = TextAreaField('Change Address', [validators.length(max=200), validators.DataRequired()])
