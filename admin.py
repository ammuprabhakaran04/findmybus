from flask import *
from database import *
admin=Blueprint('admin',__name__)
@admin.route('/adminhome')
def adminhome():
	 return render_template('adminhome.html') 

@admin.route('/adminmanageplaces', methods=['get','post'])
def adminmanageplaces():
	data={}
	if "submit" in request.form:
		place_name=request.form['place_name']
		latitude=request.form['latitude']
		longitude=request.form['longitude']
		q="insert into places values(null,'%s','%s','%s')" %(place_name,latitude,longitude)
		insert(q)
		flash("Added Place Details")
		return redirect(url_for('admin.adminmanageplaces'))
	q="select * from places"
	res=select(q)
	data['places']=res


	if 'action' in request.args:
		action=request.args['action']
		pid=request.args['pid']
	else:
		action=None
	if action=='update':
		q="select * from places where place_id='%s'"%(pid)
		res=select(q)
		data['updates']=res
	if action=='delete':
		q="delete from places where place_id='%s'"%(pid)
		delete(q)
		flash("deleted successfully")
		return redirect(url_for('admin.adminmanageplaces'))

	if 'update' in request.form:
		place_name=request.form['place_name']
		latitude=request.form['latitude']
		longitude=request.form['longitude']		
		q="update places set place_name='%s',latitude='%s',longitude='%s' where place_id='%s'"%(place_name,latitude,longitude,pid)
		update(q)
		flash("updated successfully")
		return redirect(url_for('admin.adminmanageplaces'))




	return render_template('adminmanageplaces.html',data=data)


@admin.route('/adminmanagebuses', methods=['get','post'])
def adminmanagebuses():
	data={}
	if "submit" in request.form:
		bus_name=request.form['bus_name']
		registration_number=request.form['registration_number']
		nos=request.form['nos']
		q="insert into buses values(null,'%s','%s','%s')" %(bus_name,registration_number,nos)
		id=insert(q)
		q="insert into buslocation values(null,'%s','0','0',curdate())" %(id)
		insert(q)
		return redirect(url_for('admin.adminmanagebuses'))
	q="select * from buses"
	res=select(q)
	data['buses']=res

	if 'action' in request.args:
		action=request.args['action']
		pid=request.args['pid']
	else:
		action=None
	if action=='update':
		q="select * from buses where bus_id='%s'"%(pid)
		res=select(q)
		data['updates']=res
	if action=='delete':
		q="delete from buses where bus_id='%s'"%(pid)
		delete(q)
		flash("deleted successfully")
		return redirect(url_for('admin.adminmanagebuses'))

	if 'update' in request.form:
		bus_name=request.form['bus_name']
		registration_number=request.form['registration_number']	
		nos=request.form['nos']

		q="update buses set bus_name='%s',reg_number='%s',noofseats='%s' where bus_id='%s'"%(bus_name,registration_number,nos,pid)
		update(q)
		flash("updated successfully")
		return redirect(url_for('admin.adminmanagebuses'))


	return render_template('adminmanagebuses.html',data=data)

@admin.route('/admintrips',methods=['get','post'])
def admintrips():
	data={}
	id1=request.args['id1']
	data['busid']=id1
	q="select * from buses where bus_id='%s'"%(id1)
	res=select(q)
	data['selbus']=res

	q="select * from routes"
	res=select(q)
	data['root']=res

	if 'submit' in request.form:
		r=request.form['rname']
		s=request.form['stime']
		e=request.form['etime']
		stops=request.form['stops']

		q="insert into trips values(null,'%s','%s','%s','%s','%s')"%(id1,r,s,e,stops)
		tid=insert(q)
		q="select * from routes inner join trips using(route_id) where trip_id='%s'" %(tid)
		res=select(q)
		sp=res[0]['splace_id']
		ep=res[0]['eplace_id']
		st=int(res[0]['stops'])+2
		print(st)
		q1="insert into stops values(null,'%s','%s','1')" %(tid,sp)
		insert(q1)
		q1="insert into stops values(null,'%s','%s','%s')" %(tid,ep,st)
		insert(q1)

		flash("submitted successfully")
		return redirect(url_for('admin.admintrips',id1=id1))

	q="SELECT *,p.`place_name`AS splace,pl.`place_name` AS eplace FROM trips INNER JOIN buses USING(bus_id) INNER JOIN routes r USING(route_id) INNER JOIN places p ON r.`splace_id`=p.`place_id` INNER JOIN places pl ON r.`eplace_id`=pl.`place_id`"
	res=select(q)
	data['viewtrips']=res

	if 'action' in request.args:
		action=request.args['action']
		pid=request.args['pid']
	else:
		action=None
	
	if action=='delete':
		q="delete from trips where trip_id='%s'"%(pid)
		delete(q)
		flash("deleted successfully")
		return redirect(url_for('admin.admintrips',id1=id1))
	return render_template('admintrips.html',data=data)

@admin.route('/admin_manage_stop', methods=['get','post'])
def admin_manage_stop():
	data={}
	tid=request.args['tid']
	bs_id=request.args['bs_id']
	stop=request.args['stop']
	if 'stops' in request.form:
		place=request.form['place']
		stopss=request.form['stopss']
		q1="insert into stops values(null,'%s','%s','%s')" %(tid,place,stopss)
		insert(q1)

		flash("submitted successfully")
		return redirect(url_for('admin.admin_manage_stop',tid=tid,bs_id=bs_id,stop=stop))

	q="select * from stops inner join places using(place_id) inner join trips using(trip_id) where trip_id='%s' and bus_id='%s' order by 	stopnum " %(tid,bs_id)
	res3=select(q)
	data['stopdetail']=res3
	q="select * from places where place_id not in(select place_id from stops where trip_id='%s')" %tid
	res=select(q)
	data['places']=res
	data['stops']=""
	for i in range(1,int(stop)+2):
		q="select * from stops where stopnum='%s' and trip_id='%s'" %(i,tid)
		res1=select(q)
		
		if not res1:
			if data['stops']=="":
				data['stops']=str(i)
			else:
				data['stops']+=str(i)
			print(data['stops'])
	return render_template('admin_manage_stop.html',data=data)

@admin.route('/adminmanageroutes', methods=['get','post'])
def adminmanageroutes():
	data={}
	if "submit" in request.form:
		route_name=request.form['rname']
		starting_id=request.form['sname']
		ending_id=request.form['ename']
		q="insert into routes values(null,'%s','%s','%s')" %(route_name,starting_id,ending_id)
		insert(q)
		return redirect(url_for('admin.adminmanageroutes'))
	q="select * from places"
	res=select(q)
	data['places1']=res
	q="select * from places"
	res=select(q)
	data['places2']=res
	q="SELECT *,p.`place_name` AS splace,pl.`place_name` AS eplace FROM routes r INNER JOIN places p ON r.`splace_id`=p.`place_id` INNER JOIN places pl ON r.`eplace_id`=pl.`place_id` "
	res=select(q)
	print(res)
	data['viewroute']=res



	if 'action' in request.args:
		action=request.args['action']
		pid=request.args['pid']
	else:
		action=None
	if action=='update':
		q="select * from routes where route_id='%s'"%(pid)
		res=select(q)
		print(res)
		data['updates']=res
		q="SELECT place_id='%s' AS sel,place_id,place_name  FROM places ORDER BY sel DESC,place_id ASC" %(res[0]['splace_id'])
		res1=select(q)
		print(res1)
		data['uplaces1']=res1
		q="SELECT place_id='%s' AS sel,place_id,place_name  FROM places ORDER BY sel DESC,place_id ASC" %(res[0]['eplace_id'])
		res2=select(q)
		data['uplaces2']=res2
		
	if action=='delete':
		q="delete from routes where route_id='%s'"%(pid)
		delete(q)
		flash("deleted successfully")
		return redirect(url_for('admin.adminmanageroutes'))

	if 'update' in request.form:
		route_name=request.form['rname']
		starting_id=request.form['sname']
		ending_id=request.form['ename']

		q="update routes set route_name='%s',starting_id='%s',ending_id='%s' where route_id='%s'"%(route_name,starting_id,ending_id,pid)
		update(q)
		flash("updated successfully")
		return redirect(url_for('admin.adminmanageroutes'))



	return render_template('adminmanageroutes.html',data=data)

@admin.route('/adminviewcustomers', methods=['get','post'])
def adminviewcustomers():
	data={}
	q="select * from customer"
	res=select(q)
	data['customers']=res
	return render_template('adminviewcustomers.html',data=data)

@admin.route('/adminmanageotherplaces', methods=['get','post'])
def adminmanageotherplaces():
	data={}
	if 'submit' in request.form:
		pname=request.form['place']
		ot=request.form['placetype']
		lat=request.form['lat']
		longi=request.form['long']

		q="insert into otherplaces values(null,'%s','%s','%s','%s')"%(pname,ot,lat,longi)
		insert(q)

		

		flash("submitted successfully")

	q="SELECT * FROM otherplaces"
	res=select(q)
	data['viewotherplaces']=res


	if 'action' in request.args:
		action=request.args['action']
		pid=request.args['pid']
	else:
		action=None
	if action=='update':
		q="select * from otherplaces where other_place_id='%s'"%(pid)
		res=select(q)
		data['updates']=res
	if action=='delete':
		q="delete from otherplaces where other_place_id='%s'"%(pid)
		delete(q)
		flash("deleted successfully")
		return redirect(url_for('admin.adminmanageotherplaces'))

	if 'update' in request.form:
		pname=request.form['place']
		ot=request.form['placetype']
		lat=request.form['lat']
		longi=request.form['long']

		q="update otherplaces set other_places_name='%s',other_places_type='%s',latitude='%s',longitude='%s' where other_place_id='%s'"%(pname,ot,lat,longi,pid)
		update(q)
		flash("updated successfully")
		return redirect(url_for('admin.adminmanageotherplaces'))


	return render_template('adminmanageotherplaces.html',data=data)

@admin.route('/adminviewcomplaints', methods=['get','post'])
def adminviewcomplaints():
	data={}
	q="select * from complaints inner join customer using(user_id)"
	res=select(q)
	data['complaints']=res

	j=0
	for i in range(1,len(res)+1):
		if 'submit'+str(i) in request.form:
			reply=request.form['reply'+str(i)]
			print(res[j]['complaint_id'])

			q="update complaints set reply='%s' where complaint_id='%s'"%(reply,res[j]['complaint_id'])
			update(q)
			# flash("message send successfully")
			return redirect(url_for('admin.adminviewcomplaints'))
		j=j+1
	return render_template('adminviewcomplaints.html',data=data)