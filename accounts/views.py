from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from .forms import *
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import (CreateView, TemplateView,DetailView, UpdateView, ListView, FormView, DeleteView)
from django.contrib.auth import get_user_model
# from accounts.models import User
# from LibTrade.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django import forms
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
import datetime
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render
from django.template.defaultfilters import slugify
from accounts.models import Book, Trade
from . forms import BookCreateForm
from taggit.models import Tag

class TagListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'accounts/book_list.html'

def TradeDeleteView(request,idd):
    tradeobj = get_object_or_404(Trade, trade_id=idd)
    if request.method == 'POST':
        tradeobj.delete()
        return redirect('accounts:booklist')
    return render(request, 'accounts/trade_delete_form.html', {
        'book':tradeobj.book,
    })

def TradeApproveView(request,id):
    tradeobj = get_object_or_404(Trade, trade_id=id)
    if request.method == 'POST':
        thebook = get_object_or_404(Book, slug=tradeobj.book.slug)
        thebook.keeper = tradeobj.requestor
        thebook.save()
        tradeobj.delete()
        return redirect('accounts:booklist')
    return render(request, 'accounts/trade_approve_form.html', {
        'book':tradeobj.book,
    })

def TradeView(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if not request.user.username:
        return redirect('accounts:booklist')
    requestor = request.user
    approver = book.owner
    if request.method == 'POST':
        trade = Trade()
        trade.book = book
        trade.requestor = requestor
        trade.approver = approver
        gots = Trade.objects.all().filter(
            book = book,
            approver = approver,
        )
        flag = False
        #wrong transaction conditions
        for got in gots:
            if got.requestor == trade.requestor:
                flag = True
        if trade.requestor == trade.approver:
                flag = True
        if not flag:
            trade.save()
        return redirect('landing')
    return render(request, 'accounts/tradecreateform.html', {
        'book':book,
    })

@method_decorator([login_required], name='dispatch')
class BookCreateView(CreateView):
    form_class = BookCreateForm
    template_name = 'accounts/book_add_form.html'
    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.owner = self.request.user
        quiz.keeper = quiz.owner
        quiz.slug = slugify(quiz.name)
        if(quiz.owner.is_librarian):
            membership_req = True
        quiz.save()
        form.save_m2m()
        messages.success(self.request, 'The Book was a with success!')
        return redirect('landing')

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'accounts/book_detail.html'

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'accounts/book_list.html'



def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    books = Book.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'books':books,
    }
    return render(request, 'accounts/book_taglist.html', context)


@method_decorator([login_required], name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    context_object_name = 'book'
    template_name = 'accounts/book_delete_confirm.html'
    success_url = reverse_lazy('accounts:booklist')
    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        if( book.owner == self.request.user ):
            return super().delete(request, *args, **kwargs)
    def get_queryset(self):
        return self.request.user.owned_books.all()

    # def get_queryset(self l- ):
    #     student = self.request.user.student
    #     student_interests = student.interests.values_list('pk', flat=True)
    #     taken_quizzes = student.quizzes.values_list('pk', flat=True)
    #     queryset = Quiz.objects.filter(subject__in=student_interests) \
    #         .exclude(pk__in=taken_quizzes) \
    #         .annotate(questions_count=Count('questions')) \
    #         .filter(questions_count__gt=0)
    #     return queryset
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from .forms import *
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import (CreateView, TemplateView,DetailView, UpdateView, ListView, FormView, DeleteView)
from django.contrib.auth import get_user_model
# from accounts.models import User
# from LibTrade.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django import forms
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
import datetime
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render
from django.template.defaultfilters import slugify
from accounts.models import Book, Trade
from . forms import BookCreateForm
from taggit.models import Tag

class TagListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'accounts/book_list.html'

def TradeDeleteView(request,idd):
    tradeobj = get_object_or_404(Trade, trade_id=idd)
    if request.method == 'POST':
        tradeobj.delete()
        return redirect('accounts:booklist')
    return render(request, 'accounts/trade_delete_form.html', {
        'book':tradeobj.book,
    })

def TradeApproveView(request,id):
    tradeobj = get_object_or_404(Trade, trade_id=id)
    if request.method == 'POST':
        thebook = get_object_or_404(Book, slug=tradeobj.book.slug)
        thebook.keeper = tradeobj.requestor
        thebook.save()
        tradeobj.delete()
        return redirect('accounts:booklist')
    return render(request, 'accounts/trade_approve_form.html', {
        'book':tradeobj.book,
    })

def TradeView(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if not request.user.username:
        return redirect('accounts:booklist')
    requestor = request.user
    approver = book.owner
    if request.method == 'POST':
        trade = Trade()
        trade.book = book
        trade.requestor = requestor
        trade.approver = approver
        gots = Trade.objects.all().filter(
            book = book,
            approver = approver,
        )
        flag = False
        #wrong transaction conditions
        for got in gots:
            if got.requestor == trade.requestor:
                flag = True
        if trade.requestor == trade.approver:
                flag = True
        if not flag:
            trade.save()
        return redirect('landing')
    return render(request, 'accounts/tradecreateform.html', {
        'book':book,
    })

@method_decorator([login_required], name='dispatch')
class BookCreateView(CreateView):
    form_class = BookCreateForm
    template_name = 'accounts/book_add_form.html'
    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.owner = self.request.user
        quiz.keeper = quiz.owner
        quiz.slug = slugify(quiz.name)
        if(quiz.owner.is_librarian):
            membership_req = True
        quiz.save()
        form.save_m2m()
        messages.success(self.request, 'The Book was a with success!')
        return redirect('landing')

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'accounts/book_detail.html'

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'accounts/book_list.html'



def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    books = Book.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'books':books,
    }
    return render(request, 'accounts/book_taglist.html', context)


@method_decorator([login_required], name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    context_object_name = 'book'
    template_name = 'accounts/book_delete_confirm.html'
    success_url = reverse_lazy('accounts:booklist')
    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        if( book.owner == self.request.user ):
            return super().delete(request, *args, **kwargs)
    def get_queryset(self):
        return self.request.user.owned_books.all()

    # def get_queryset(self l- ):
    #     student = self.request.user.student
    #     student_interests = student.interests.values_list('pk', flat=True)
    #     taken_quizzes = student.quizzes.values_list('pk', flat=True)
    #     queryset = Quiz.objects.filter(subject__in=student_interests) \
    #         .exclude(pk__in=taken_quizzes) \
    #         .annotate(questions_count=Count('questions')) \
    #         .filter(questions_count__gt=0)
    #     return queryset
