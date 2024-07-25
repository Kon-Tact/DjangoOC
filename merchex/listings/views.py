from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from listings.models import Band
from listings.models import New
from listings.forms import ContactUsForm, BandForm, NewForm

def bands_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/bands_list.html', {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {'band': band})

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', {'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_update.html', {'form': form})

def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        band.delete()
        return redirect('bands_list')
    return render(request, 'listings/band_delete.html', {'band': band})

def news_list(request):
    news = New.objects.all()
    return render(request, 'listings/news_list.html', {'news': news})

def new_detail(request, id):
    new = New.objects.get(id=id)
    return render(request, 'listings/new_detail.html', {'new': new})

def new_create(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            new = form.save()
            return redirect('news-detail', new.id)
    else:
        form = NewForm()
    return render(request, 'listings/new_create.html', {'form': form})

def new_update(request, id):
    new = New.objects.get(id=id)
    if request.method == 'POST':
        form = NewForm(request.POST, instance=new)
        if form.is_valid():
            form.save()
            return redirect('news-detail', new.id)
    else:
        form = NewForm(instance=new)
    return render(request, 'listings/new_update.html', {'form': form})

def new_delete(request, id):
    new = New.objects.get(id=id)
    if request.method == 'POST':
        new.delete()
        return redirect('news_list')
    return render(request, 'listings/new_delete.html', {'new': new})

def contact(request):
    if request.method == 'POST':
        form= ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["nom"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['mathiasorlando95@gmail.com']
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form': form})

def email_sent(request):
    return render(request, 'listings/email_sent.html')
