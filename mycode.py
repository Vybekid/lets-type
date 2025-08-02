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
        1: "Conserving semen allows the vital energy (ojas) to nourish the brain, sharpening memory and intellect for understanding scripture. [11]",
        2: "Following the vow of brahmacharya (celibacy) helps in controlling the mind and senses, which is essential for spiritual advancement. [10]",
        3: "By abstaining from sense gratification, one can more easily focus on devotional service and pleasing Krishna. [9]",
        4: "True strength, as Krishna teaches in the Bhagavad Gita, is devoid of desire and attachment, which is cultivated through retention. [6]",
        5: "Brahmacharya is the basis for achieving immortality and opens the door to Moksha (liberation). [12]",
        6: "It helps transmute physical energy into spiritual energy, which is necessary to reawaken our dormant love for God. [14]",
        7: "Preserving vital fluid leads to fixed intelligence, strong determination, and willpower in one's devotional path. [8]",
        8: "One who practices brahmacharya gives Krishna a special place in their heart, allowing for a deeper meditative connection. [3]",
        9: "The practice helps overcome the 'eternal enemy' of lust, which Krishna describes as an insatiable fire. [6]",
        10: "By retaining this sacred energy, one can attain the highest perfection of life by attentively hearing the Lord's pastimes. [15]"
    }
    print(f"The spiritual benefit of semen retention in Krishna Consciousness for number {choice} is: {semen_retention_benefits[choice]}")
  elif 10 < choice <= 20:
    # Benefits of quitting drugs remain the same as they are universally applicable.
    # Sourced from the previous interaction.
    drug_cessation_benefits = {
        11: "Improved physical and mental wellbeing.",
        12: "Reduced risk of permanent damage to vital organs and death.",
        13: "Improved relationships with friends and family.",
        14: "The ability to reconnect with your emotions.",
        15: "Increased energy.",
        16: "Improved sleep.",
        17: "An improved appearance.",
        18: "Saving money.",
        19: "A stronger immune system.",
        20: "Better focus and memory."
    }
    print(f"The benefit of quitting drugs for number {choice} is: {drug_cessation_benefits[choice]}")

if __name__ == "__main__":
  user_choice = get_user_input()
  display_benefit(user_choice)