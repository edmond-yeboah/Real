from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
from .forms import CreateUserForm,addlistingForm
from .models import agent, listing, compare, favourite, Message, region,compare_region, PrivateSchools,PublicSchools,Bank,Manufacturing,Hospital,Insurance,SecondarySchools,Programs






def home(request):
    context = {}
    all_listings = listing.objects.all()
    context["all_listings"] = all_listings

    locations_first = region.objects.all()[:4]
    context["locations_first"] = locations_first

    insurance_first = Insurance.objects.all()[:4]
    context["insurance_first"] = insurance_first

    private_first = PrivateSchools.objects.all()[:4]
    context["private_first"] = private_first

    bank_first = Bank.objects.all()[:4]
    context["bank_first"]= bank_first

    hospital_first = Hospital.objects.all()[:4]
    context["hospital_first"]= hospital_first

    manu_first = Manufacturing.objects.all()[:4]
    context["manu_first"]=manu_first

    return render(request,'boss/home.html',context)


def register(request):
    if request.user.is_authenticated:
        return redirect('../profile/')
    else:
        if request.method == 'POST':
            username = request.POST['user_name']
            email = request.POST['email']
            password1 = request.POST['user_password']
            password2 = request.POST['confirm-password']

            if password1==password2:
                if User.objects.filter(username=username).exists():
                    messages.warning(request,'Username already exist!')
                    return redirect('../register/')
                
                elif User.objects.filter(email=email).exists():
                    messages.warning(request,'Email already exist!')
                    return redirect('../register/') 
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email)
                    user.save()
                    messages.success(request,'Account successfully created for ' + username +'!')
            else:
                messages.warning(request,'Passwords do not match!')
                return redirect('../register/')
            return redirect('../login/')
        else:
            return render(request,'boss/register.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('../profile/')
    else:
         if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('../')
            else:
                messages.warning(request,'Invalid username or password!')
                return redirect('../login/')

         else:
            return render(request,'boss/login.html')



def logoutUser(request):
    logout(request)
    return redirect('../')



@login_required(login_url='login')
def profile(request):
    context={}
    check = agent.objects.filter(user_id = request.user.id)
    receiver = User.objects.get(username=request.user.username)
    
    if len(check)>0:
        data = agent.objects.get(user_id = request.user.id)
        context["data"]=data

        all = listing.objects.filter(Agent_id=request.user.id)
        context["listing"]= all

        fav = favourite.objects.filter(user_id=request.user.id)
        context["fav"]=fav

        mes = Message.objects.filter(to=receiver)
        context["mes"]= mes

    if request.method == "POST":
        fname = request.POST["fullname"]
        address = request.POST["address"]
        city = request.POST["city"]
        state = request.POST["state"]
        zipcode = request.POST["zipcode"]
        tit = request.POST["title"]
        mail = request.POST["email"]
        number = request.POST["phone"]
        abt = request.POST["about"]

        usr = User.objects.get(id=request.user.id)
        usr.email = mail
        usr.save()
 
        data.fullname = fname
        data.address = address
        data.city = city
        data.title = tit
        data.phone = number
        data.about_me = abt
        data.state = state
        data.zipcode = zipcode

        data.save()

    return render(request,'boss/profile.html',context)


@login_required(login_url='login')
def addlisting(request):
    context = {}
    ch = agent.objects.filter(user_id=request.user.id)
    if len(ch)>0:
        data = agent.objects.get(user_id=request.user.id)
        context["data"]= data
    form = addlistingForm()
    if request.method=="POST":
        agent_name = User.objects.get(username=request.user.username)
        title = request.POST['title']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        ptype = request.POST['property_type']
        pstatus = request.POST['property_status']
        price = request.POST['price']
        desc = request.POST['description']
        numbedrooms = request.POST['number_bedrooms']
        numrooms = request.POST['number_rooms']
        numbath = request.POST['number_bath']
        numgarage = request.POST['number_garage']
        year = request.POST['year_built']
        floorsize = request.POST['floor_size']
        lat= request.POST['latitude_input']
        lon = request.POST['longitude_input']
        image = request.FILES['file']
       
    
        now = listing.objects.create(
            Agent=agent_name,
            title=title,
            address=address,
            city=city,
            state=state,
            zipcode=zipcode,
            property_type=ptype,
            property_status=pstatus,
            price=price,
            description=desc,
            number_bedrooms=numbedrooms,
            number_rooms=numrooms,
            number_bath=numbath,
            number_garage=numgarage,
            year_built=year,
            # rooms_size=roomsize,
            # bath_size=bathsize,
            floor_size=floorsize,
            lat=lat,
            lon=lon,
            image=image,
            )
        
        return redirect('../mylisting/')
    context["form"] = form
    return render(request,'boss/submit-property.html',context)



@login_required(login_url='login')
def mylisting(request):
    context={}
    ch = agent.objects.filter(user_id=request.user.id)
    if len(ch)>0:
        data = agent.objects.get(user_id=request.user.id)
        context["data"]=data

    all = listing.objects.filter(Agent_id=request.user.id).order_by("-id")
    context["listing"]= all

    

    return render(request,'boss/my-property.html',context)



@login_required(login_url='login')
def deletelisting(request):
    context = {}

    if "lid" in request.GET:
        lid = request.GET["lid"]
        prd = get_object_or_404(listing,id=lid)
        context["listing"]=prd

        if "action" in request.GET:
            prd.delete()
            context["status"] = str(prd.title)+"  deleted successfully!"

    return render(request,'boss/delete-property.html',context)



@login_required(login_url='login')
def editlisting(request):
    context={}

    lid = request.GET["lid"]
    listings = get_object_or_404(listing,id=lid)
    context["listing"]=listings

    if request.method == "POST":
        title = request.POST['title']
        address = request.POST['address']
        # neighbouhoood = request.POST['neighborhood']
        # country = request.POST['country']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        price = request.POST['price']
        desc = request.POST['description']
        # pid = request.POST['property_id']
        numbedrooms = request.POST['number_bedrooms']
        numrooms = request.POST['number_rooms']
        numbath = request.POST['number_bath']
        numgarage = request.POST['number_garage']
        year = request.POST['year_built']
        # roomsize = request.POST['rooms_size']
        # bathsize = request.POST['bath_size']
        floorsize = request.POST['floor_size']
        lat = request.POST['latitude_input']
        lon = request.POST['longitude_input']

        listings.title = title
        listings.address = address
        # listings.neighbouhoood = neighbouhoood
        # listings.country = country
        listings.city = city
        listings.state = state
        listings.zipcode = zipcode
        listings.price = price
        listings.description = desc
        # listings.property_id = pid
        listings.number_bedrooms = numbedrooms
        listings.number_rooms = numrooms
        listings.number_bath = numbath
        listings.number_garage = numgarage
        listings.year_built = year
        # listings.rooms_size = roomsize
        # listings.bath_size = bathsize
        listings.floor_size = floorsize
        listings.lat = lat
        listings.lon = lon

        listings.save()
        context["status"] = "Changes saved successfully"
        context["id"] = lid

    return render(request,'boss/edit-property.html',context)


@login_required(login_url='login')
def listings(request):
    context = {}
    all_listings = listing.objects.all()
    
    if request.method=="POST":
        reg=request.POST["region"]
        status=request.POST["status"]
        types=request.POST["type"]
        bath=request.POST["baths"]
        bed=request.POST["beds"]
        

        searched = listing.objects.filter(Q(property_status__icontains=status) & Q(address__icontains=reg) & Q(number_bedrooms__contains=bed) & Q(number_bath__contains=bath)& Q(property_type__contains=types))
        context["all_listings"] = searched
    else:
        context["all_listings"] = all_listings

    return render(request,'boss/listing.html',context)



@login_required(login_url='login')
def singlelisting(request):
    context ={}

    compare_items = compare.objects.filter(user_id=request.user.id)
    context["compare_items"]=compare_items

    if "lid" in request.GET:
        id = request.GET['lid']
        obj = listing.objects.get(id=id)
        context["listing"]=obj



    if "action" in request.GET:
        is_exist = compare.objects.filter(listings_id=id,user_id=request.user.id)
        if len(is_exist)>0:
            context['already']="Listing already added to compare"
            print("already exist")

        elif len(compare_items)>=3:
            context['already']="Listing already added to compare"
            print("already exist")

        else:
            lis=get_object_or_404(listing,id=id)
            usr=get_object_or_404(User,id=request.user.id)
            c= compare(user=usr,listings=lis)
            c.save()

    if "love" in request.GET:
        is_exist = favourite.objects.filter(fav_listing_id=id, user_id=request.user.id)
        if len(is_exist)>0:
            context['already2']="Listing already added to favourites"
        else:
            liss=get_object_or_404(listing,id=id)
            usrr=get_object_or_404(User,id=request.user.id)
            f= favourite(user=usrr,fav_listing=liss)
            f.save()

    if request.method == "POST":
        message_to = request.POST["to"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        text = request.POST["message"]

        new = Message.objects.create(
            to = message_to,
            phone = phone,
            email = email,
            message = text,
        )

    all_listings = listing.objects.all()
    context["all"] = all_listings

    return render(request,'boss/single-property.html',context)


@login_required(login_url='login')
def comparelisting(request):
    context ={}

    compare_items = compare.objects.filter(user_id=request.user.id)
    context["compare_items"]=compare_items

    if "lid" in request.GET:
        lid = request.GET["lid"]
        pd = get_object_or_404(compare,id=lid)
        
        if "action" in request.GET:
            pd.delete()

    return render(request,'boss/compare-property.html',context)


@login_required(login_url='login')
def bookmarklist(request):
    context = {}

    fav = favourite.objects.filter(user_id=request.user.id)
    # print(favourite_items)
    context["fav"]=fav

    if "lid" in request.GET:
         fid = request.GET["lid"]
         fl = get_object_or_404(favourite,id=fid)

         if "action" in request.GET:
             fl.delete()

    return render(request,'boss/bookmark-list.html',context)



@login_required(login_url='login')
def messages(request):
    context ={}

    receiver = User.objects.get(username=request.user.username)
    all = Message.objects.filter(to=receiver).order_by("-id")
    context["Message"]= all

    if "lid" in request.GET:
         mid = request.GET["lid"]
         ml = get_object_or_404(Message,id=mid)

         if "action" in request.GET:
             ml.delete()

    return render(request,'boss/messages.html',context)



@login_required(login_url='login')
def accra(request):
    context ={}
    id=1
    region_compares = compare_region.objects.filter(user_id=request.user.id)
    context["compares"] = region_compares

    a = region.objects.get(id=id)
    context["a"]= a

    if "rid" in request.GET:
        rid= request.GET["rid"]

        exist= compare_region.objects.filter(region_id=rid,user_id=request.user.id)
        if len(exist)>0:
            context['already']="Region already added to compare"
        elif len(region_compares)>=3:
            context['full']="Caompare full"
        else:
            reg= get_object_or_404(region,id=rid)
            usr= get_object_or_404(User,id=request.user.id)
            rc= compare_region(user=usr,region=reg)
            rc.save()

    return render(request,'boss/regions-accra.html',context)


@login_required(login_url='login')
def ashanti(request):
    context ={}
    id=4
    region_compares = compare_region.objects.filter(user_id=request.user.id)
    context["compares"] = region_compares

    a = region.objects.get(id=id)
    context["a"]= a

    if "rid" in request.GET:
        rid= request.GET["rid"]

        exist= compare_region.objects.filter(region_id=rid,user_id=request.user.id)
        if len(exist)>0:
            context['already']="Region already added to compare"
        elif len(region_compares)>=3:
            context['full']="Caompare full"
        else:
            reg= get_object_or_404(region,id=rid)
            usr= get_object_or_404(User,id=request.user.id)
            rc= compare_region(user=usr,region=reg)
            rc.save()
    return render(request,'boss/regions-kumasi.html',context)


@login_required(login_url='login')
def central(request):
    context ={}
    id=3
    region_compares = compare_region.objects.filter(user_id=request.user.id)
    context["compares"] = region_compares

    a = region.objects.get(id=id)
    context["a"]= a

    if "rid" in request.GET:
        rid= request.GET["rid"]

        exist= compare_region.objects.filter(region_id=rid,user_id=request.user.id)
        if len(exist)>0:
            context['already']="Region already added to compare"
        elif len(region_compares)>=3:
            context['full']="Caompare full"
        else:
            reg= get_object_or_404(region,id=rid)
            usr= get_object_or_404(User,id=request.user.id)
            rc= compare_region(user=usr,region=reg)
            rc.save()

    return render(request,'boss/regions-central.html',context)


@login_required(login_url='login')
def eastern(request):
    context ={}
    id=2
    region_compares = compare_region.objects.filter(user_id=request.user.id)
    context["compares"] = region_compares

    a = region.objects.get(id=id)
    context["a"]= a

    if "rid" in request.GET:
        rid= request.GET["rid"]

        exist= compare_region.objects.filter(region_id=rid,user_id=request.user.id)
        if len(exist)>0:
            context['already']="Region already added to compare"
        elif len(region_compares)>=3:
            context['full']="Caompare full"
        else:
            reg= get_object_or_404(region,id=rid)
            usr= get_object_or_404(User,id=request.user.id)
            rc= compare_region(user=usr,region=reg)
            rc.save()

    return render(request,'boss/regions-eastern.html',context)


@login_required(login_url='login')
def volta(request):
    context ={}
    id=7
    region_compares = compare_region.objects.filter(user_id=request.user.id)
    context["compares"] = region_compares

    a = region.objects.get(id=id)
    context["a"]= a

    if "rid" in request.GET:
        rid= request.GET["rid"]

        exist= compare_region.objects.filter(region_id=rid,user_id=request.user.id)
        if len(exist)>0:
            context['already']="Region already added to compare"
        elif len(region_compares)>=3:
            context['full']="Caompare full"
        else:
            reg= get_object_or_404(region,id=rid)
            usr= get_object_or_404(User,id=request.user.id)
            rc= compare_region(user=usr,region=reg)
            rc.save()

    return render(request,'boss/regions-volta.html',context)


@login_required(login_url='login')
def western(request):
    context ={}
    id=8
    region_compares = compare_region.objects.filter(user_id=request.user.id)
    context["compares"] = region_compares

    a = region.objects.get(id=id)
    context["a"]= a

    if "rid" in request.GET:
        rid= request.GET["rid"]

        exist= compare_region.objects.filter(region_id=rid,user_id=request.user.id)
        if len(exist)>0:
            context['already']="Region already added to compare"
        elif len(region_compares)>=3:
            context['full']="Caompare full"
        else:
            reg= get_object_or_404(region,id=rid)
            usr= get_object_or_404(User,id=request.user.id)
            rc= compare_region(user=usr,region=reg)
            rc.save()

    return render(request,'boss/regions-western.html',context)


@login_required(login_url='login')
def uppereast(request):
    context ={}
    id=5
    region_compares = compare_region.objects.filter(user_id=request.user.id)
    context["compares"] = region_compares

    a = region.objects.get(id=id)
    context["a"]= a

    if "rid" in request.GET:
        rid= request.GET["rid"]

        exist= compare_region.objects.filter(region_id=rid,user_id=request.user.id)
        if len(exist)>0:
            context['already']="Region already added to compare"
        elif len(region_compares)>=3:
            context['full']="Caompare full"
        else:
            reg= get_object_or_404(region,id=rid)
            usr= get_object_or_404(User,id=request.user.id)
            rc= compare_region(user=usr,region=reg)
            rc.save()

    return render(request,'boss/regions-uppereast.html',context)


@login_required(login_url='login')
def upperwest(request):
    context ={}
    id=6
    region_compares = compare_region.objects.filter(user_id=request.user.id)
    context["compares"] = region_compares

    a = region.objects.get(id=id)
    context["a"]= a

    if "rid" in request.GET:
        rid= request.GET["rid"]

        exist= compare_region.objects.filter(region_id=rid,user_id=request.user.id)
        if len(exist)>0:
            context['already']="Region already added to compare"
        elif len(region_compares)>=3:
            context['full']="Caompare full"
        else:
            reg= get_object_or_404(region,id=rid)
            usr= get_object_or_404(User,id=request.user.id)
            rc= compare_region(user=usr,region=reg)
            rc.save()

    return render(request,'boss/regions-upperwest.html',context)


@login_required(login_url='login')
def CompareRegion(request):
    context={}
    region_compares = compare_region.objects.filter(user_id=request.user.id)
    context["compares"] = region_compares

    if "lid" in request.GET:
        lid = request.GET["lid"]
        pd = get_object_or_404(compare_region,id=lid)
        
        if "action" in request.GET:
            pd.delete()

    return render(request,'boss/compare-region.html',context)



def SearchResults(request):
    context={}

    locations =True
    shs=True
    bank=True
    manufacturing=True
    hospital=True
    insure=True
    privatesch=True
    publicsch = True
    
    if "query" in request.GET:
        query=request.GET["query"]

        q = query.strip() #removing all white spaces fro query

        if len(q)>0:
     
            locations = region.objects.filter(name__icontains=query)
            if len(locations)>0:
                context["locations"] = locations
            else:
                locations = False

            privatesch = PrivateSchools.objects.filter(name__icontains=query)
            if len(privatesch)>0:
                context["privatesch"] = privatesch
            else:
                privatesch = False

            publicsch = PublicSchools.objects.filter(name__icontains=query)
            if len(publicsch)>0:
                context["publicsch"] = publicsch
            else:
                publicsch = False
            
            shs = SecondarySchools.objects.filter(name__icontains=query)
            if len(shs)>0:
                context["shs"] = shs
            else:
                shs = False

            bank = Bank.objects.filter(name__icontains=query)
            if len(bank)>0:
                context["bank"] = bank
            else:
                bank = False

            manufacturing = Manufacturing.objects.filter(name__icontains=query)
            if len(manufacturing)>0:
                context["man"] = manufacturing
            else:
                manufacturing = False

            hospital = Hospital.objects.filter(name__icontains=query)
            if len(hospital)>0:
                context["min"] = hospital
            else:
                hospital = False

            insure = Insurance.objects.filter(name__icontains=query)
            if len(insure)>0:
                context["ins"] = insure
            else:
                insure = False

            if locations==False and privatesch==False and publicsch==False and shs==False and bank==False and manufacturing==False and hospital==False and insure==False:
                 context['nothing']="Please enter a valid search word!"
            else:
                pass
            
        else:
            context['nothing']="Please enter a valid search word!"
    return render(request,'boss/search_result.html',context)




def LocationTemplate(request):
    context={}

    all = region.objects.all()
    context["all"]=all

    # print(all)

    if "rid" in request.GET:
        rid = request.GET['rid']
        locations = get_object_or_404(region,id=rid)
        private_schools = locations.private_schools.all()
        public_schools = locations.public_schools.all()
        shs_schools = locations.shs_schools.all()
        hospitals = locations.hospitals.all()
        bank = locations.bank.all()
        manu = locations.manu.all()
        # mining = locations.hospitals.all()
        insurance = locations.insurance.all()
       
       
        context["private_schools"]=private_schools
        context["public_schools"]=public_schools
        context["shs_schools"]=shs_schools
        context["locations"]=locations
        context["hospitals"]=hospitals
        context["bank"]=bank
        context["manu"]=manu
        # context["mining"]=mining
        context["insurance"]=insurance

        ho = locations.name
        house = listing.objects.filter(address__icontains=ho)
        
        context["house"] = house
       

    return render(request,'boss/locations-template.html',context)



def SchoolsTemplate(request):
    context={}

    if "rid" in request.GET:
        rid = request.GET['rid']
        public = get_object_or_404(PublicSchools,id=rid)
        context["schools"]= public
        all = PublicSchools.objects.all()
        context["all"]= all
        context['uni']="uni"
        programs = public.programs.all()
        context["programs"]=programs
        campuses = public.campuses.all()
        context["campuses"]=campuses

    elif "sid" in request.GET:
        sid = request.GET['sid']
        private = get_object_or_404(PrivateSchools,id=sid)
        context["schools"]= private
        all = PrivateSchools.objects.all()
        context["all"]=all
        context['uni']="uni"
        programs = private.programs.all()
        context["programs"]=programs
        campuses = private.campuses.all()
        context["campuses"]=campuses

    elif "hid" in request.GET:
        hid = request.GET['hid']
        shs = get_object_or_404(SecondarySchools,id=hid)
        context["schools"]=shs
        all = SecondarySchools.objects.all()
        context["all"] = all
        context['secondary']="secondary"
        programs = shs.programs.all()
        context["programs"]= programs
        facilities = shs.facilities.all()
        context["facilities"]=facilities
        asso = shs.asso.all()
        context["asso"]=asso
    else:
        pass

    return render(request,'boss/schools-template.html',context)



def IndustryTemplate(request):
    context={}

    if "bid" in request.GET:
        bid = request.GET['bid']
        bank = get_object_or_404(Bank,id=bid)
        context["industry"] = bank
        all = Bank.objects.all()
        context["all"]=all
        branches = bank.branches.all()
        context["branches"]=branches
        services = bank.services.all()
        context["services"]=services
        context["same"]="same"

    elif "mid" in request.GET:
        mid = request.GET['mid']
        manu = get_object_or_404(Manufacturing,id=mid)
        context["industry"] = manu
        all = Manufacturing.objects.all()
        context["all"]=all
        branches = manu.branches.all()
        context["branches"]=branches
        products = manu.products.all()
        context["products"]=products
        context["same"]="same"


    elif "min" in request.GET:
        minn = request.GET['min']
        mini = get_object_or_404(Hospital,id=minn)
        context["industry"] = mini
        all = Hospital.objects.all()
        context["all"]=all
        branches = mini.branches.all()
        context["branches"]=branches
        # departments = mini.departments.all()
        # context["departments"]=departments
        facility = mini.facility.all()
        context["facilities"] = facility
        context["hos"]="hospital"

    
    elif "ins" in request.GET:
        isnid = request.GET['ins']
        ins = get_object_or_404(Insurance,id=isnid)
        context["industry"] = ins
        all = Insurance.objects.all()
        context["all"]=all
        branches = ins.branches.all()
        context["branches"]=branches
        services = ins.services.all()
        context["services"]=services
        context["same"]="same"


    return render(request,'boss/industry-template.html',context)