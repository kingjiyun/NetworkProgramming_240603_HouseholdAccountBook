from django.shortcuts import render

# Create your views here.
def show_chart(request):
    context = {}
    return render(request, 'chart_test/chart_view.html', context =context)

