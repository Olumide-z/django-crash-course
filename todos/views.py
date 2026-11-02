from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PersonForm, TodoForm
from .models import Todo, Person

# basic view
# view is a python function that takes a request and returns a response


def hello_world_view(request):
    return HttpResponse("Hello World")


def hello_python(request):
    return HttpResponse("Hello Python")


def hello_html_view(request):
    return render(request, 'todos/hello.html')


def hello_name_html_view(request, name):
    return HttpResponse(f"Hello {name}")


def hello_query(request):
    # /search?query=
    return HttpResponse(f"Your query was {request.GET.get('query')}")


def special_view(request):
    return redirect('hello_html')


def post_example(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']

            return HttpResponse(f'You posted: {name}, {age}')
    else:
        return HttpResponseNotAllowed(['POST'])


def submit_example(request):
    return render(request, 'todos/submit.html')


def submit_django_form(request):
    form = PersonForm()

    return render(request, 'todos/submit_django_form.html', {'form': form})


def template_view(request):
    context = {
        "name": "Mike",
        "age": 30,
        "skills": ["Python", "SQL", "Docker"]
    }

    return render(request, 'todos/template_demo.html', context)


def todos_view(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            todo = form.save()

            return HttpResponse('Todo successfully created!')

    else:
        form = TodoForm()

        todos = Todo.objects.all()

        return render(request, 'todos/todos.html', {'form': form, 'todos': todos})


def person_details(request, person_id):
    person = Person.objects.filter(id=person_id).first()

    return render(request, 'todos/person_details.html', {'person': person})


def delete_todo(request, todo_id):
    todo = Todo.objects.filter(id=todo_id).first()
    todo.delete()
    return HttpResponse("Todo successfully deleted")


def toggle_todo_done(request, todo_id):
    todo = Todo.objects.filter(id=todo_id).first()
    todo.done = not todo.done
    todo.save()
    return HttpResponse("Todo successfully toggled")
