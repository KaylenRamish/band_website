# band/views.py
from django.shortcuts import render, redirect
from .models import Album, Song, SongVote

def home(request):
    """
    Render the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered home page template.
    """
    return render(request, 'home.html')

def about(request):
    """
    Render the about page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered about page template.
    """
    return render(request, 'about.html')

def music(request):
    """
    Render the music page with a list of songs. Handle song voting.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered music page template with song list and voting functionality.
    """
    songs = Song.objects.all()

    if request.method == 'POST':
        vote = request.POST.get('vote')
        if vote == 'song1' or vote == 'song2':
            song_vote = SongVote.objects.filter(song_name=vote).first()
            if song_vote:
                song_vote.votes += 1
                song_vote.save()
            else:
                SongVote.objects.create(song_name=vote, votes=1)
            return redirect('music')

    return render(request, 'music.html', {'songs': songs})

def poll_results(request):
    """
    Render the poll results page with the results of song voting.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered poll results page template with song voting results.
    """
    songs = Song.objects.all()
    total_votes = sum(song.total_votes for song in songs)

    if total_votes > 0:
        for song in songs:
            song.percentage = (song.total_votes / total_votes) * 100
    else:
        # Avoid division by zero if there are no votes yet.
        for song in songs:
            song.percentage = 0

    context = {
        'songs': songs,
        'total_votes': total_votes,
    }
    return render(request, 'poll_results.html', context)
