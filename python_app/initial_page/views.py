from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from . import forms, models

# Create your views here.
#start page
def hello_template(request):
    return render(request, 'init_start.html')

#get post number
"""
def get_post_query(request):
    d = {
        'your_postnumber': request.GET.get('your_postnumber')
    }
    return render(request, 'init_postnumber.html', d)
"""

def get_post_query(request):
    form = forms.PostnumberForm(request.POST or None)
    if form.is_valid():
        models.Customer.objects.create(**form.cleaned_data)
        return redirect('initial:get_post_query')

    d = {
        'form': form,
        'post_number_qs': models.Customer.objects.all().order_by('-id')
    }
    return render(request, 'init_postnumber.html', d)


#get work time
"""
def get_worktime(request):
    d = {
        'worktime_start': request.GET.get('worktime_start'),
        'worktime_end': request.GET.get('worktime_end')
    }
    return render(request, 'init_worktime.html', d)
"""
def get_worktime(request):
    form = forms.WorktimeForm(request.POST or None)
    if form.is_valid():
        models.Customer.objects.create(**form.cleaned_data)
        return redirect('initial:get_post_query')
    d = {
        'form': form,
    }
    return render(request, 'init_worktime.html', d)

#get laundry scale
def get_laundryscale(request):
    d = {
        'scale': request.GET.get('scale')
    }
    return render(request, 'init_laundryscale.html', d)

#end setting
def init_end_page(request):
    return render(request, 'init_end.html')

#usual
def usual_page(request):
    #graph
    import numpy as np
    import matplotlib
    matplotlib.use('Agg') # -----(1)
    import matplotlib.pyplot as plt

# y = f(x)
    x = np.linspace(-np.pi, np.pi)
    y1 = np.sin(x)+np.cos(x)
    y2 = np.cos(x)

# figure
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

# plot
    ax.plot(x, y1, linestyle='--', color='b', label='y = sin(x)')
    ax.plot(x, y2, linestyle='-', color='#e46409', label='y = cos(x)')

# x axis
    plt.xlim([-np.pi, np.pi])
    ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    ax.set_xticklabels(['-pi', '-pi/2', '0', 'pi/2', 'pi'])
    ax.set_xlabel('x')

# y axis
    plt.ylim([-1.2, 1.2])
    ax.set_yticks([-1, -0.5, 0, 0.5, 1])
    ax.set_ylabel('y')

# legend and title
    ax.legend(loc='best')
    ax.set_title('Plot of sine and cosine')


#スクレイピングのデータとdatabaseのデータより提案の処理、グラフをpng変換
# save as png
    plt.savefig('./static/figure.png')

    d = {
        'is_visible':False,
    }
    return render(request, 'usual.html', d)

#plan today page
def today_plan(request):
    #スクレイピングのデータとdatabaseのデータより提案の処理、グラフをpng変換


    d = {
        'time':"8:00 ~ 10:00"
    }
    return render(request, 'today_plan.html',d)

#plan week page
def weekly_plan(request):
    #スクレイピングのデータとdatabaseのデータより提案の処理、グラフをpng変換


    d = {
        'mon_plan':["8:00 ~ 9:00", "9:00 ~ 10:00"],
        'tue_plan':["11:00 ~ 14:00"],
        'wed_plan':["8:00 ~ 9:00", "9:00 ~ 10:00", "11:00 ~ 12:00"],
        'thr_plan':["8:00 ~ 9:00"],
        'fri_plan':["8:00 ~ 9:00", "9:00 ~ 10:00", "16:00 ~ 17:00", "20:00 ~ 21:00", "22:00 ~ 24:00"],
        'sat_plan':["8:00 ~ 9:00", "10:00 ~ 11:00"],
        'sun_plan':["8:00 ~ 24:00"],
    }
    return render(request, 'week_plan.html',d)