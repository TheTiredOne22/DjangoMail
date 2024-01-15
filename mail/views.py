from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Email
from .forms import EmailComposeForm
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.

@login_required()
def inbox(request):
    emails = Email.objects.filter(recipients=request.user)
    return render(request, 'mailbox/index.html', {'emails': emails})


def sent(request):
    sent_emails = Email.objects.filter(sender=request.user)
    return render(request, 'mailbox/sent.html', {'sent_emails': sent_emails})


def draft(request):
    draft_emails = Email.objects.filter(sender=request.user, is_draft=True)
    return render(request, 'mailbox/draft.html', {'draft_emails': draft_emails})


def archive(request):
    archive_emails = Email.objects.filter(recipient=request.user, is_archived=True)
    return render(request, 'mailbox/archive.html', {'archive_emails': archive_emails})


def read_email(request, slug):
    email = get_object_or_404(Email, slug=slug)
    return render(request, 'mailbox/read.html', {'email': email})


@login_required
def compose_email(request):
    if request.method == 'POST':
        form = EmailComposeForm(request.POST)
        if form.is_valid():
            sender = request.user
            recipients = form.cleaned_data['recipients']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']

            # Create the email instance
            email = Email.objects.create(sender=sender, subject=subject, body=body)
            email.recipients.set(recipients)
            return redirect('mail:read', slug=email.slug)
    else:
        form = EmailComposeForm()
    return render(request, 'mailbox/compose.html', {'form': form})

# def read(request):
#     return render(request, 'read.html')
#
#
# def reply(request):
#     return render(request, 'reply.html')
