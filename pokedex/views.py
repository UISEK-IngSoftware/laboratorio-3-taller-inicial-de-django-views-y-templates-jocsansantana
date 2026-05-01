from django.shortcuts import render

# Create your views here.
def index(request):
    pokemons = ['Charizard','Gengar','Squirtle','Mew','Lucario','Charmander','Blaziken','Infernape','Blastoise','Greninja']
    return render(request,'index.html',{'pokemons' : pokemons})
    
def pokemon_details(request,pokemon):
    return render(request,'details.html',{'pokemon' : pokemon})