# pages/views.py
from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
import pickle
import sklearn # You must perform a pip install.
import pandas as pd



def homePageView(request):
    return render(request, 'home.html', {
        'mynumbers':[1,2,3,4,5,6,],
        'firstName': 'Fonse',
        'lastName': 'Clarito'
    })

def fonsePageView(request):
    return render(request, 'fonse.html')

def aboutPageView(request):
    return render(request, 'about.html')


def homePost(request):
    # Use request object to extract choice.

    choice = -999
    gmat = -999

    try:
        # Extract value from request object by control name.
        currentChoice = request.POST['choice']
        gmatStr = request.POST['gmat']

        # Crude debugging effort.
        print("*** Years work experience: " + str(currentChoice))
        choice = int(currentChoice)
        gmat = float(gmatStr)
    # Enters 'except' block if integer cannot be created.
    except:
        return render(request, 'home.html', {
            'errorMessage': '*** The data submitted is invalid. Please try again.',
            'mynumbers': [1, 2, 3, 4, 5, 6, ]})
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', kwargs={'choice': choice, 'gmat': gmat}, ))


def results(request, choice, gmat):
    print("*** Inside reults()")
    # load saved model
    with open(f'{BASE_DIR}/pkl', 'rb') as f:
        loadedModel = pickle.load(f)

    # Create a single prediction.
    singleSampleDf = pd.DataFrame(columns=['gmat', 'work_experience'])

    workExperience = float(choice)
    print("*** GMAT Score: " + str(gmat))
    print("*** Years experience: " + str(workExperience))
    singleSampleDf = singleSampleDf.append({'gmat':gmat,
                                            'work_experience':workExperience},
                                        ignore_index=True)

    singlePrediction = loadedModel.predict(singleSampleDf)

    print("Single prediction: " + str(singlePrediction))

    return render(request, 'results.html', {'choice': workExperience, 'gmat':gmat,
                'prediction':singlePrediction})

