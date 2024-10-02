import random

# Function to generate a hybrid name
def generate_hybrid_name(creature1, creature2):
    # Combine part of each creature's name to create a hybrid name
    return creature1[:len(creature1)//2] + creature2[len(creature2)//2:]

# Function to generate creature details
def generate_creature_details():
    weight = random.randint(100, 2000)  # Random weight between 100lbs and 2000lbs
    diets = ["celery", "meat", "fruits", "insects", "grass", "fish"]
    diet = random.choice(diets)  # Random diet choice
    return weight, diet

# Function to display an ASCII check mark to confirm creation
def display_ascii_checkmark():
    checkmark = """
        _______  
       /       \\
      /  ____   \\
     /  /    \\  |  
    /  /      \\ |
    \\ |        \\| 
     \\
      \\
       \\_______/
    """
    print(checkmark)

# Main program
def main():
    print("Welcome to the Hybrid Creature Generator!")
    
    # Get user input for the two creatures
    creature1 = input("Enter the first creature's name: ")
    creature2 = input("Enter the second creature's name: ")
    
    # Generate hybrid name
    hybrid_name = generate_hybrid_name(creature1, creature2)
    
    # Generate weight and diet
    weight, diet = generate_creature_details()
    
    # Display the result
    print(f"\nCongratulations! You have created a new hybrid creature: {hybrid_name}")
    print(f"Details about {hybrid_name}:")
    print(f"Weight: {weight} lbs")
    print(f"Preferred diet: {diet}")
    
    # Display ASCII checkmark to confirm creation
    display_ascii_checkmark()

# Run the program
if __name__ == "__main__":
    main()