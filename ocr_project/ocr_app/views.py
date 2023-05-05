import tempfile
import os
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .ocr import extract_text
from .forms import UploadImageForm

def index(request):
    return render(request, 'ocr_app/index.html')

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded file to a temporary file
            uploaded_file = request.FILES['image']
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            temp_file.write(uploaded_file.read())
            temp_file.close()

            text = extract_text(temp_file.name)

            # Delete the temporary file
            os.unlink(temp_file.name)

            return render(request, 'ocr_app/result.html', {'text': text})
    return HttpResponseRedirect(reverse('ocr_app:index'))
