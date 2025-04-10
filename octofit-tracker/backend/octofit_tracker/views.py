from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout
from django.http import JsonResponse

def api_root(request):
    codespace_url = "https://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev"
    local_url = "http://localhost:8000"
    # return JsonResponse({
    #     "message": "Welcome to the Octofit API!",
    #     "codespace_url": codespace_url,
    #     "local_url": local_url
    # })
    if request.method == 'POST':
        return Response({"message": "POST request received"}, status=status.HTTP_201_CREATED)
    
    return Response({
            'users': local_url + 'api/users/?format=api',
            'teams': local_url + 'api/teams/?format=api',
            'activities': local_url + 'api/activities/?format=api',
            'leaderboard': local_url + 'api/leaderboard/?format=api',
            'workouts': local_url + 'api/workouts/?format=api'
        })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer