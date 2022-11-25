from datetime import datetime

from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.db.models import Max
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .forms import ProfileUpdateForm
from .models import *

def driver_login(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		if Driver.objects.filter(driver_user=username).exists():
			if Driver.objects.filter(driver_user=username,driver_password=password).exists():
				return render(request,"driver_monitor.html",)	
	return render(request,"login_driver.html",)

def login_request(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			messages.success(request, f" Hello {username}, You Are Successfully Logged In")
			current_user = request.user
		
			return render(request,"homepage_monitor.html",{'current_user':current_user})

		else:
			if not User.objects.filter(username=username).exists():
				messages.error(request, "Username Doesn't Exist")
				return render(request,'login.html',{'message1':"Username Doesn't Exist."})
				
			else:
				messages.info(request, "Incorrect Password")
				return render(request,'login.html',{'message2':"Incorrect Password."})
	else:
		return render(request,'login.html')

@login_required
def homepage_monitor(request):
	return render(request,'homepage_monitor.html')


def monitor_detail(request):
	     return render(request,'monitor.html')

def user_detail(request):
	
	return render(request,'table_create.html')

def logout(request):
	try:
		del request.session['username']
	except KeyError:
		pass
	return redirect('/')


# Add management

def add_user(request):
	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		confirm_password = request.POST.get('confirm_password')
		email = request.POST.get('email')
		picture = request.POST.get('picture')
		role = request.POST.get('role')
		fname = request.POST.get('fname')
		lname = request.POST.get('lname')
		id_card = request.POST.get('id_card')
		if User.objects.filter(username=username).exists():
				# messages.info(request,'This username has already been taken!')
				print("This username has already been taken!")
				return render(request,'add_user.html',{'message1':"This username has already been taken"})
		else:
			if password==confirm_password:
				# Create auto ref_no
				if User.objects.count() != 0:
					admin_id_max = User.objects.aggregate(Max('admin_id'))['admin_id__max']
					next_admin_id = admin_id_max[0:2] + str(int(admin_id_max[2:6])+1)
				else:
					next_admin_id = "US1000"
				add_new = User.objects.create_user(admin_id=next_admin_id,
													username=username,
													password=confirm_password,
													email=email,
													profile_user=picture,
													role_user=role,
													first_name=fname,
													last_name=lname,
													id_card=id_card)
				add_new.save()
				return render(request,'create_user.html',{'message2':"Add new user successful."})
	return render(request,'create_user.html')

def add_driver(request):
	if request.method=='POST':
		driver_user = request.POST.get('driver_user')
		password = request.POST.get('password')
		confirm_password = request.POST.get('confirm_password')
		f_name = request.POST.get('f_name')
		l_name = request.POST.get('l_name')
		id_card = request.POST.get('id_card')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		picture_driver = request.POST.get('picture_driver')
		drivinglicense_id = request.POST.get('drivinglicense_id')
		issue_date = request.POST.get('issue_date')
		expire_date = request.POST.get('expire_date')

		if Driver.objects.filter(driver_user=driver_user).exists():
				# messages.info(request,'This username has already been taken!')
				print("This username has already been taken!")
				return render(request,'add_driver.html',{'message1':"This username has already been taken"})
		else:
			if password==confirm_password:
				# Create auto ref_no
				if Driver.objects.count() != 0:
					driver_id_max = Driver.objects.aggregate(Max('driver_id'))['driver_id__max']
					next_driver_id = driver_id_max[0:2] + str(int(driver_id_max[2:6])+1)
				else:
					next_driver_id = "DV1000"
				new_driver = Driver.objects.create(
				driver_id = next_driver_id,
				driver_user = driver_user,
				driver_password = confirm_password,
				driver_fname = f_name,
				driver_lname = l_name,
				driver_email = email,
				drivinglicense_id = drivinglicense_id,
				issue_date = issue_date,
				expire_date = expire_date,
				id_card = id_card,
				driver_phone = phone,
				profile_driver = picture_driver
			)
				new_driver.save()
				return render(request,'add_driver.html',{'message1':"Add driver successful."})
	return render(request,'add_driver.html')
		
		

def add_type(request):
	if request.method=='POST':
		
		t_name = request.POST.get('t_name')
		description = request.POST.get('description')
		


		# Create auto ref_no
		if Type_medicine.objects.count() != 0:
			type_id_max = Type_medicine.objects.aggregate(Max('type_id'))['type_id__max']
			next_type_id = type_id_max[0:2] + str(int(type_id_max[2:6])+1)
		else:
			next_type_id = "TY1000"

		new_type = Type_medicine.objects.create(
			type_id = next_type_id,
			type_name = t_name,
			description = description
		)
		new_type.save()
		return render(request,'add_type.html',{'message1':"Add type successful."})
	return render(request,'add_type.html')

def add_car(request):
	if request.method=='POST':
		
		car_brand = request.POST.get('car_brand')
		license_p = request.POST.get('license_p')
		car_weight = request.POST.get('car_weight')
		temp_max = request.POST.get('temp_max')
		temp_min = request.POST.get('temp_min')
		car_picture = request.POST.get('car_picture')

		if Car.objects.count() != 0:
			car_id_max = Car.objects.aggregate(Max('car_id'))['car_id__max']
			next_car_id = car_id_max[0:3] + str(int(car_id_max[3:7])+1)
		else:
			next_car_id = "CAR1000"

		new_car = Car.objects.create(
				car_id = next_car_id,
				car_band = car_brand,
				total_coolbox_weight = car_weight,
				temp_max = temp_max,
				temp_min = temp_min,
				license_plate = license_p,
				car_picture = car_picture
				
			)

		new_car.save()

		return render(request,'add_car.html',{'message1':"Add car successful."})
	
	return render(request,'add_car.html')
		
		
def add_medicine(request):
	if request.method=='POST':

		m_type = request.POST.get('m_type')
		type_name = Type_medicine.objects.get(type_id=m_type)
		m_name = request.POST.get('m_name')
		totals = request.POST.get('totals')
		measurement = request.POST.get('measurement')
		temp_max = request.POST.get('temp_max')
		temp_min = request.POST.get('temp_min')
		description = request.POST.get('description')

		if Medicine.objects.count() != 0:
			Medicine_id_max = Medicine.objects.aggregate(Max('medicine_id'))['medicine_id__max']
			next_medicine_id = Medicine_id_max[0:2] + str(int(Medicine_id_max[2:6])+1)
		else:
			next_medicine_id = "MC1000"

	

		new_medicine = Medicine.objects.create(
				medicine_id = next_medicine_id,
				medicine_name = m_name,
				medicine_type = type_name,
				medicine_tempmax = temp_max,
				medicine_tempmin = temp_min,
				description = description,
				total = totals,
				t_measurement = measurement
				
			)

		new_medicine.save()
		return render(request,'add_medicine.html',{'message1':"Add medicine successful."})
	
	type_med = Type_medicine.objects.all()
	return render(request,'add_medicine.html',{'type_med':type_med})



def add_coolbox(request):
	if request.method=='POST':
		
		m_medicine = request.POST.get('m_medicine')
		medicine_name = Medicine.objects.get(medicine_id=m_medicine)

		dimention = request.POST.get('dimention')
		totals = request.POST.get('totals')
		t_measurement = request.POST.get('t_measurement')
		d_measurement = request.POST.get('d_measurement')
		weight = request.POST.get('weight')
		temp_max = request.POST.get('temp_max')
		temp_min = request.POST.get('temp_min')
		

		if Coolbox.objects.count() != 0:
			coolbox_id_max = Coolbox.objects.aggregate(Max('coolbox_id'))['coolbox_id__max']
			next_coolbox_id = coolbox_id_max[0:2] + str(int(coolbox_id_max[2:6])+1)
		else:
			next_coolbox_id = "CB1000"

		new_coolbox = Coolbox.objects.create(
				coolbox_id = next_coolbox_id,
				medicine_name = medicine_name,
				weight = weight,
				coolboxtemp_max = temp_max,
				coolboxtemp_min = temp_min,
				dimension = dimention,
				d_measurement = d_measurement,
				t_measurement = t_measurement,
				total = totals,
				status = 'Shipping'
				
			)

		new_coolbox.save()

		return render(request,'add_coolbox.html',{'message1':"Add coolbox successful."})
	med_coolbox = Medicine.objects.all()
	return render(request,'add_coolbox.html',{'med_coolbox':med_coolbox})	

def add_ship(request):
	if request.method=='POST':
		
		m_namedriver = request.POST.get('m_namedriver')
		driver_id = Driver.objects.get(driver_id=m_namedriver)

		m_licensepl = request.POST.get('m_licensepl')
		car_id = Car.objects.get(car_id=m_licensepl)

		m_weightcoolbox = request.POST.getlist('m_weightcoolbox')
		coolbox_id = [i for i in Coolbox.objects.filter(coolbox_id__in=m_weightcoolbox)]
		
		ship_date = request.POST.get('ship_date')
		ship_time = request.POST.get('ship_time')
		original = request.POST.get('original')
		destination = request.POST.get('destination')

		if shipping.objects.count() != 0:
			ship_id_max = shipping.objects.aggregate(Max('shipping_id'))['ship_id__max']
			next_ship_id = ship_id_max[0:2] + str(int(ship_id_max[2:6])+1)
		else:
			next_ship_id = "SP1000"

		new_shipping = shipping.objects.create(
				shipping_id = next_ship_id,
				driver_id = driver_id,
				car_id = car_id,
				ship_date = ship_date,
				ship_time = ship_time,
				original = original,
				destination = destination,
			).save()
		new_shipping.coolbox_id.set(coolbox_id)

		return render(request,'add_ship.html',{'message1':"Add shipping successful."})
	driver_ship = Driver.objects.all()
	car_ship = Car.objects.all()
	coolbox_ship = Coolbox.objects.all()
	return render(request,'add_ship.html',{'driver_ship':driver_ship,'car_ship':car_ship,'coolbox_ship':coolbox_ship})	

	# context = {
	# 	'driver_ship':driver_ship,
	# 	'car_ship':car_ship,
	# 	'coolbox_ship':coolbox_ship
	# }
	# return render(request,'add_ship.html',context)

# table management

def table_car(request):
	car_info = Car.objects.all()
	return render(request,'table_car.html',{'car_info':car_info})

def table_type(request):
	type_info = Type_medicine.objects.all()
	m_type = Medicine.objects.all()
	return render(request,'table_type.html',{'type_info':type_info})

def table_driver(request):
	driver_info = Driver.objects.all()
	return render(request,'table_driver.html',{'driver_info':driver_info})

def table_medicine(request):
	medicine_info = Medicine.objects.all()
	return render(request,'table_medicine.html',{'medicine_info':medicine_info})

def table_shipping(request):
	shipping_info = shipping.objects.all()
	return render(request,'table_shipping.html',{'shipping_info':shipping_info})

def table_coolbox(request):
	coolbox_info = Coolbox.objects.all()
	return render(request,'table_coolbox.html',{'coolbox_info':coolbox_info})

def table_create(request):
	users = User.objects.all()
	return render(request,'table_create.html',{'users':users})



def tracking(request):
	return render(request,'tracking.html')

def track(request):
	return render(request,'track.html')

def moni1(request):
	return render(request,'moni1.html')

def profile_setting(request):
	if request.method == 'POST':
		profile_form = ProfileUpdateForm(request.POST, instance=request.user)
		profile_form.save()
		# if profile_form.is_valid():
		# 	profile_form.save()
		# 	redirect('profile_setting')
	else:
		profile_form = ProfileUpdateForm(instance=request.user)
	# current_user = request.user
	context = {
		# 'current_user':current_user
		'profile_form':profile_form
	}
	return render(request,'profile_setting.html',context)

# def profile_setting(request,pk):
# 	editu = User.objects.get(admin_id=pk)
# 	if request.method == "POST":
# 		username = request.POST.get('username')
# 		email = request.POST.get('email')
# 		idcard = request.POST.get('idcard')
# 		userpic = request.POST.get('userpic')
# 		first_name = request.POST.get('fname')
# 		last_name = request.POST.get('lname')
		

# 		editu.username = username
# 		editu.email = email
# 		editu.id_card = idcard
# 		editu.profile_user = userpic
# 		editu.first_name = first_name
# 		editu.last_name = last_name
# 		editu.save()
# 		# return redirect('edit_car')
# 		return render(request,'profile_setting.html',{'message1':"Edit profile successful."})
# 	return render(request,'profile_setting.html',{'editu':editu})

# View management

def view_user(request,pk):
	usdt = User.objects.get(admin_id=pk)
	
	
	return render(request,'view_user.html',{'usdt':usdt})


def view_car(request,pk):
	crdt = Car.objects.get(car_id=pk)
	
	return render(request,'view_car.html',{'crdt':crdt})


def view_coolbox(request,pk):
	cbdt = Coolbox.objects.get(coolbox_id=pk)
	med_coolbox = Type_medicine.objects.all()	
 	
	

	return render(request,'view_coolbox.html',{'cbdt':cbdt ,'med_coolbox':med_coolbox})

def view_medicine(request,pk):
	mcdt = Medicine.objects.get(medicine_id=pk)
	type_med = Type_medicine.objects.all()

	return render(request,'view_medicine.html',{'mcdt':mcdt,'type_med':type_med})

def view_shipping(request,pk):
	spdt = shipping.objects.get(shipping_id=pk)
	
	return render(request,'view_shipping.html',{'spdt':spdt})

def view_type(request,pk):
	tpdt = Type_medicine.objects.get(type_id=pk)
	
	return render(request,'view_type.html',{'tpdt':tpdt})

def view_driver(request,pk):
	dvdt = Driver.objects.get(driver_id=pk)
	
	return render(request,'view_driver.html',{'dvdt':dvdt})

# Edit management



def edit_user(request,pk):
	editu = User.objects.get(admin_id=pk)
	if request.method == "POST":
		username = request.POST.get('username')
		email = request.POST.get('email')
		idcard = request.POST.get('idcard')
		userpic = request.POST.get('userpic')
		first_name = request.POST.get('fname')
		last_name = request.POST.get('lname')
		

		editu.username = username
		editu.email = email
		editu.id_card = idcard
		editu.profile_user = userpic
		editu.first_name = first_name
		editu.last_name = last_name
		editu.save()
		# return redirect('edit_car')
		return render(request,'edit_user.html',{'message1':"Edit user successful."})
	return render(request,'edit_user.html',{'editu':editu})

def edit_driver(request,pk):
	editd = Driver.objects.get(driver_id=pk)
	if request.method == "POST":
		driver_user = request.POST.get('driver_user')
		email = request.POST.get('email')
		id_card = request.POST.get('id_card')
		profile_driver = request.POST.get('profile_driver')
		driver_fname = request.POST.get('f_name')
		driver_lname = request.POST.get('l_name')
		phone = request.POST.get('phone')
		drivinglicense_id = request.POST.get('drivinglicense_id')
		issue_date = request.POST.get('issue_date')
		expire_date = request.POST.get('expire_date')
		

		editd.driver_user = driver_user
		editd.driver_email = email
		editd.driver_phone = phone
		editd.id_card = id_card
		editd.drivinglicense_id = drivinglicense_id
		editd.issue_date = issue_date
		editd.expire_date = expire_date
		editd.profile_driver = profile_driver
		editd.driver_fname = driver_fname
		editd.driver_lname = driver_lname
		editd.save()
		# return redirect('edit_car')
		return render(request,'edit_driver.html',{'message1':"Edit driver successful."})
	
	return render(request,'edit_driver.html',{'editd':editd})

# def edit_car(request,pk):
# 	car_id = Car.objects.get(car_id=pk)
# 	if request.method == "POST":
# 		car_brand = request.POST.get('car_brand')
# 		license_p = request.POST.get('license_p')
# 		car_weight = request.POST.get('car_weight')
# 		temp_max = request.POST.get('temp_max')
# 		temp_min = request.POST.get('temp_min')
# 		car_picture = request.POST.get('car_picture')
		

# 		update_car = Car.objects.filter(car_id = car_id).update(
# 				car_band = car_brand,
# 				total_coolbox_weight = car_weight,
# 				temp_max = temp_max,
# 				temp_min = temp_min,
# 				license_plate = license_p,
# 				car_picture = car_picture				
# 			)
# 		# return redirect('edit_car')
# 		return render(request,'edit_car.html',{'message1':"Add car successful."})
# 	return render(request,'edit_car.html',{'editc':car_id})

def edit_car(request,pk):
	editc = Car.objects.get(car_id=pk)
	if request.method == "POST":
		car_brand = request.POST.get('car_brand')
		license_p = request.POST.get('license_p')
		car_weight = request.POST.get('car_weight')
		temp_max = request.POST.get('temp_max')
		temp_min = request.POST.get('temp_min')
		car_picture = request.POST.get('car_picture')
		
		

		editc.car_band = car_brand
		editc.license_plate = license_p
		editc.total_coolbox_weight = car_weight
		
		editc.temp_max = temp_max
		editc.temp_min = temp_min
		editc.car_picture = car_picture
		editc.save()
		# return redirect('edit_car')
		return render(request,'edit_car.html',{'message1':"Edit driver successful."})
	
	return render(request,'edit_car.html',{'editc':editc})




def edit_type(request,pk):
	editt = Type_medicine.objects.get(type_id=pk)
	if request.method == "POST":
		type_name = request.POST.get('type_name')
		description = request.POST.get('description')
		
		
		

		editt.type_name = type_name
		editt.description = description
		
		editt.save()
		# return redirect('edit_car')
		return render(request,'edit_type.html',{'message1':"Edit type successful."})
	
	return render(request,'edit_type.html',{'editt':editt})

def edit_medicine(request,pk):
	editm = Medicine.objects.get(medicine_id=pk)
	type_med = Type_medicine.objects.all()
	if request.method == "POST":
		
		m_type = request.POST.get('m_type')
		type_name = Type_medicine.objects.get(type_id=m_type)
		# m_type = request.POST.get('m_type')
		description = request.POST.get('description')
		m_name = request.POST.get('m_name')
		total = request.POST.get('total')
		temp_max = request.POST.get('temp_max')
		temp_min = request.POST.get('temp_min')
		t_measurement = request.POST.get('t_measurement')
		
		
		

		editm.medicine_type = type_name
		editm.t_measurement = t_measurement

		editm.medicine_name = m_name
		editm.medicine_tempmax = temp_max
		editm.medicine_tempmin = temp_min
		editm.total = total
		
		editm.description = description
		editm.save()
		
		# return redirect('edit_car')
		return render(request,'edit_medicine.html',{'message1':"Edit medicine successful."})
	
	return render(request,'edit_medicine.html',{'editm':editm,'type_med':type_med})


def edit_coolbox(request,pk):
	editcb = Coolbox.objects.get(coolbox_id=pk)
	med_coolbox = Medicine.objects.all()
	if request.method == "POST":
		
		
		m_medicine = request.POST.get('m_medicine')
		medicine_name = Medicine.objects.get(medicine_id=m_medicine)

		dimention = request.POST.get('dimention')
		totals = request.POST.get('totals')
		t_measurement = request.POST.get('t_measurement')
		d_measurement = request.POST.get('d_measurement')
		weight = request.POST.get('weight')
		temp_max = request.POST.get('temp_max')
		temp_min = request.POST.get('temp_min')
		
		
		
		

		# editm.type_name = m_type

		
		editcb.medicine_name = medicine_name
		editcb.weight = weight
		editcb.coolboxtemp_max = temp_max
		editcb.coolboxtemp_min = temp_min
		editcb.dimension = dimention
		editcb.d_measurement = d_measurement
		editcb.t_measurement = t_measurement
		editcb.total = totals
		editcb.save()
		
		# return redirect('edit_car')
		return render(request,'edit_coolbox.html',{'message1':"Edit medicine successful."})
	
	return render(request,'edit_coolbox.html',{'editcb':editcb,'med_coolbox':med_coolbox})
		





def edit_shipping(request,pk):
	editsp = shipping.objects.get(shipping_id=pk)
	
	return render(request,'edit_shipping.html',{'editsp':editsp})

# def delete_user(request,pk):
# 	del_user = User.objects.get(admin_id=pk)
# 	if request.method == "POST":
# 		del_user.delete()
# 		return redirect('table_create')
# 	return render(request,'delete_user.html', {'del_user':del_user})

# def delete_user(request,pk):
# 	del_user = User.objects.get(admin_id=pk)
# 	del_user.delete()
# 	return render(request,'table_create.html', {'del_user':del_user})

# def delete_driver(request, pk):
# 	del_dri = Driver.objects.get(driver_id=pk)
# 	if request.method == 'POST':
# 		del_dri.delete()
# 		return redirect('table_driver')
# 	return render(request, 'table_driver.html')

# def delete_driver(request,pk):
# 	del_dri = Driver.objects.get(driver_id=pk)
# 	del_dri.delete()
# 	return redirect('table_driver')

def delete_type(request,pk):
	del_dri = Type_medicine.objects.get(type_id=pk)
	del_dri.delete()
	return redirect('table_type')
	




def driver_shipping(request):
	shipping_info = shipping.objects.all()
	return render(request,'driver_shipping.html',{'shipping_info':shipping_info})
	
def driver_shipping_confrim(request,pk):
	dscf = shipping.objects.get(shipping_id=pk)
	shipping_info = shipping.objects.all()
	return render(request,'driver_shipping_confrim.html',{'dscf':dscf,'shipping_info':shipping_info})

def driver_tracking(request):
	dritg = shipping.objects.all()
	return render(request,'driver_tracking.html',{'dritg':dritg})

def driver_track(request):
	dritk = shipping.objects.all()
	return render(request,'driver_track.html',{'dritk':dritk})

def driver_monitor(request):
	drimr = shipping.objects.all()
	return render(request,'driver_monitor.html',{'drimr':drimr})

