from evento.models import Notification

def notifications(request):
    if request.user.is_authenticated:
        user_notifications = Notification.objects.filter(user=request.user, is_read=False)
        return {'user_notifications': user_notifications}
    else:
        return {}