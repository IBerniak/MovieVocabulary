from django.shortcuts import render, redirect, get_object_or_404
from .forms import SearchingForm

def searching(request):
    if request.method == "POST":
        form = SearchingForm(request.POST)
        if form.is_valid():
            search = form.save(commit=False)
            return redirect('search_response', pk=search.pk)
    else:
        form = SearchingForm()

    return render(request, 'sub_analyze/searching.html', {'form':form})

def search_response(request, pk):
    movie = pk
    return render(request, 'sub_analyze/search_response.html', {'movie': movie})
