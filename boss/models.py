from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class agent(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    fullname = models.CharField(max_length=200,null=True, blank=True)
    username = models.CharField(max_length=200,null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zipcode = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    about_me = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username




class listing(models.Model):
    PTYPE=(('House','House'),('Apartment','Apartment'),('Villas','Villas'),('Commercial','Commercial'),('Garages','Garages'))
    PSTATUS=(('For Sale','For Sale'),('For Rent','For Rent'))
    FSELECT=(('First Floor','First Floor'),('Second Floor','Second Floor'))
    # ASELECT=(('Iron','Iron'),('Sandals','Sandals'))

    Agent = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='listing_pics')
    title = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    # neighbouhoood = models.CharField(max_length=200, null=True, blank=True)
    # country = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zipcode = models.CharField(max_length=200, null=True, blank=True)
    property_type = models.CharField(max_length=200, null=True, blank=True, choices=PTYPE)
    property_status = models.CharField(max_length=200, null=True, blank=True,choices=PSTATUS)
    price = models.CharField(max_length=200,null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    # property_id = models.CharField(max_length=200,null=True, blank=True)
    number_bedrooms = models.CharField(max_length=200,null=True, blank=True)
    number_rooms = models.CharField(max_length=200,null=True, blank=True)
    number_bath = models.CharField(max_length=200,null=True, blank=True)
    number_garage = models.CharField(max_length=200,null=True, blank=True)
    year_built = models.CharField(max_length=200,null=True, blank=True)
    # floor_select = models.CharField(max_length=200, null=True, blank=True, choices=FSELECT)
    floor_size = models.CharField(max_length=200,null=True, blank=True)
    # rooms_size = models.CharField(max_length=200,null=True, blank=True)
    # bath_size = models.CharField(max_length=200,null=True, blank=True)
    lat = models.CharField(max_length=200, null=True, blank=True)
    lon = models.CharField(max_length=200, null=True, blank=True)
    # amenity = models.ManyToManyField(amenities)

    def __str__(self):
        return self.title



class compare(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    listings = models.ForeignKey(listing,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class favourite(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fav_listing = models.ForeignKey(listing,on_delete=models.CASCADE)
    added_on =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Message(models.Model):
    to = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    message = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.to

class Programs(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Campuses(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    lat = models.CharField(max_length=200, null=True, blank=True)
    lon = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class PrivateSchools(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(default='default.jpg')
    about = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    cost = models.CharField(max_length=200, null=True, blank=True)
    # cost_about = models.CharField(max_length=200, null=True, blank=True)
    # admission_about = models.CharField(max_length=200, null=True, blank=True)
    admission = models.CharField(max_length=200, null=True, blank=True)
    # enrol_about = models.CharField(max_length=200, null=True, blank=True)
    enrolment = models.CharField(max_length=200, null=True, blank=True)
    # grad_about = models.CharField(max_length=200, null=True, blank=True)
    graduates = models.CharField(max_length=200, null=True, blank=True)
    population = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    tel = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    acept_rate = models.CharField(max_length=200, null=True, blank=True)
    programs = models.ManyToManyField(Programs, blank=True)
    campuses = models.ManyToManyField(Campuses, blank=True)
    # opera_about = models.CharField(max_length=200, null=True, blank=True)
    num_professor = models.CharField(max_length=200, null=True, blank=True)
    num_assoprof = models.CharField(max_length=200, null=True, blank=True)
    num_assprof = models.CharField(max_length=200, null=True, blank=True)
    num_lec = models.CharField(max_length=200, null=True, blank=True)
    num_instruct = models.CharField(max_length=200, null=True, blank=True)
    num_nonaca = models.CharField(max_length=200, null=True, blank=True)
    lat = models.CharField(max_length=200, null=True, blank=True)
    lon = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name


class PublicSchools(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(default='default.jpg')
    about = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    # cost_about = models.CharField(max_length=200, null=True, blank=True)
    cost = models.CharField(max_length=200, null=True, blank=True)
    # admission_about = models.CharField(max_length=200, null=True, blank=True)
    admission = models.CharField(max_length=200, null=True, blank=True)
    # enrol_about = models.CharField(max_length=200, null=True, blank=True)
    enrolment = models.CharField(max_length=200, null=True, blank=True)
    # grad_about = models.CharField(max_length=200, null=True, blank=True)
    graduates = models.CharField(max_length=200, null=True, blank=True)
    population = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    tel = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    acept_rate = models.CharField(max_length=200, null=True, blank=True)
    programs = models.ManyToManyField(Programs, blank=True)
    campuses = models.ManyToManyField(Campuses, blank=True)
    # opera_about = models.CharField(max_length=200, null=True, blank=True)
    num_professor = models.CharField(max_length=200, null=True, blank=True)
    num_assoprof = models.CharField(max_length=200, null=True, blank=True)
    num_assprof = models.CharField(max_length=200, null=True, blank=True)
    num_lec = models.CharField(max_length=200, null=True, blank=True)
    num_instruct = models.CharField(max_length=200, null=True, blank=True)
    num_nonaca = models.CharField(max_length=200, null=True, blank=True)
    lat = models.CharField(max_length=200, null=True, blank=True)
    lon = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name


class Facilities(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Associations(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class SecondarySchools(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(default='default.jpg')
    about = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    cost = models.CharField(max_length=200, null=True, blank=True)
    # acaperf_about = models.CharField(max_length=200, null=True, blank=True)
    num_acaperf = models.CharField(max_length=200, null=True, blank=True)
    # admission_about = models.CharField(max_length=200, null=True, blank=True)
    admission = models.CharField(max_length=200, null=True, blank=True)
    enrolment = models.CharField(max_length=200, null=True, blank=True)
    graduates = models.CharField(max_length=200, null=True, blank=True)
    population = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    tel = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    programs = models.ManyToManyField(Programs, blank=True)
    facilities = models.ManyToManyField(Facilities, blank=True)
    asso = models.ManyToManyField(Associations, blank=True)


    def __str__(self):
        return self.name



class branch(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    branchLat = models.CharField(max_length=200,null=True,blank=True)
    branchLon = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class service(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Bank(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(default='default.png')
    about = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    tel = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    branches = models.ManyToManyField(branch, blank=True)
    services = models.ManyToManyField(service, blank=True)
    # rev_about = models.CharField(max_length=200, null=True, blank=True)
    revenue = models.CharField(max_length=200, null=True, blank=True)
    employment = models.CharField(max_length=200, null=True, blank=True)
    # emp_about = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Manufacturing(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(default='default.png')
    about = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    tel = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    branches = models.ManyToManyField(branch, blank=True)
    products = models.ManyToManyField(product, blank=True)
    # rev_about = models.CharField(max_length=200, null=True, blank=True)
    revenue = models.CharField(max_length=200, null=True, blank=True)
    employment = models.CharField(max_length=200, null=True, blank=True)
    # emp_about = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class facility(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name



class Hospital(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(default='default.png')
    about = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    tel = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    branches = models.ManyToManyField(branch, blank=True)
    # departments = models.ManyToManyField(departments, blank=True)
    facility = models.ManyToManyField(facility, blank=True)
    revenue = models.CharField(max_length=200, null=True, blank=True)
    employment = models.CharField(max_length=200, null=True, blank=True)
    # emp_about = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Insurance(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(default='default.png')
    about = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    tel = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    branches = models.ManyToManyField(branch,blank=True)
    services = models.ManyToManyField(service, blank=True)
    # rev_about = models.CharField(max_length=200, null=True, blank=True)
    revenue = models.CharField(max_length=200, null=True, blank=True)
    employment = models.CharField(max_length=200, null=True, blank=True)
    # emp_about = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name 


class region(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(default='default.jpg')
    description = models.CharField(max_length=200, blank=True)
    about = models.CharField(max_length=1000, null=True, blank=True)
    covid_about = models.CharField(max_length=1000, null=True, blank=True)
    covid = models.CharField(max_length=200, null=True, blank=True)
    pop_about = models.CharField(max_length=1000, null=True, blank=True)
    population = models.CharField(max_length=200, null=True, blank=True)
    male_population = models.CharField(max_length=200,null=True, blank=True)
    female_population = models.CharField(max_length=200,null=True, blank=True)
    chri_num = models.CharField(max_length=200, null=True, blank=True)
    muslim_num = models.CharField(max_length=200, null=True, blank=True)
    other_num = models.CharField(max_length=200, null=True, blank=True)
    tradi_num = models.CharField(max_length=200, null=True, blank=True)
    diversity_about = models.CharField(max_length=1000, null=True, blank=True)
    economy_about = models.CharField(max_length=1000, null=True, blank=True)
    housing_about = models.CharField(max_length=2000, null=True, blank=True)
    poverty_rate = models.CharField(max_length=2000, null=True, blank=True)
    median_age = models.CharField(max_length=2000, null=True, blank=True)
    num_employees = models.CharField(max_length=2000, null=True, blank=True)
    private_schools = models.ManyToManyField(PrivateSchools, blank=True)
    public_schools = models.ManyToManyField(PublicSchools, blank=True)
    shs_schools = models.ManyToManyField(SecondarySchools, blank=True)
    hospitals = models.ManyToManyField(Hospital, blank=True)
    bank = models.ManyToManyField(Bank, blank=True)
    manu = models.ManyToManyField(Manufacturing, blank=True)
    insurance = models.ManyToManyField(Insurance, blank=True)

    def __str__(self):
        return self.name


class compare_region(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    region = models.ForeignKey(region, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username






