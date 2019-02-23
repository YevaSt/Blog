from django.shortcuts import render
from django.views.generic import TemplateView,DetailView

from my_blog.forms import AddCommenr
from my_blog.models import Post
# Create your views here.
class IndexView(TemplateView):
    template_name="index.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context
class PostDetailView(DetailView):
        template_name= "post.html"
        model = Post
        def get_context_data(self,**kwargs):
            context = super().get_context_data(**kwargs)
            context["form"]= AddCommenr()
            return context
        def post(self, request, pk):
            form = AddCommenr(data= request.POST)
            self.object=self.get_object()
            context= self.get_context_data()
            if form.is_valid():
                comment= form.save(commit=False)
                comment.post=self.object
                comment.save()
                context["form"]= AddCommenr()
                return self.render_to_response(context)
            else:
                context['form']= form
                return self.render_to_response(context)
            