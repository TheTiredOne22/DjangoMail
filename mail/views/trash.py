from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from mail.models import Email


def trash(request):
    # Filter soft-deleted emails for the current user, whether they were the sender or recipient
    deleted_emails = Email.objects.filter(
        Q(sender=request.user, is_deleted_by_sender=True) |
        Q(recipient=request.user, is_deleted_by_recipient=True)
    ).order_by('-timestamp')
    return render(request, 'mailbox/trash.html', {'deleted_emails': deleted_emails})


# def delete_email(request, slug):
#     if request.method == 'POST':
#         email = get_object_or_404(Email, slug=slug)
#         if request.user == email.sender:
#             email.is_deleted_by_sender = True
#         elif request.user == email.recipient:
#             email.is_deleted_by_recipient = True
#         email.save()
#         messages.success(request, 'Email deleted successfully')
#     return redirect('mail:inbox')
#
#
# def bulk_delete(request):
#     if request.method == 'POST':
#         email_ids = request.POST.getlist('email_ids')
#         emails = Email.objects.filter(id__in=email_ids)
#         for email in emails:
#             if request.user == email.sender:
#                 email.is_deleted_by_sender = True
#             elif request.user == email.recipient:
#                 email.is_deleted_by_recipient = True
#             email.save()
#         messages.success(request, 'Emails deleted successfully.')
#     return redirect('mail:inbox')


#

def delete_email(request, slug):
    """
    View to toggle the deletion status of a specific email.

    Toggles the deletion status of the email with the given slug if the authenticated user is the sender or recipient.

    Args:
        request (HttpRequest): The request object.
        slug (str): The slug of the email to toggle deletion status.

    Returns:
        HttpResponseRedirect: Redirects to the inbox after toggling deletion status.
    """
    # Retrieve the email to toggle deletion status
    email = get_object_or_404(Email, slug=slug)

    # Check if the authenticated user is the sender or recipient of the email
    if request.user == email.sender or request.user == email.recipient:
        # Toggle the deletion status of the email
        email.toggle_deleted()

    # Redirect to the trash page after toggling deletion status
    return redirect('mail:trash')


def bulk_delete(request):
    if request.method == 'POST':
        email_ids = request.POST.getlist('email_ids[]')
        emails = Email.objects.filter(id__in=email_ids)
        for email in emails:
            email.toggle_deleted()

    if request.htmx:
        return render(request, 'mailbox/partials/search-results')
    else:
        return HttpResponse()
