from flask import Blueprint,request
from database import *
import demjson
import qrcode
import uuid

api=Blueprint('api',__name__)
@api.route('/login/',methods=['get','post'])
def login():
	data={}
	username=request.args['username']
	password=request.args['password']
	q="select * from login where  username='%s' and password='%s'" %(username,password)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return  demjson.encode(data)

@api.route('/register/',methods=['get','post'])
def register():
	data={}
	
	first_name = request.args['firstname']
	last_name = request.args['lastname']
	gender = request.args['gender']
	age = request.args['age']
	email = request.args['email']
	phone = request.args['contact']
	username = request.args['username']
	password = request.args['password']
	
	q = "insert into login values(null,'%s','%s','customer')" % (username,password)
	login_id = insert(q)
	q = "insert into customer values(null,'%s','%s','%s','%s','%s','%s','%s')" % (login_id,first_name,last_name,age,gender,phone,email)
	print(q)
	insert(q)
	data['status'] = 'success'
	return demjson.encode(data)


@api.route('/location/',methods=['get','post'])
def location():
	data={}
	
	logid = request.args['logid']
	lati = request.args['lat']
	longi = request.args['longi']
	q="select * from buslocation where bus_id=(select bus_id from conductor where log_id='%s')" %(logid)
	res=select(q)
	if res:
		q = "update buslocation set latitude='%s',longitude='%s' where bus_id=(select bus_id from conductor where log_id='%s')" %(lati,longi,logid)
		print(q)
		update(q)
		data['status'] = 'success'
	else:
		data['status']='failed'
	data['method'] = 'location'
	return demjson.encode(data)



@api.route('/viewtrips/',methods=['get','post'])
def viewtrips():
	data={}
	logid=request.args['logid']
	
	q="SELECT trip_id,bus_name,route_name,p1.`place_name` AS splace,p2.`place_name` AS eplace,t.`stime`,t.`etime` FROM trips t,buses b,routes r,places p1,places p2 WHERE t.`bus_id`=b.`bus_id` AND t.`route_id`=r.`route_id` AND r.`splace_id`=p1.`place_id` AND r.`eplace_id`=p2.`place_id` AND t.bus_id=(select bus_id from conductor where log_id='%s')" %(logid)
	
	print(q)
	res=select(q)
	print(res)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="viewtrips"
	return  demjson.encode(data)

@api.route('/viewreservation/',methods=['get','post'])
def viewreservation():
	data={}
	logid=request.args['logid']
	q="SELECT r.`reservation_id`,r.qrcode,r.`no_of_seats`,CONCAT(c.`first_name`,' ',c.`last_name`) AS name,p1.`place_name` AS fplace,p2.`place_name`AS tplace,r.`reservation_amount`,r.`reservation_status` FROM `reservations` r,`customer` c,places p1,places p2,trips t WHERE r.`user_id`=c.`user_id` AND r.`from_place_id`=p1.`place_id` AND r.`to_place_id`=p2.`place_id` AND r.`trip_id`=t.`trip_id` AND t.bus_id=(select bus_id from conductor where log_id='%s')" %(logid)
	res=select(q)
	print(res)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="viewreservation"
	return  demjson.encode(data)


@api.route('/viewreservationb/',methods=['get','post'])
def viewreservationb():
	data={}
	logid=request.args['logid']
	date=request.args['date']
	q="SELECT r.`reservation_id`,r.`no_of_seats`,CONCAT(c.`first_name`,' ',c.`last_name`) AS name,p1.`place_name` AS fplace,p2.`place_name`AS tplace,r.`reservation_amount`,r.`reservation_status` FROM `reservations` r,`customer` c,places p1,places p2,trips t WHERE r.`user_id`=c.`user_id` AND r.`from_place_id`=p1.`place_id` AND r.`to_place_id`=p2.`place_id` AND r.`trip_id`=t.`trip_id` AND t.bus_id=(SELECT bus_id FROM conductor WHERE log_id='%s') AND r.`date`='%s'" %(logid,date)
	res=select(q)
	print(res)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="viewreservation"
	return  demjson.encode(data)


@api.route('/viewnearbystops/',methods=['get','post'])
def viewnearbystops():
	data={}
	lati=request.args['lati']
	longi=request.args['longi']
	
	q="SELECT *,(3959 * ACOS ( COS ( RADIANS('%s') ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS('%s') ) + SIN ( RADIANS('%s') ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM places HAVING user_distance <40 ORDER BY user_distance ASC " %(lati,longi,lati)
	print(q)
	res=select(q)
	print(res)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="viewnearbystops"
	return  demjson.encode(data)


@api.route('/viewcomplaints/',methods=['get','post'])
def viewcomplaints():
	data={}
	logid=request.args['logid']
	
	q="select * from complaints where  user_id=(select user_id from customer where log_id='%s')" %(logid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="viewcomplaints"
	return  demjson.encode(data)


@api.route('/complaints/',methods=['get','post'])
def complaints():
	data={}
	
	complaint = request.args['complaint']
	logid = request.args['logid']
	
	q = "insert into complaints values(null,(select user_id from customer where log_id='%s'),'%s','NA',curdate())" % (logid,complaint)
	insert(q)
	data['status'] = 'success'
	data['method'] = 'complaints'
	return demjson.encode(data)


@api.route('/viewnearbyplaces/',methods=['get','post'])
def viewnearbyplaces():
	data={}
	lati=request.args['lati']
	longi=request.args['longi']
	
	q="SELECT *,(3959 * ACOS ( COS ( RADIANS('%s') ) * COS( RADIANS( latitude) ) * COS( RADIANS( longitude ) - RADIANS('%s') ) + SIN ( RADIANS('%s') ) * SIN( RADIANS( latitude ) ))) AS user_distance FROM otherplaces HAVING user_distance <40 ORDER BY user_distance ASC " %(lati,longi,lati)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="viewnearbyplaces"
	return  demjson.encode(data)



@api.route('/viewspstart/',methods=['get','post'])
def viewspstart():
	data={}
	
	q="select * from places"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="viewspstart"
	return  demjson.encode(data)

@api.route('/viewspend/',methods=['get','post'])
def viewspend():
	data={}
	splace=request.args['splace']
	q="select * from places where place_id !='%s'" %(splace)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="viewspend"
	return  demjson.encode(data)

@api.route('/viewroutes/',methods=['get','post'])
def viewroutes():
	data={}
	splace=request.args['splace']
	eplace=request.args['eplace']
	q="SELECT *,t.trip_id,b.bus_id,b.bus_name,b.reg_number,r.route_name,p1.place_name AS s_name,p2.place_name AS e_name FROM trips t,places p1,places p2,buses b,routes r WHERE t.`bus_id`=b.`bus_id` AND t.`route_id`=r.`route_id` AND r.`splace_id`=p1.`place_id` AND r.`eplace_id`=p2.`place_id` AND  trip_id IN (SELECT trip_id FROM STOPs WHERE place_id='%s') AND trip_id IN (SELECT trip_id FROM STOPs WHERE place_id='%s')" %(splace,eplace)
	print(q)
	res=select(q)
	if res: 
		q="select * from stops where (place_id='%s' and trip_id='%s')" %(splace,res[0]['trip_id'])
		res1=select(q)
		print(res1)
		q="select * from stops where (place_id='%s' and trip_id='%s')" %(eplace,res[0]['trip_id'])
		res2=select(q)
		print(res2)
		if int(res1[0]['stopnum'])<int(res2[0]['stopnum']):
		
			data['status']="success"
			data['data']=res
		else:
			data['status']="failed"
	else:
			data['status']="failed"
	print(data['status'])
	data['method']="viewroutes"
	return  demjson.encode(data)
	# http://127.0.0.1:5010/api/viewroutes/?splace=1&eplace=1


@api.route('/viewseat/',methods=['get','post'])
def viewseat():
	data={}
	bid=request.args['bid']
	tid=request.args['tid']
	date=request.args['date']
	q="SELECT SUM(no_of_seats) as total FROM reservations WHERE trip_id='%s' AND DATE='%s'" %(tid,date)

	res=select(q)
	print(res)
	if res[0]['total']!=None:
		val=int(res[0]['total'])
	else:
		val=0
	print(val)
	
	data['status']="success"
	data['data']=[{"total":val}]

	data['method']="viewseat"
	return  demjson.encode(data)
@api.route('/viewfares/',methods=['get','post'])
def viewfares():
	data={}

	tid=request.args['tid']
	fplace=request.args['fplace']
	tplace=request.args['tplace']
	q="select * from stops where (place_id='%s' and trip_id='%s')" %(fplace,tid)
	res=select(q)
	q="select * from stops where (place_id='%s' and trip_id='%s')" %(tplace,tid)
	res1=select(q)
	if res[0]['stopnum']<res1[0]['stopnum']:
		print("ss")
		diff=int(res1[0]['stopnum'])-int(res[0]['stopnum'])
		print(diff)
		q="select * from rate";
		res9=select(q);
		if diff<=2:
			rates=res9[0]['mincharge'];
		else:
			vals=diff-2;
			rates=int(res9[0]['mincharge'])+(int(res9[0]['stage_charge'])*int(vals));
		data['status']="success"
		data['rate']=rates
	else:
		data['status']="failed"
	data['method']="viewfares"
	return  demjson.encode(data)

@api.route('/addtoreservation/',methods=['get','post'])
def addtoreservation():
	data={}
	
	noofseats = request.args['noofseats']
	lid = request.args['lid']
	tid = request.args['tid']
	fromid = request.args['fromid']
	toid = request.args['toid']
	total = request.args['total']
	date = request.args['date']
	
	q = "insert into reservations values(null,'%s',(SELECT user_id FROM customer WHERE log_id='%s'),'%s','%s','%s','%s','pending','%s','')" % (noofseats,lid,tid,fromid,toid,total,date)
	print(q)
	id=insert(q)
	path = "static/qrcode/" + str(uuid.uuid4()) + ".png"
				
	img = qrcode.make(str(id))
	img.save(path) 
	qw="update reservations set qrcode='%s' where reservation_id='%s'" %(path,id)
	update(qw)
	data['status']='success'
	data['method']="addtoreservation"
	return demjson.encode(data)


@api.route('/viewreservations/',methods=['get','post'])
def viewreservations():
	data={}
	logid=request.args['logid'] 
	
	q="SELECT r.`reservation_id`,r.qrcode,r.`no_of_seats`,p1.`place_name` AS fplace,p2.`place_name`AS tplace,r.`reservation_amount`,r.`reservation_status`,b.`bus_name` FROM `reservations` r,places p1,places p2,trips t,buses b WHERE  r.`from_place_id`=p1.`place_id` AND r.`to_place_id`=p2.`place_id` AND r.`trip_id`=t.`trip_id` AND t.`bus_id`=b.`bus_id` AND r.`user_id`=(SELECT user_id FROM customer WHERE log_id='%s')" %(logid)
	print(q)
	res=select(q)
	print(res)
	if res:
		data['status']="success"
		data['data']=res

	else:
		data['status']="failed"
	data['method']="viewreservations"
	return  demjson.encode(data)

@api.route('/viewreservationsss/',methods=['get','post'])
def viewreservationsss():
	data={}
	rid=request.args['rid']
	
	q="SELECT r.`reservation_id`,r.`no_of_seats`,CONCAT(c.`first_name`,' ',c.`last_name`) AS name,p1.`place_name` AS fplace,p2.`place_name`AS tplace,r.`reservation_amount`,r.`reservation_status` FROM `reservations` r,`customer` c,places p1,places p2,trips t WHERE r.`user_id`=c.`user_id` AND r.`from_place_id`=p1.`place_id` AND r.`to_place_id`=p2.`place_id` AND r.`trip_id`=t.`trip_id` AND r.reservation_id='%s'" %(rid)
	res=select(q)
	print(res)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="viewreservationsss"
	return  demjson.encode(data)


@api.route('/addpay/',methods=['get','post'])
def addpay():
	data={}
	
	rid = request.args['rid']
	amount = request.args['amount']
	
	q = "insert into payment values(null,'%s','%s',curdate())" % (rid,amount)
	# insert(q)
	q="update reservations set reservation_status='Payed' where reservation_id='%s'" %(rid)
	update(q)
	data['status'] = 'success'
	data['method'] = 'addpay'
	return demjson.encode(data)