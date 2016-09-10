from django.shortcuts import render

from website.forms import SearchForm
from website.util import blast_tool



# Create your views here.


def index(request):
    return render(request, 'website/Index.html')

def about(request):
    return render(request, 'website/Aboutus.html')

def tools(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            target = form['target'].value()
            print(target)
            result = blast_tool.blast_call_text(target)
            re_dict = blast_tool.read_blast_result_text(result)
            print(re_dict)
            return render(request, 'website/Tools.html',{'form':form,'re_dict':re_dict})
    else:
        form = SearchForm()
    return render(request, 'website/Tools.html',{'form':form})

def blogtwo(request):
    return render(request, 'website/Blogtwo.html')


