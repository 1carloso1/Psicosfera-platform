from evento.models import Notification

def notifications(request):
    if request.user.is_authenticated:
        notificaciones_no_leidas = 0
        user_notifications = Notification.objects.filter(user=request.user).order_by('-timestamp')
        notificaciones_leidas = []
        for notificacion in user_notifications:
            if not notificacion.is_read:
                notificaciones_no_leidas += 1
            else:
                notificaciones_leidas.append(notificacion)
        return {'user_notifications': user_notifications, 'notificacionesNoLeidas': notificaciones_no_leidas,'notificacionesLeidas': notificaciones_leidas}
    else:
        return {}