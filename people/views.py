from django.shortcuts import render

# Create your views here.
def user_list_view(request):
    return render(request, template_name="people/list_user.html", context=None)