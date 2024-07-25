from django.shortcuts import render

def home(request):
    context = {
        'organization': 'aut0b0ts',
        'about_containerization': 'Containerization allows applications to be packaged with all necessary dependencies and run consistently across different environments. It ensures reliability, scalability, and efficiency in deploying applications.',
        'social_links': [
            {'name': 'GitHub', 'url': 'https://github.com/kanonkartik', 'icon': 'https://image.flaticon.com/icons/png/512/25/25231.png'},
            {'name': 'LinkedIn', 'url': 'https://linkedin.com/in/kanonkartik', 'icon': 'https://image.flaticon.com/icons/png/512/174/174857.png'}
        ]
    }
    return render(request, 'home.html', context)
