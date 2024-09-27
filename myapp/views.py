from django.shortcuts import render,redirect

# Create your views here.
from .form import ImageUploadForm,EditOptionsForm
from .models import ImageUpload

def upload_image(request):
    if request.method == 'POST':
        form=ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_images')
    else:
        form=ImageUploadForm()
    return render(request, 'myapp/upload_image.html',{'form':form})

def view_image(request):
    image=ImageUpload.objects.all()
    return render(request, 'myapp/view_image.html',{"images":image})

# def edit_image(request):
#     image=ImageUpload.objects.all()
#     return render(request, 'myapp/edit_image.html',{"images":image})
    
def edit_options(request):
    images = ImageUpload.objects.all()  # Fetching images to display if needed

    if request.method == 'POST':
        form = EditOptionsForm(request.POST)
        if form.is_valid():
            # Process the number and possibly the comment
            number = form.process_data()  # Process the number as needed
            comment = form.cleaned_data.get('comment')  # Get the comment if provided
            
            # Implement your logic here (e.g., save to database, manipulate images, etc.)
            print(f"Received number: {number} and comment: {comment}")  # Example operation
            
            return redirect('edit_images')  # Replace with your actual view name

    else:
        form = EditOptionsForm()  # Instantiate the form for GET request
    image=ImageUpload.objects.all()
    return render(request, 'myapp/edit_image.html', {'form': form, 'images': images})