from django.shortcuts import render
from django.http import HttpResponse
import random
import string

def menu(request):
    return render(request, 'passwordapp/menu.html')

def calculate_password_strength(password):
    lowercas = uppercas = splchar = num = wsp = 0
    for i in password:
        if i in string.ascii_lowercase:
            lowercas += 1
        elif i in string.ascii_uppercase:
            uppercas += 1
        elif i in string.digits:
            num += 1
        elif i in " ":
            wsp += 1
        else:
            splchar += 1
    strength_levels = [lowercas, uppercas, num, wsp, splchar]
    strength = len([i for i in strength_levels if i > 0])
    
    if strength == 1:
        strength_score = 1
        strength_message = "Not recommendable"
        strength_color = "bg-danger"
    elif strength == 2:
        strength_score = 2
        strength_message = "Poor"
        strength_color = "bg-warning"
    elif strength == 3:
        strength_score = 3
        strength_message = "Average"
        strength_color = "bg-info"
    elif strength == 4:
        strength_score = 4
        strength_message = "Good"
        strength_color = "bg-primary"
    elif strength == 5:
        strength_score = 5
        strength_message = "Excellent"
        strength_color = "bg-success"
    
    return {
        'strength_score': strength_score,
        'strength_message': strength_message,
        'strength_color': strength_color,
        'lowercas': lowercas,
        'uppercas': uppercas,
        'num': num,
        'wsp': wsp,
        'splchar': splchar
    }

def password_strength(request):
    if request.method == 'POST':
        password = request.POST.get('password', '')
        strength_data = calculate_password_strength(password)
        context = {
            'password': password,
            'generated': request.POST.get('generated', False),
            **strength_data,
        }
        return render(request, 'passwordapp/password_strength.html', context)
    return render(request, 'passwordapp/password_strength.html')

def password_generator(request):
    if request.method == 'POST':
        length = int(request.POST.get('length'))
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
        
        while True:
            password = ''.join(random.choice(chars) for _ in range(length))
            strength_data = calculate_password_strength(password)
            if strength_data['strength_score'] >= 4:
                break
        
        context = {'password': password}
        return render(request, 'passwordapp/password_generator.html', context)
    return render(request, 'passwordapp/password_generator.html')

def download_strength_report(request):
    password = request.POST.get('password')
    lowercas = request.POST.get('lowercas')
    uppercas = request.POST.get('uppercas')
    num = request.POST.get('num')
    wsp = request.POST.get('wsp')
    splchar = request.POST.get('splchar')
    strength_message = request.POST.get('strength_message')
    strength_score = request.POST.get('strength_score')

    report_content = f"""
    Password Report:
    Your password: {password}
    Lowercase letters: {lowercas}
    Uppercase letters: {uppercas}
    Numbers: {num}
    Blank spaces: {wsp}
    Special characters: {splchar}
    Strength: {strength_message} ({strength_score}/5)
    """

    response = HttpResponse(report_content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="password_strength_report.txt"'
    return response

def download_generated_password(request):
    password = request.POST.get('password')
    response = HttpResponse(password, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="generated_password.txt"'
    return response

def check_generated_password_strength(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        request.POST = request.POST.copy()  # Allow modification of POST data
        request.POST['generated'] = True
        return password_strength(request)

def password_tips(request):
    return render(request, 'passwordapp/password_tips.html')