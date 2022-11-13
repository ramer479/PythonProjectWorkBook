def band_name(city, pet):
    return city + ' ' + pet


if __name__ == '__main__':
    print("Lets get to the game. Band name Generator")
    city = input("Enter the city name: ")
    pet_name = input("Enter your pet's name: ")
    print(band_name(city,pet_name))