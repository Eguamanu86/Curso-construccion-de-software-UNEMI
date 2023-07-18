from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

class LoginPageView(TemplateView):
    template_name = 'seguridad/login.html'

    def post(self, request, *args, **kwargs):
        status_code = None
        data = {'resp': False, 'error': None}
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    status_code = 200
                    data['resp'] = True
                else:
                    status_code = 400
                    data['error'] = 'Login Fallido!, usuario no esta habilitado'
            else:
                status_code = 400
                data['error'] = 'Login Fallido!, credenciales incorrectas.'

        except Exception as e:
            data['error'] = 'Error internal Server'
            status_code = 500

        return JsonResponse(data, status=status_code)
