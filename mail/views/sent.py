from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from mail.models import Email
from mail.utils import filter_emails


@login_required()
def sent(request):
    """
    View function for displaying the sent emails of the logged-in user.
    """

    # Retrieve sent emails for the current user
    emails = Email.objects.filter(sender=request.user).select_related('sender', 'recipient').prefetch_related(
        'parent_email').order_by('-timestamp')
    search_query = request.GET.get('q')
    sent_emails = filter_emails(emails, search_query)

    return render(request, 'mailbox/sent.html', {'sent_emails': sent_emails})
