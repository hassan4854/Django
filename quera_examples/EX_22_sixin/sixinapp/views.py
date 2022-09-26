from .models import Musician, Album
from django.views.generic import ListView, DetailView


class MusicianListView(ListView):
    model = Musician
    queryset = Musician.objects.order_by("name")
    paginate_by = 1
    template_name = 'musician_list.html'



class AlbumDetailView(DetailView):
    model = Album
    queryset = Album.objects.filter(num_stars__gte=3)
    template_name = 'album_detail.html'
