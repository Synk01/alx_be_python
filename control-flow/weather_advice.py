
# 1. Prompt User for Weather Input:
weather_input = input("What's the weather like today? (sunny/rainy/cold): ")

# Initialize response variable
response = "" 

# Check the value of the weather_input
if weather_input == "sunny":
    response = "Wear a t-shirt and sunglasses."
elif weather_input == "rainy":
    response = "Don't forget your umbrella and a raincoat."
elif weather_input == "cold":
    response = "Make sure to wear a warm coat and a scarf."
else:
    response = "Sorry, I don't have recommendations for this weather."

# Print the final response
print(response)

