from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from shortcuts.utils import render_to_pdf
from django.conf import settings
from django.http import Http404

# Create your views here.
def index(request):
    return render(request,'app/index.html')
def python(request):
    return render(request,'app/python.html')
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404