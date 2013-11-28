from django.http.response import HttpResponse

# Create your views here.

def mainview(request):
    return HttpResponse("""
<!DOCTYPE html>
<html>
<head>
    <title>
        US to Canadian currency converter
    </title>
</head>
<body>
    <h1>US to Canadian currency converter</h1>
    <p>This converter will give you some perspective on how much the USD has been devalued
    over the years.</p>

    <form action="doconversion">
        <p> USD:
            <input type="number" name="USD">
        </p>
        <input type="submit" value="Convert">
    </form>
</body>
</html>
    """)

def doconvert(request):
    # input string
    instring = request.GET["USD"]

    # check the input
    if not instring.isdigit():
        return HttpResponse("It is forbidden to  process a non-numeric input!")

    # convert to a number
    f = eval(instring)

    # apply the formula
    ca = f * 1.05

    # return the result
    return HttpResponse("Result is: ${0:0.2f} Canadian".format(ca))
