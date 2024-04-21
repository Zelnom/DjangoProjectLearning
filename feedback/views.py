from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from feedback.forms import FeedbackForm, FeedbackUpdateForm
from feedback.models import Feedback


class FeedbackCreateView(LoginRequiredMixin, CreateView):
    template_name = "feedback/create_feedback.html"
    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy("create-feedback")


class FeedbackListView(LoginRequiredMixin, ListView):
    template_name = "feedback/list_of_feedbacks.html"
    model = Feedback
    context_object_name = "all_feedbacks"


class FeedbackUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "feedback/update_feedback.html"
    model = Feedback
    form_class = FeedbackUpdateForm
    success_url = reverse_lazy("list-of-feedbacks")


class FeedbackDetailView(LoginRequiredMixin, DetailView):
    template_name = "feedback/details_feedback.html"
    model = Feedback


class FeedbackDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "feedback/delete_feedback.html"
    model = Feedback
    success_url = reverse_lazy("list-of-feedbacks")
