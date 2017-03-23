from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from products.models import ProductFeatured, Product
from .forms import ContactForm, SignUpForm
from .models import SignUp

# Create your views here.
def home(request):
		products = Product.objects.all()[:8]
		context = {
				"products": products,
		}






		return render(request, "home.html", context)








def contact(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
		# 	#print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print email, message, full_name
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'youotheremail@email.com']
		contact_message = "%s: %s via %s"%(
				form_full_name,
				form_message,
				form_email)
		some_html_message = """
		<h1>hello</h1>
		"""
		send_mail(subject,
				contact_message,
				from_email,
				to_email,
				html_message=some_html_message,
				fail_silently=True)

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
	}
	return render(request, "forms.html", context)
















