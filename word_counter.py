def word_counter(sentence):
    words = sentence.split()     # Splitting the sentence into words on the basis of white-spaces
    return len(words)            # Return the number of words


user_input = input("Please enter a sentence or paragraph: ").strip()      # Taking user input
    
# Check if the input is empty
if not user_input:
    print("Error: No input provided. Please enter some sentence.")
    
    
# Count the number of words in the input
word_count = word_counter(user_input)
    
# Display the word count
print(f"The number of words in the given sentence is: {word_count}")