from django.contrib.auth.decorators import user_passes_test
from django.http import request
from django.shortcuts import render
from .models import tweet
from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class TweetListView(LoginRequiredMixin,ListView):
    model = tweet
    template_name = 'feed/home.html'
    ordering = ['-dateTime']

class TweetCreateView(LoginRequiredMixin,CreateView):
    model = tweet
 
    fields = ['tweets']
    success_url='/'

    def form_valid(self, form):
        form.instance.usrName = self.request.user
        return super().form_valid(form)

class TweetUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = tweet

    fields = ['tweets']
    success_url='/'

    def form_valid(self, form):
        form.instance.usrName = self.request.user
        return super().form_valid(form)   

    def test_func(self):
        tweet = self.get_object()
        if(self.request.user == tweet.usrName):
            return True 
        return False          

class TweetDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = tweet


    success_url='/'


    def test_func(self):
        tweet = self.get_object()
        if(self.request.user == tweet.usrName):
            return True 
        return False          

