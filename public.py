from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
	return render_template('home.html')

@public.route('/login/',methods=['get','post'])
def login():
	if 'submit' in request.form:
		uname=request.form['username']
		passs=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(uname,passs)
		res=select(q);
		print(res)
		if res:
			if res[0]['usertype']=="admin":
				return redirect(url_for('admin.adminhome'))
		else:
			flash("InvalidUsernameorPassword")
				# if res[0]['usertype']=="customer":
				# 	return redirect(url_for('customer.customerhome'))

	return render_template('login.html')
@public.route('/register/',methods=['get','post'])
def register():
	if 'submit' in request.form:
			fname=request.form['first_name']
			lname=request.form['last_name']
			agee=request.form['age']
			genderr=request.form['gender']
			phnno=request.form['phone']
			emailid=request.form['email']
			uname=request.form['username']
			passs=request.form['password']
			q="insert into login values(null,'%s','%s','customer')" %(uname,passs)
			id=insert(q)
			q="insert into customer values(null,'%s','%s','%s','%s','%s','%s','%s')" %(id,fname,lname,agee,genderr,phnno,emailid)
			insert(q)
			return redirect(url_for('public.login'))

	return render_template('register.html')


@public.route('/registerbus', methods=['get','post'])
def registerbus():
	data={}
	if "submit" in request.form:
		bus_name=request.form['bus_name']
		registration_number=request.form['registration_number']
		lnumber=request.form['lnumber']
		nos=request.form['nos']
		fname=request.form['fname']
		lname=request.form['lname']
		age=request.form['age']
		phone=request.form['phone']
		uname=request.form['uname']
		passs=request.form['passs']
		q="insert into buses values(null,'%s','%s','%s')" %(bus_name,registration_number,nos)
		id=insert(q)
		q="insert into login values(null,'%s','%s','conductor')" %(uname,passs)
		lid=insert(q)
		q="insert into conductor values(null,'%s','%s','%s','%s','%s','%s')" %(lid,id,fname,lname,age,phone)
		insert(q)

		q="insert into buslocation values(null,'%s','0','0',curdate())" %(id)
		insert(q)
		return redirect(url_for('public.login'))
	return render_template('registerbus.html',data=data)