from django.shortcuts import render
from django.views.generic import TemplateView

class Index(TemplateView):
    template = "Index.html"

    def get(self, request):
        return render(request, self.template, {})
