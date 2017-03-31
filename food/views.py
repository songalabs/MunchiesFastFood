from django.shortcuts import render

def index(request):
	return render(request, 'munchiesfastfood/home.html', {'drinks':['Pineapple Juice','Green Juice','Soft Drinks','Carlo Rosee Drinks'], 'dishes':['Beef Steak','Tomato with Chicken','Sausages from Italy','Beef Grilled']})
