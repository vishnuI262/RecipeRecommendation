import requests
from django.shortcuts import render

def chatbot_view(request):
    user_message = request.GET.get('message', '')
    api_key = '29cb7c2da2a844298766c3cf172f0b52'  # Your Spoonacular API key

    # Search for recipes based on the user message
    search_url = f"https://api.spoonacular.com/recipes/complexSearch?query={user_message}&apiKey={api_key}&number=1"
    search_response = requests.get(search_url)
    search_data = search_response.json()

    # Debugging: Print the search response to the console
    print("Search API Response:", search_data)

    recipes = search_data.get('results', [])

    if recipes:
        # Get the first recipe ID
        recipe_id = recipes[0].get('id')
        if recipe_id:
            # Fetch detailed recipe information
            detail_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}"
            detail_response = requests.get(detail_url)
            detail_data = detail_response.json()

            # Debugging: Print the detailed recipe response to the console
            print("Detail API Response:", detail_data)

            recipe_title = detail_data.get('title', 'No title available')
            recipe_image = detail_data.get('image', '')
            recipe_source_url = detail_data.get('sourceUrl', 'No source URL available')
            recipe_instructions = detail_data.get('instructions', 'No instructions available')

            image_tag = f"<img src='{recipe_image}' alt='{recipe_title}' style='width:300px;'>" if recipe_image else 'No image available'

            response_message = (
                f"Recipe: {recipe_title}<br>"
                f"Source: <a href='{recipe_source_url}' target='_blank'>{recipe_source_url}</a><br>"
                f"Image: {image_tag}<br>"
                f"Instructions: <br>{recipe_instructions}"
            )
        else:
            response_message = "Sorry, I couldn't find detailed information for this recipe."
    else:
        response_message = "Sorry, I couldn't find any recipes for that."

    return render(request, 'chatbot.html', {'response': response_message})
