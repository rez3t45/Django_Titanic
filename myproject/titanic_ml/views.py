import os
import joblib
import numpy as np
from django.shortcuts import render
from .forms import PredictionForm

from sklearn.preprocessing import StandardScaler
import pandas as pd

#INCOMPATIBILIDAD DE VERSION SKLEARN
import warnings
from sklearn.exceptions import InconsistentVersionWarning
#END INCOMPATIBILIDAD


warnings.filterwarnings("ignore", category=InconsistentVersionWarning)


def predict_ML(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Load the trained linear regression model
            model_path = os.path.join(os.path.dirname(__file__), 'models', 'Titanic_Knn_Predict_Survival.pkl')
            model = joblib.load(model_path)

            # Extract input data from the form
            new_data = np.array(list(form.cleaned_data.values())).reshape(1, -1)
            #print( 'new_data : ')
            #print( new_data)

            #Transformation Standar scale ----------------------------------------------------------
            norm = StandardScaler()

            data_path = os.path.join(os.path.dirname(__file__), 'models', 'titanic_X_standarSc.csv')
            data = pd.read_csv(data_path,sep=';')
            #data.info()
            

            data_normalizado = norm.fit_transform(data) #Just to FIT

            Xval_normalizado = norm.transform(pd.DataFrame(new_data))

            #End Transformation -----------------------------------------

            # Perform prediction
            predicted_val = model.predict(Xval_normalizado)[0]     
            #print(predicted_val)

            diccionario = {'Si': 1, 'No': 0}
            predicted_ = next((clave for clave, valor in diccionario.items() if valor == predicted_val), None)


            # Prepare the response
            context = {
                'form': form,
                'predicted_': predicted_,
            }
            return render(request, 'index.html', context)
    else:
        form = PredictionForm()

    context = {'form': form}
    return render(request, 'index.html', context)