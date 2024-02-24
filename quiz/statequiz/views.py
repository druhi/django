from django.shortcuts import render, HttpResponse
import random

# Create your views here.
states1 = {
  "Uttar Pradesh": "Lucknow",
  "Arunachal Pradesh": "Itanagar",
  "Madhya Pradesh": "Bhopal",
  "Uttrakhand": "Dehradun",
  "Maharastra": "Mumbai",
  "Tamilnadu": "Chennai"
}

# res = key, val = random.choice(list(states1.items()))

def home(request):
        #  return HttpResponse('<h1>hi Druhi</h1>')
        global res
        global key
        global val
        res = key, val = random.choice(list(states1.items()))
        return render(request, "home.html", {'key' : key})


def result(request):
        no2 = (request.GET.get("Ans"))
        a = no2.strip().lower()

        if key == "Arunachal Pradesh" and a == "itanagar":
         b = "correct"
         return render(request, "result.html", {'answer' : b})
        elif key == "Uttar Pradesh" and a == "lucknow":
         b = "correct"
         return render(request, "result.html", {'answer' : b})
        elif key == "Madhya Pradesh" and a == "bhopal":
         b = "correct"
         return render(request, "result.html", {'answer' : b})
        elif key == "Maharastra" and a == "mmumbai":
         b = "correct"
         return render(request, "result.html", {'answer' : b})
        elif key == "Uttrakhand" and a == "dehradun":
         b = "correct"
         return render(request, "result.html", {'answer' : b})
        elif key == "Tamilnadu" and a == "chennai":
         b = "correct"
         return render(request, "result.html", {'answer' : b})
        else:
         b = (f"incorrect, Ans is {val}")
         return render(request, "result.html", {'answer' : b})