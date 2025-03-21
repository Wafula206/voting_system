from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F
from .models import Candidate, Voter, Vote
from django.core.exceptions import ObjectDoesNotExist

def vote(request):
    candidates = Candidate.objects.all()  # Fetch all candidates

    if request.method == 'POST':
        voter_email = request.POST.get('email', '').strip()
        candidate_id = request.POST.get('candidate_id', '').strip()

        # Validate form data
        if not voter_email or not candidate_id:
            return render(request, 'voting_app/vote_page.html', {
                'candidates': candidates,
                'error': 'Please provide your email and select a candidate.'
            })

        try:
            candidate_id = int(candidate_id)
        except ValueError:
            return render(request, 'voting_app/vote_page.html', {
                'candidates': candidates,
                'error': 'Invalid candidate selection.'
            })

        try:
            voter = Voter.objects.get(email=voter_email)
        except ObjectDoesNotExist:
            return render(request, 'voting_app/vote_page.html', {
                'candidates': candidates,
                'error': 'Voter not found. Please register first.'
            })

        if Vote.objects.filter(voter=voter).exists():
            return render(request, 'voting_app/vote_page.html', {
                'candidates': candidates,
                'error': 'You have already voted.'
            })

        candidate = get_object_or_404(Candidate, pk=candidate_id)

        # Register the vote
        Vote.objects.create(voter=voter, candidate=candidate)
        voter.has_voted = True
        voter.save()
        Candidate.objects.filter(id=candidate_id).update(votes=F('votes') + 1)

        return redirect('vote_success')  # ✅ Ensure 'vote_success' is in urls.py

    # ✅ Handle GET requests properly
    return render(request, 'voting_app/vote_page.html', {'candidates': candidates})

# ✅ SUCCESS PAGE FUNCTION
def vote_success(request):
    return render(request, 'voting_app/vote_success.html')
