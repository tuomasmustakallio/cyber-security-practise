from django.http import HttpResponse

# Create your views here.

def addPageView(request):
    first = request.GET.get('first')
    second = request.GET.get('second')

    # Convert the values to integers
    first = int(first)
    second = int(second)

    # Calculate the sum
    result = first + second

    # Return the result as a response to the user
    return HttpResponse(str(result))


def multiplyPageView(request):
    f = request.GET.get('first')
    s = request.GET.get('second')

    # Convert the values to integers
    f = int(f)
    s = int(s)

    # Calculate the sum
    r = f * s

    # Return the result as a response to the user
    return HttpResponse(str(r))