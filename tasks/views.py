from django.shortcuts import render

from django.views import View
# Create your views here.

class TaskList(View):
    def get(self, request):
        return render(request, 'task.html')
