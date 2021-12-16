from django.shortcuts import render, HttpResponse


# html_base = """
#     <h1>Mi web personal<h1/>
#     <ul>
#         <li><a href="/">Portada</a></li>
#         <li><a href="/about-me/">Acerca de</a></li>
#         <li><a href="/briefcase/">Portafolio</a></li>
#         <li><a href="/contact/">Contacto</a></li>
#     <ul/>
# """

def home(request):
    # return HttpResponse(html_base + """
    #     <h2>Acerca de</h2>
    #     <p>Me llamo Franco y soy sentipensante</p>
    # """)
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')
