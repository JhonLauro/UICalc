from django.shortcuts import render

def calculator(request):
    context = {'result': None, 'a': '', 'b': '', 'op': '+', 'error': ''}

    if request.method == 'POST':
        a = request.POST.get('a', '').strip()
        b = request.POST.get('b', '').strip()
        op = request.POST.get('op', '+')
        context.update({'a': a, 'b': b, 'op': op})

        try:
            x = float(a)
            y = float(b)

            if op == '+':
                res = x + y
            elif op == '-':
                res = x - y
            elif op == '*':
                res = x * y
            elif op == '/':
                if y == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                res = x / y
            else:
                context['error'] = 'Unknown operator.'
                res = None

            context['result'] = res
        except ValueError:
            context['error'] = 'Please enter valid numbers.'
        except ZeroDivisionError as e:
            context['error'] = str(e)

    return render(request, 'calc/index.html', context)