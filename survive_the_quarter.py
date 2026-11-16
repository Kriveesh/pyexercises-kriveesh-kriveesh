# First name: Kriveeshwaran
# Last name: Shankar
# Group letter: B
# Draft comments: review and rewrite these in your own words before submission.
# 1. Input: scenarios_B.csv uses semicolons and has 14 columns.
# Num identifies the scenario and Situation describes it.
# Each option has Choice (text), Money (budget), Buzz (reputation),
# and Reaction (feedback). Money and Buzz are signed whole numbers.
# Option B uses B_Choice, B_Money, B_Buzz, and B_Reaction.
# The player enters a name, difficulty, and A, B, or C each day.
# 2. Process: shuffle all scenarios and take the first ten.
# Show the day, budget, reputation, situation, and three choices.
# Ask for a choice until it is valid.
# Apply its impacts, limit reputation to 100, and show feedback.
# Store the move in history and stop immediately if a gauge is <= 0.
# 3. Output: show the final gauges, title, best move, and worst move.
# Append name,budget,reputation,title,date to results.csv.
# Example shape: Player,7500,80,Growth Hacker,2026-11-16
# 4. Problems: invalid choices are requested again; blank names are rejected.
# A gauge <= 0 ends the game with the reason for being fired.
# Missing or invalid scenario files produce a clear message instead of crashing.
# An unavailable results file produces a warning without losing the final display.
# Feature: difficulty. Easy starts at 15000 EUR, hard at 6000 EUR.
# I chose it because a smaller budget makes expensive choices harder.

import csv
import random
from datetime import date
from pathlib import Path


# Load group B's columns and turn each option into the required tuple.
def load_scenarios(filename):
    scenarios = []
    with open(filename, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=";")
        required = ["Num", "Situation"]
        for letter in "ABC":
            for ending in ["Choice", "Money", "Buzz", "Reaction"]:
                required.append(letter + "_" + ending)
        if reader.fieldnames != required:
            raise ValueError("The scenario file must use group B's 14 columns.")
        for row in reader:
            options = {}
            for letter in "ABC":
                options[letter] = (
                    row[letter + "_Choice"],
                    int(row[letter + "_Money"]),
                    int(row[letter + "_Buzz"]),
                    row[letter + "_Reaction"],
                )
            scenarios.append({
                "number": int(row["Num"]),
                "situation": row["Situation"],
                "options": options,
            })
    if len(scenarios) < 10:
        raise ValueError("At least ten scenarios are needed.")
    return scenarios


# Require a player name so the saved result has an owner.
def ask_player_name():
    name = input("Player name: ").strip()
    while not name:
        name = input("Please enter a name: ").strip()
    return name


# Set the starting budget using the chosen difficulty.
def choose_starting_budget():
    while True:
        difficulty = input("Difficulty (easy or hard): ").strip().lower()
        if difficulty == "easy":
            return 15000
        if difficulty == "hard":
            return 6000
        print("Please type easy or hard.")


# Accept only one of the three displayed choices.
def ask_choice():
    while True:
        choice = input("Your choice (A, B or C): ").strip().upper()
        if choice in ("A", "B", "C"):
            return choice
        print("Please type A, B or C.")


# Return the two updated gauges as a tuple for the caller to unpack.
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option
    return budget + budget_change, min(100, reputation + reputation_change)


# Translate the final gauges into the title specified in the brief.
def calculate_title(budget, reputation):
    if budget <= 0 or reputation <= 0:
        return "Fired"
    score = reputation + budget // 200
    if score < 95:
        return "Eternal Intern"
    elif score < 120:
        return "Growth Hacker"
    elif score < 140:
        return "CMO Material"
    return "Viral Legend"


# Compare the first item of each history tuple to find reputation extremes.
def show_best_and_worst(history):
    best = max(history)
    worst = min(history)
    change, day, text = best
    print(f'Best move: day {day}, "{text}" ({change:+d})')
    change, day, text = worst
    print(f'Worst move: day {day}, "{text}" ({change:+d})')


# Append one game result and write the header only for an empty file.
def save_result(filename, name, budget, reputation, title):
    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["name", "budget", "reputation", "title", "date"])
        writer.writerow([name, budget, reputation, title, date.today().isoformat()])


# Run one game from the files beside this Python script.
def play_game():
    folder = Path(__file__).resolve().parent
    try:
        scenarios = load_scenarios(folder / "scenarios_B.csv")
    except (OSError, ValueError, KeyError, TypeError, csv.Error) as error:
        print("Cannot load scenarios_B.csv:", error)
        return

    name = ask_player_name()
    budget = choose_starting_budget()
    reputation = 50
    history = []
    random.shuffle(scenarios)

    # Play up to ten different situations, stopping as soon as a gauge fails.
    for day, scenario in enumerate(scenarios[:10], start=1):
        print(f"\n--- Day {day} ---")
        print(f"Budget: {budget} EUR | Reputation: {reputation}/100")
        print(scenario["situation"])
        for letter in "ABC":
            print(letter + ": " + scenario["options"][letter][0])

        choice = ask_choice()
        option = scenario["options"][choice]
        text, budget_change, reputation_change, feedback = option
        budget, reputation = apply_choice(budget, reputation, option)
        print(feedback)
        print(f"Budget {budget_change:+d} EUR, Reputation {reputation_change:+d}")
        print(f"Now: {budget} EUR | Reputation: {reputation}/100")
        # Record the option's stated reputation impact, before the 100 cap.
        history.append((reputation_change, day, text))
        if budget <= 0 or reputation <= 0:
            break

    # Explain the final outcome and show the strongest and weakest choices.
    title = calculate_title(budget, reputation)
    if title == "Fired":
        if budget <= 0:
            print("Fired: your budget reached zero or below.")
        if reputation <= 0:
            print("Fired: your reputation reached zero or below.")
    else:
        print("Quarter survived!")
        print("Final score:", reputation + budget // 200)
    print(f"Budget left: {budget} EUR | Reputation: {reputation}/100")
    print(name + ", your title: " + title)
    show_best_and_worst(history)

    # Keep earlier results when saving this game's result.
    try:
        save_result(folder / "results.csv", name, budget, reputation, title)
        print("Saved in results.csv")
    except (OSError, csv.Error) as error:
        print("Could not save results.csv:", error)


# End cleanly if the terminal closes or the player interrupts input.
if __name__ == "__main__":
    try:
        play_game()
    except (EOFError, KeyboardInterrupt):
        print("\nGame cancelled. No completed result was saved.")
