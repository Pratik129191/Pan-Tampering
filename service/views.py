from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, reverse
from django.conf import settings
from .forms import PancardForm, PancardImageForm
from .models import Pancard, PancardImage, PanOriginal
from django.contrib.auth.decorators import login_required
from skimage.metrics import structural_similarity
import imutils
import os
import cv2
from PIL import Image


def say_hello(request):
    return HttpResponse("Hello World")


@login_required
def pan_details(request):
    form_p = PancardForm()
    form_i = PancardImageForm()
    imgs = []
    pan = Pancard.objects.filter(user=request.user).order_by('-datetime')
    for p in pan:
        imgs.append(PancardImage.objects.get(pancard=p.id))

    context = {
        'form_p': form_p,
        'form_i': form_i,
        'imgs': imgs,
        'detail': reverse('service:detail')
    }

    if request.method == 'POST':
        form_p = PancardForm(request.POST)
        form_i = PancardImageForm(request.POST, request.FILES)
        if form_p.is_valid() and form_i.is_valid():
            form_p.user = request.user
            form_p.save()

            form_i.user = request.user
            form_i.save()

            pan = Pancard.objects.select_related('user').filter(user=request.user).latest().id
            url = (reverse('service:detail')
                   + str(pan)
                   )
            # return render(request, 'upload.html', context)
            return redirect(url)
    return render(request, 'upload.html', context)


@login_required
def pan_tampered(request, id):
    pan = Pancard.objects.get(id=id)
    pan.status = 'P'
    pan.save()
    panimg = PancardImage.objects.filter(pancard=id).latest()
    orgimg = PanOriginal.objects.all()[0]

    upl_img_path = str(panimg.image.path).replace("\\", "/")
    org_img_path = str(orgimg.image.path).replace("\\", "/")

    file_upl = upl_img_path.split("/")[-1].split(".")[0]
    file_org = org_img_path.split("/")[-1].split(".")[0]

    # Resize and save the uploaded image
    uploaded_image = Image.open(upl_img_path).resize((250, 160))
    uploaded_image.save(f"{file_upl}.jpg")

    # Resize and save the original image to ensure both uploaded and original matches in size
    original_image = Image.open(org_img_path).resize((250, 160))
    original_image.save(f"{file_org}.jpg")

    # Read uploaded and original image as array
    original_image = cv2.imread(org_img_path)
    uploaded_image = cv2.imread(upl_img_path)

    # Convert image into grayscale
    original_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    uploaded_gray = cv2.cvtColor(uploaded_image, cv2.COLOR_BGR2GRAY)

    # Calculate structural similarity
    (score, diff) = structural_similarity(original_gray, uploaded_gray, full=True)
    diff = (diff * 255).astype("uint8")


    # Calculate threshold and contours
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # Draw contours on image
    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(uploaded_image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    path = "/".join(org_img_path.split('/')[:-1])
    cv2.imwrite(f"{path}/{file_upl}_uploaded.jpg", uploaded_image)
    panimg.upload = f"service/images/{file_upl}_uploaded.jpg"

    cv2.imwrite(f"{path}/{file_upl}_diff.jpg", diff)
    panimg.diff = f"service/images/{file_upl}_diff.jpg"

    cv2.imwrite(f"{path}/{file_upl}_thresh.jpg", thresh)
    panimg.thresh = f"service/images/{file_upl}_thresh.jpg"

    panimg.save()

    score = round(score * 100, 2)
    pan.confidence = score
    pan.status = 'C'
    if 95 < score <= 100:
        pan.result = 'O'
    pan.save()

    pan_sh = PancardImage.objects.get(pancard=id)
    context = {
        'upload': pan_sh.upload.url,
        'diff': pan_sh.diff.url,
        'thresh': pan_sh.thresh.url,
        'pan': pan,
        'home': reverse('core:home'),
        'back': reverse('service:detail'),

    }
    return render(request, 'show.html', context)

