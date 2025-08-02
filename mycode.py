def get_user_input():
      """Prompts the user to enter a number and returns it."""
  while True:
    try:
      choice = int(input("Enter a number between 1 and 20: "))
      if 1 <= choice <= 20:
        return choice
      else:
        print("Invalid input. Please enter a number between 1 and 20.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def display_benefit(choice):
  """Displays a benefit based on the user's choice."""
  if 1 <= choice <= 10:
    semen_retention_benefits = {
        1: "Enhanced spiritual awareness and a greater sense of purpose. [6, 8]",
        2: "Increased willpower and discipline in other areas of life. [6]",
        3: "A deeper sense of purpose and fulfillment. [6]",
        4: "Heightened states of consciousness during meditation and prayer. [6]",
        5: "Transmuting sexual energy into higher spiritual awareness and physical health. [6]",
        6: "Channeling sexual energy upwards through the energy channels and chakras. [6]",
        7: "Accelerating spiritual evolution and the awakening of Kundalini energy. [6]",
        8: "Redirecting sexual energies to other areas of life. [7]",
        9: "Improving emotional health. [7]",
        10: "Gaining back your powers as a child of God. [7]"
    }
    print(f"The magical/spiritual benefit of semen retention for number {choice} is: {semen_retention_benefits[choice]}")
  elif 10 < choice <= 20:
    drug_cessation_benefits = {
        11: "Improved physical and mental wellbeing. [3]",
        12: "Reduced risk of permanent damage to vital organs and death. [3]",
        13: "Improved relationships with friends and family. [3, 2]",
        14: "The ability to reconnect with your emotions. [3]",
        15: "Increased energy. [3]",
        16: "Improved sleep. [3]",
        17: "An improved appearance. [3]",
        18: "Saving money. [3]",
        19: "A stronger immune system. [2]",
        20: "Better focus and memory. [5]"
    }
    print(f"The benefit of quitting drugs for number {choice} is: {drug_cessation_benefits[choice]}")

if __name__ == "__main__":
  user_choice = get_user_input()
  display_benefit(user_choice)