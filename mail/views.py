from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Email
from .forms import EmailComposeForm


# Create your views here.


def inbox(request):
    emails = Email.objects.filter(recipient=request.user)
    return render(request, 'index.html', {'emails': emails})


def sent(request):
    sent_emails = Email.objects.filter(sender=request.user)
    return render(request, '', {'sent_emails': sent_emails})


def draft(request):
    draft_emails = Email.objects.filter(sender=request.user, is_draft=True)
    return render(request, '', {'draft_emails': draft_emails})


def archive(request):
    archive_emails = Email.objects.filter(recipient=request.user, is_archived=True)
    return render(request, '', {'archive_emails': archive_emails})


def read_email(request, email_id):
    email = Email.objects.get(email_id)
    return render(request, 'read.html', {'email': email})


@login_required
def compose(request):
    if request.method == 'POST':
        form = EmailComposeForm
    return render(request, 'compose.html')


def read(request):
    return render(request, 'read.html')


def reply(request):
    return render(request, 'reply.html')
