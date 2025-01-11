from django.shortcuts import render, get_object_or_404, redirect
from .models import Review

def review_list(request):
    reviews = Review.objects.all()  # 모든 리뷰를 가져옴
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})

def review_delete(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    return redirect('review_list')

def review_write(request):
    if request.method == "POST":
        Review.objects.create(
            title=request.POST['title'],
            release_year=request.POST['release_year'],
            director=request.POST['director'],
            actors=request.POST['actors'],
            genre=request.POST['genre'],
            rating=request.POST['rating'],
            running_time=request.POST['running_time'],
            content=request.POST['content']
        )
        return redirect('review_list')
    return render(request, 'reviews/review_write.html')

def review_edit(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == "POST":
        review.title = request.POST['title']
        review.release_year = request.POST['release_year']
        review.director = request.POST['director']
        review.actors = request.POST['actors']
        review.genre = request.POST['genre']
        review.rating = request.POST['rating']
        review.running_time = request.POST['running_time']
        review.content = request.POST['content']
        review.save()
        return redirect('review_detail', review_id=review.id)
    return render(request, 'reviews/review_write.html', {'review': review})
