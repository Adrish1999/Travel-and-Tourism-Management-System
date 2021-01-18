from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render , get_object_or_404 , redirect
from django.views.generic import ListView , DetailView , View
from django.utils import timezone
from .models import Item

class HomeView(ListView):
    model = Item
    template_name = "index.html"