# task9--
# Example two
voter_set = set()

while True:
    name = input("Enter voter's name (or type 'exit' to finish): ").strip().title()
    
    if name.lower() == 'exit':
        break

    if name in voter_set:
        print("⚠️ Warning: This voter is already registered.")
    else:
        voter_set.add(name)
        print(f"✅ {name} has been successfully registered.")
# Display total unique voters
print("\n🗳️ Registration Complete.")
print(f"Total unique voters registered: {len(voter_set)}")
