def calculate_love_score(name1, name2):
    # Convert both names to lowercase and combine
    combined_names = (name1 + name2).lower()

    # Count letters for TRUE
    true_count = 0
    for letter in "true":
        true_count += combined_names.count(letter)

    # Count letters for LOVE
    love_count = 0
    for letter in "love":
        love_count += combined_names.count(letter)

    # Combine counts into a two-digit score
    love_score = int(str(true_count) + str(love_count))

    # Print the result as required
    print(love_score)

# Example call with hardcoded names
calculate_love_score("Kanye West", "Kim Kardashian")
