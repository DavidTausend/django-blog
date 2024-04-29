from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Event


class EventsList(generic.ListView):


    model = Event
    template_name = "index.html"
    paginate_by = 12

def post_detail(request, slug):

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
         "coder": "Matt Rudge"},
    )


def event_detail(request, event_id):
    
    queryset = Event.objects.all()
    event = get_object_or_404(queryset, event_id=event_id)

    return render(
        request,
        "events/event_detail.html",
        {"event": event}
    )