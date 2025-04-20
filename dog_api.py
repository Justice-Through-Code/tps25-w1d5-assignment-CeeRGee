import requests

def get_all_breeds():
    """GET request to fetch all dog breeds."""
    try:
        response = requests.get("https://dog.ceo/api/breeds/list/all")
        response.raise_for_status()
        data = response.json()
        return data["message"]
    except requests.exceptions.RequestException:
        print("Error: Could not fetch breed list from API.")
        return {}

def get_random_image(breed):
    """GET request to fetch a random image from a breed."""
    try:
        response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
        response.raise_for_status()
        data = response.json()
        if data["status"] == "success":
            return data["message"]
        else:
            return f"Error: Could not get image for breed '{breed}'"
    except requests.exceptions.RequestException:
        return "Error: Could not connect to API."

def get_random_sub_breed_image(breed, sub_breed):
    """GET request to fetch a random image from a sub-breed."""
    try:
        response = requests.get(f"https://dog.ceo/api/breed/{breed}/{sub_breed}/images/random")
        response.raise_for_status()
        data = response.json()
        if data["status"] == "success":
            return data["message"]
        else:
            return f"Error: Could not get image for sub-breed '{sub_breed}' of breed '{breed}'"
    except requests.exceptions.RequestException:
        return "Error: Could not connect to API."

def show_breeds(breeds_dict):
    """Prints all available breeds 5 per line."""
    all_breeds = sorted(breeds_dict.keys())
    for i in range(0, len(all_breeds), 5):
        print("  ".join(all_breeds[i:i+5]))

def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Show all breeds")
        print("2. Get a random image from a breed")
        print("3. Get a random image from a sub-breed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            breeds = get_all_breeds()
            show_breeds(breeds)

        elif choice == "2":
            breeds = get_all_breeds()
            breed = input("Enter breed name: ").strip().lower()
            if breed not in breeds:
                print(f"Error: Breed '{breed}' not found.")
            else:
                image_url = get_random_image(breed)
                print(f"Image URL: {image_url}")

        elif choice == "3":
            breeds = get_all_breeds()
            breed = input("Enter breed name: ").strip().lower()
            if breed not in breeds:
                print(f"Error: Breed '{breed}' not found.")
            elif not breeds[breed]:
                print(f"Breed '{breed}' has no sub-breeds.")
            else:
                print(f"Available sub-breeds for {breed}: {', '.join(breeds[breed])}")
                sub_breed = input("Enter sub-breed name: ").strip().lower()
                if sub_breed not in breeds[breed]:
                    print(f"Error: Sub-breed '{sub_breed}' not found for breed '{breed}'.")
                else:
                    image_url = get_random_sub_breed_image(breed, sub_breed)
                    print(f"Image URL: {image_url}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 4.")

git add dog_api.py
git commit -m "Complete dog API browser"
git pushif __name__ == "__main__":
    main()
