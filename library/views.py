from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import Context
from django.template import RequestContext 
from models import Author
from models import Book
# Create your views here.
def search(request):
    return render(request,'search.html')
def showauthor(request):
    auname = request.GET['qq']
    names = Author.objects.filter(Name = auname)
    if names:
        booklist = Book.objects.filter(AuthorID = names )
    else:
        return render(request,'noauthor.html')
    if  booklist:
        return render(request, 'showauthor.html',{"booklist":booklist,'author_name':auname} )
    else:
         return render(request,'nobook.html', {'author_name':auname} )

def addauthor(request):
    if request.POST:
        post = request.POST
        new_author = Author(
            Name = post["name"],
            Age = post["age"],
            Country = post["country"])
        new_author.save()
    return render_to_response('addauthor.html',context_instance=RequestContext(request))
def authorlist(request):
    author_list = Author.objects.all()
    c = Context({"author_list":author_list,})
    return render_to_response("authorlist.html", c)
def addbook(request):
    auname = request.GET['author_name']
    author = Author.objects.get(Name=auname)
    if request.POST:
        post = request.POST
        author.book_set.create(
        ISBN = post["isbn"],
        Title = post["title"],
        Publisher = post["publisher"],
        PublishDate = post["publishdate"],
        Price = post["price"])
    return render_to_response('addbook.html',context_instance=RequestContext(request))
def booklist(request):
    book_list = Book.objects.all()
    c = Context({"book_list":book_list,})
    return render_to_response("booklist.html", c)
def detail(request,isbnn):
    prebook=Book.objects.get(ISBN=isbnn)
    c=Context({"prebook":prebook,})
    return render_to_response("detail.html", c,)
def delete(request,isbnn):
    prebook=Book.objects.filter(ISBN=isbnn)
    prebook.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
def updata(request,isbnn):
    if request.POST:
        post = request.POST
        pretitle = post["rtitle"]
        prepublisher = post["rpublisher"]
        prepublishDate = post["rpublishdate"]
        preprice=post["rprice"]
        prebook=Book.objects.get(ISBN=isbnn)
        prebook.Title=pretitle
        prebook.Publisher=prepublisher
        prebook.PublishDate=prepublishDate
        prebook.Price=preprice
        prebook.save()
    return render_to_response('updata.html',context_instance=RequestContext(request))