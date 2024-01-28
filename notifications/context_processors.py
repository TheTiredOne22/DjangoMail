from .models import Notification


def notification_list(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user, is_read=False).order_by('-timestamp')
        count = notifications.count
        return {'notifications': notifications, 'notifications_count': count}
    return {}
