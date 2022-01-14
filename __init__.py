from flask import Flask,render_template,request, redirect, url_for
from Forms import *
import shelve,Customer,Account,Staff, Cart, Order
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    login_customer_form = LoginCustomerForm(request.form)
    if request.method == 'POST' and login_customer_form.validate():
        # db = shelve.open('customer.db', 'c')
        # for i in db:
        #     if db[i].get('username')==login_customer_form.username.data:
        #         if db[i].get("password")==login_customer_form.password.data:
        #             return redirect(url_for("welcome"))
        #             end
            customers_dict = {}
            db = shelve.open('customer.db', 'r')
            customers_dict = db['Customers']
            db.close()
            # global user
            # user= request.form.get('username')
            customers_list = []
            for key in customers_dict:
                customer = customers_dict.get(key)
                customers_list.append(customer)
                db.close()
            for customer in customers_list:
                if customer.get_username()== login_customer_form.username.data:
                    if customer.get_password()== login_customer_form.password.data:
                        return redirect(url_for("welcome"))
            username=login_customer_form.username.data
            # customers_list = []
            # for key in customers_dict:
            #     customer = customers_dict.get(key)
            #     customers_list.append(customer)
            #     db.close()
            # for customer in customers_list:
            #     if customer.get_username()==request.form.get('username'):
            #         if customer.get_username()==request.form.get('password'):
            #             return redirect(url_for("welcome"))
            #             end
            return redirect(url_for("home"))

        # UP_dict = {}
        # UP = shelve.open('up.db', 'c')
        # try:
        #     UP_dict = UP['userpass']
        # except:
        #     print("Error")
        #
        # UP = [login_customer_form.username.data,login_customer_form.password.data]
        # UP_dict[0]=UP
        # UP['userpass']=UP_dict
        # personal=shelve.open(shelve.open('uplist.db', 'c'))
        #
        # for i in personal:
        #     if personal[i]==UP['up']:
        #         return redirect(url_for("welcome"))
        #         end
        # UP.close()
        # personal.close

    return render_template('loginCustomer.html', form=login_customer_form)
    # return render_template('homelogin.html')
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/createCustomer', methods=['GET', 'POST'])
def create_customer():
    create_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and create_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'c')

        try:
            customers_dict = db['Customers']
        except:
            print("Error in retrieving Customers from customer.db.")

        customer = Customer.Customer(create_customer_form.first_name.data, create_customer_form.last_name.data,
                                     create_customer_form.mobile_no.data, create_customer_form.address.data,
                                     create_customer_form.username.data, create_customer_form.password.data,
                                    )

        customers_dict[customer.get_customer_id()] = customer
        db['Customers'] = customers_dict

        db.close()

        return redirect(url_for("home"))
    return render_template('createCustomer.html', form=create_customer_form)

@app.route('/CustomerProfile')
def retrieve_profile():
    customers_dict = {}
    db = shelve.open('customer.db', 'r')
    customers_dict = db['Customers']
    db.close()

    customers_list = []
    for key in customers_dict:
        customer = customers_dict.get(key)
        customers_list.append(customer)
        db.close()
    for customer in customers_list:
        # if customer.get_username()==username:
            return customer
            return render_template('CustomerProfile.html')

#
# @app.route('/contactUs')
# def contact_us():
#     return render_template('contactUs.html')
#
# @app.route('/createUser', methods=['GET', 'POST'])
# def create_user():
#     create_user_form = CreateUserForm(request.form)
#     if request.method == 'POST' and create_user_form.validate():
#         db = shelve.open('user.db', 'c')
#         users_dict = {}
#         try:
#             if 'Users' in db:
#                 users_dict=db['Users']
#             else:
#                 db['Users']=users_dict
#
#             if 'User_Countid' in db:
#                 User.count_id=db['user_Countid']
#             else:
#                 db['User_Countid']=0
#         except:
#                 print("Error in retrieving Users from user.db.")
#         # print(f'create user open db["Users"] len = {len(users_dict)} user_id={User.Count_id}')
#         user = User.User(create_user_form.first_name.data, create_user_form.last_name.data, create_user_form.gender.data, create_user_form.membership.data, create_user_form.remarks.data)
#         users_dict[user.get_user_id()] = user
#         db['Users'] = users_dict
#
#         # Test codes
#         # users_dict = db['Users']
#         # user = users_dict[user.get_user_id()]
#         # print(user.get_first_name(), user.get_last_name(), "was stored in user.db successfully with user_id ==", user.get_user_id())
#
#         db.close()
#
#         return redirect(url_for('retrieve_users'))
#     return render_template('createUser.html', form=create_user_form)
#
# @app.route('/createCustomer', methods=['GET', 'POST'])
# def create_customer():
#     create_customer_form = CreateCustomerForm(request.form)
#     if request.method == 'POST' and create_customer_form.validate():
#         customers_dict = {}
#         db = shelve.open('customer.db', 'c')
#
#         try:
#             customers_dict = db['Customers']
#         except:
#             print("Error in retrieving Customers from customer.db.")
#
#         customer = Customer.Customer(create_customer_form.first_name.data, create_customer_form.last_name.data,
#                                      create_customer_form.gender.data, create_customer_form.membership.data,
#                                      create_customer_form.remarks.data, create_customer_form.email.data,
#                                      create_customer_form.date_joined.data,
#                                      create_customer_form.address.data, )
#         customers_dict[customer.get_customer_id()] = customer
#         db['Customers'] = customers_dict
#
#         db.close()
#
#         return redirect(url_for('home'))
#     return render_template('createCustomer.html', form=create_customer_form)
#
# @app.route('/retrieveUsers')
# def retrieve_users():
#     users_dict = {}
#     db = shelve.open('user.db', 'r')
#     users_dict = db['Users']
#     db.close()
#
#
#     users_list = []
#     for key in users_dict:
#         user = users_dict.get(key)
#         users_list.append(user)
#
#     return render_template('retrieveUsers.html', count=len(users_list), users_list=users_list)
#
@app.route('/retrieveCustomers') #customer list
def retrieve_customers():
    customers_dict = {}
    db = shelve.open('customer.db', 'r')
    customers_dict = db['Customers']
    db.close()

    customers_list = []
    for key in customers_dict:
        customer = customers_dict.get(key)
        customers_list.append(customer)

    return render_template('retrieveCustomers.html', count=len(customers_list), customers_list=customers_list)

#
# @app.route('/updateUser/<int:id>/', methods=['GET', 'POST'])
# def update_user(id):
#     update_user_form = CreateUserForm(request.form)
#     if request.method == 'POST' and update_user_form.validate():
#         users_dict = {}
#         db = shelve.open('user.db', 'w')
#         users_dict = db['Users']
#
#         user = users_dict.get(id)
#         user.set_first_name(update_user_form.first_name.data)
#         user.set_last_name(update_user_form.last_name.data)
#         user.set_gender(update_user_form.gender.data)
#         user.set_membership(update_user_form.membership.data)
#         user.set_remarks(update_user_form.remarks.data)
#
#         db['Users'] = users_dict
#         db.close()
#
#         return redirect(url_for('retrieve_users'))
#     else:
#         users_dict = {}
#         db = shelve.open('user.db', 'r')
#         users_dict = db['Users']
#         db.close()
#
#         user = users_dict.get(id)
#         update_user_form.first_name.data = user.get_first_name()
#         update_user_form.last_name.data = user.get_last_name()
#         update_user_form.gender.data = user.get_gender()
#         update_user_form.membership.data = user.get_membership()
#         update_user_form.remarks.data = user.get_remarks()
#         return render_template('updateUser.html', form=update_user_form)
#
@app.route('/updateCustomer/<int:id>/', methods=['GET', 'POST'])
def update_customer(id):
    update_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and update_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'w')
        customers_dict = db['Customers']

        customer = customers_dict.get(id)
        customer.set_first_name(update_customer_form.first_name.data)
        customer.set_last_name(update_customer_form.last_name.data)
        customer.set_mobile_no(update_customer_form.mobile_no.data)
        customer.set_address(update_customer_form.address.data)
        customer.set_username(update_customer_form.username.data)
        customer.set_password(update_customer_form.password.data)
        db['Customers'] = customers_dict
        db.close()

        return redirect(url_for('retrieve_customers'))
    else:
        customers_dict = {}
        db = shelve.open('customer.db', 'r')
        customers_dict = db['Customers']
        db.close()

        customer = customers_dict.get(id)
        update_customer_form.first_name.data = customer.get_first_name()
        update_customer_form.last_name.data = customer.get_last_name()
        update_customer_form.mobile_no.data = customer.get_mobile_no()
        update_customer_form.address.data = customer.get_address()
        update_customer_form.username.data = customer.get_username()
        update_customer_form.password.data = customer.get_password()

        return render_template('updateCustomer.html', form=update_customer_form)

# @app.route('/deleteUser/<int:id>', methods=['POST'])
# def delete_user(id):
#     users_dict = {}
#     db = shelve.open('user.db', 'w')
#     users_dict = db['Users']
#
#     users_dict.pop(id)
#
#     db['Users'] = users_dict
#     db.close()
#
#     return redirect(url_for('retrieve_users'))
#
@app.route('/deleteCustomer/<int:id>', methods=['POST'])
def delete_customer(id):
    customers_dict = {}
    db = shelve.open('customer.db', 'w')
    customers_dict = db['Customers']

    customers_dict.pop(id)

    db['Customers'] = customers_dict
    db.close()

    return redirect(url_for('retrieve_customers'))

@app.route('/loginStaff', methods=['GET', 'POST'])
def staffLogin():
    login_staff_form = LoginStaffForm(request.form)
    if request.method == 'POST' and login_staff_form.validate():
            staff_dict = {}
            db = shelve.open('staff.db', 'r')
            staff_dict = db['Staffs']
            db.close()

            staff_list = []
            for key in staff_dict:
                staff = staff_dict.get(key)
                staff_list.append(staff)
                db.close()
            for staff in staff_list:
                if staff.get_username()== login_staff_form.username.data:
                    if staff.get_password()== login_staff_form.password.data:
                        return redirect(url_for("backend"))

    return render_template('loginStaff.html', form=login_staff_form)

@app.route('/createStaff', methods=['GET', 'POST'])
def create_staff():
    create_staff_form = CreateStaffForm(request.form)
    if request.method == 'POST' and create_staff_form.validate():
        staff_dict = {}
        db = shelve.open('staff.db', 'c')
        try:
            staff_dict = db['Staffs']
        except:
            print("Error in retrieving Customers from customer.db.")

        staff = Staff.Staff(create_staff_form.staff_id.data,
                            create_staff_form.username.data,
                            create_staff_form.password.data)

        staff_dict[staff.get_staff_count()] = staff
        db['Staffs'] = staff_dict

        db.close()
        return redirect(url_for("backend"))
    return render_template('createStaff.html', form=create_staff_form)

@app.route('/createCart', methods=['GET', 'POST'])
def create_cart():
    create_user_form = CreateCartForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        db = shelve.open('cart.db', 'c')  # creates db if not present
        users_dict = {}
        try:
            if 'Users' in db:             #setup users_dict in db
                users_dict = db['Users']
            else:
                db['Users'] = users_dict

            if 'User_Countid' in db:      # setup User.count_id in db
                Cart.count_id = db['User_Countid']
            else:
                db['User_Countid'] = 0

        except:
            print("Error in retrieving Users from cart.db.")
        print(f'create_user: open db["Users"] len = {len(users_dict)} user_id = {Cart.count_id}')

        user = Cart.Cart(create_user_form.product_name.data, create_user_form.last_name.data,
                         create_user_form.quantity.data, create_user_form.sugar_lvl.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict
        db['User_Countid'] = Cart.count_id

        # Test codes
        #users_dict = db['Users']
        #user = users_dict[user.get_user_id()]
        #print(user.get_first_name(), user.get_last_name(), "was stored in cart.db successfully with user_id ==",
              #user.get_user_id())

        db.close()

        return redirect(url_for('retrieve_cart'))

    return render_template('createCart.html', form=create_user_form)

@app.route('/retrieveCart')
def retrieve_cart():
    users_dict = {}
    db = shelve.open('cart.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('retrieveCart.html', count=len(users_list), users_list=users_list)

@app.route('/updateCart/<int:id>/', methods=['GET', 'POST'])
def update_cart(id):
    update_user_form = CreateCartForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open('cart.db', 'w')
        users_dict = db['Users']

        user = users_dict.get(id)
        user.set_product_name(update_user_form.product_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_quantity(update_user_form.quantity.data)
        user.set_sugar_lvl(update_user_form.sugar_lvl.data)

        db['Users'] = users_dict
        db.close()

        return redirect(url_for('retrieve_cart'))
    else:
        users_dict = {}
        db = shelve.open('cart.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        update_user_form.product_name.data = user.get_product_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.quantity.data = user.get_quantity()
        update_user_form.sugar_lvl.data = user.get_sugar_lvl()
        return render_template('updateCart.html', form=update_user_form)

@app.route('/deleteCart/<int:id>', methods=['POST'])
def delete_cart(id):
    users_dict = {}
    db = shelve.open('cart.db', 'w')
    users_dict = db['Users']

    users_dict.pop(id)

    db['Users'] = users_dict
    db.close()

    return redirect(url_for('retrieve_cart'))

@app.route('/order', methods=['GET', 'POST'])
def create_order():
    create_order_form = CreateOrderForm(request.form)
    if request.method == 'POST' and create_order_form.validate():
        db = shelve.open('order.db', 'c')  # creates db if not present
        orders_dict = {}
        try:
            if 'Orders' in db:             #setup users_dict in db
                orders_dict = db['Orders']
            else:
                db['Orders'] = orders_dict

            #if 'User_Countid' in db:  # setup User.count_id in db
                #User.count_id = db['User_Countid']
            #else:
                #db['User_Countid'] = 0


        except:
            print("Error in retrieving Orders from order.db.")
        #print(f'create_order: open db["Orders"] len = {len(orders_dict)} user_id = {User.count_id} ')

        order = Order.Order(create_order_form.name.data, create_order_form.card_number.data,
                         create_order_form.expiry_date.data, create_order_form.cvv.data, create_order_form.address.data)
        db['Orders'] = orders_dict

        # Test codes
        #orders_dict = db['Orders']
        #order = orders_dict[order.get_order_id()]
        #print(order.get_name(), "was stored in user.db successfully with user_id ==")

        db.close()

        return redirect(url_for('home'))

    return render_template('order.html', form=create_order_form)

@app.route('/backend')
def backend():
    return render_template('backend.html')


if __name__ == '__main__':
    app.run()
