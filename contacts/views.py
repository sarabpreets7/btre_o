from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def contact(request):
    if request.method =='POST':
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        realtor_email = request.POST['realtor_email']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'you have already made an inquiry for this listing')
                return redirect('/listings/' + listing_id)


        contact = Contact(listing_id=listing_id,listing=listing,name=name,email=email,phone=phone,user_id=user_id)
        contact.save()
        send_mail(
            'Propert Listing Inquiry',
            'Here is inquiry for '+ listing+' sign into admin.',
            'sarabpreets7@gmail.com',
            [realtor_email,'rocko78903@gmail.com'],
            fail_silently=False,
        )



        messages.success(request,'Your request has been submitted,a realtor will get in contact with you')

        return redirect('/listings/'+listing_id)

