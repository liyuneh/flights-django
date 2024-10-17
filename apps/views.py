from django.http import  Http404,HttpResponseRedirect

from django.shortcuts import render
from django.urls import reverse

from .models import Airport, Flight, Passenger,Food


def index(request):
     context={
         "flight":Flight.objects.all()
     }
     return render(request, 'apps/index.html', context)


def flight(request, flight_id):
     try:
        flight = Flight.objects.get(pk=flight_id)
     
     except Flight.DoesNotExist:
        raise Http404("Flight does not exist")
     context = {
          'flight':flight,
          'passengers':flight.passengers.all(),
          "non_passengers":Passenger.objects.exclude(flights=flight).all(),
          "food":flight.food.all(),
          "non_food":Food.objects.exclude(flights=flight).all(),
     }
     return render(request, 'apps/flight.html', context)

def book(request, flight_id):
    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)
    except KeyError:
        return render(request, 'apps/error.html', {'Message': "No Selection."})
    except Flight.DoesNotExist:
        return render(request, 'apps/error.html', {'Message': "No flight."})
    except Passenger.DoesNotExist:
        return render(request, 'apps/error.html', {'Message': "No passenger."})
    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse('flight',args=(flight.id,) )) 

def food(request, flight_id):
    if request.method == 'POST':
        print("called POST method")
        try:
            food_id = int(request.POST["food"])
            food = Food.objects.get(pk=food_id)
            flight = Flight.objects.get(pk=flight_id)
            print( "info:", food_id, food, flight)
            # Associate the food item with the flight
            food.flights.add(flight)

        except KeyError  as e:
            print("KeyError:", e)
            return render(request, 'apps/error.html', {'Message': "No food selection made."})
        except Food.DoesNotExist  as e:
            print("DoesNotExist:", e)
            return render(request, 'apps/error.html', {'Message': "No food item found."})
        except Flight.DoesNotExist  as e:
            print("error3:", e)
            
            return render(request, 'apps/error.html', {'Message': "No flight found."})
        except Exception as e:
            print("error4:", e)
            
            return render(request, 'apps/error.html', {'Message': str(e)})

        return HttpResponseRedirect(reverse('flight', args=(flight.id,)))

    # If the request method is not POST
    else:
        return render(request, 'apps/error.html', {'Message': "Invalid request method."})