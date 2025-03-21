from django.db import models
from django.utils.timezone import now  # Import 'now' for default timestamp

# Candidate Model
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)  # Optional bio
    photo = models.ImageField(upload_to='candidates/', blank=True, null=True)  # Candidate photo
    votes = models.IntegerField(default=0)  # Vote count

    def __str__(self):
        return f"{self.name} ({self.party})"

# Voter Model
class Voter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Unique email for login
    has_voted = models.BooleanField(default=False)  # Prevents multiple votes

    def __str__(self):
        return self.name

# Vote Model
class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)  # Allows multiple elections
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)  # Set default to current time

    def __str__(self):
        return f"{self.voter.name} voted for {self.candidate.name}"
