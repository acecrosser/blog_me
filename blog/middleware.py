

def anonymous_session(get_response):
    def middleware(request):
        if not request.user.is_authenticated and not request.session.session_key:
            request.session.save()
        response = get_response(request)
        return response
    return middleware
