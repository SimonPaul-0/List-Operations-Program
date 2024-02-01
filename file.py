def reverse_list(lst):
    return lst[::-1]

def capitalize_list(lst):
    return [item.capitalize() for item in lst]

def count_elements(lst):
    return len(lst)

def concatenate_lists(list1, list2):
    return list1 + list2

def repeat_list(lst, n):
    return lst * n

def search_element(lst, element):
    return lst.index(element) if element in lst else -1

def find_element_index(lst, target):
    return [index for index, item in enumerate(lst) if item == target]

def is_numeric_list(lst):
    return all(isinstance(item, (int, float)) for item in lst)

def is_palindrome_list(lst):
    cleaned_list = [item.lower() for item in lst if str(item).isalnum()]
    return cleaned_list == cleaned_list[::-1]

def replace_element(lst, old_element, new_element):
    return [new_element if item == old_element else item for item in lst]

def remove_duplicates(lst):
    return list(set(lst))

def main():
    user_list = eval(input("Enter a list (e.g., [1, 'abc', 3.14]): "))

    while True:
        print("\nMenu:")
        print("1. Reverse List")
        print("2. Capitalize List")
        print("3. Count Elements")
        print("4. Concatenate Lists")
        print("5. Repeat List")
        print("6. Search Element")
        print("7. Find Element Index")
        print("8. Check Numeric List")
        print("9. Check Palindrome List")
        print("10. Replace Element")
        print("11. Remove Duplicates")
        print("12. Exit")

        choice = input("Enter your choice (1-12): ")

        if choice == '1':
            result = reverse_list(user_list)
            print("Reversed List:", result)
        elif choice == '2':
            result = capitalize_list(user_list)
            print("Capitalized List:", result)
        elif choice == '3':
            result = count_elements(user_list)
            print("Number of Elements:", result)
        elif choice == '4':
            second_list = eval(input("Enter another list to concatenate: "))
            result = concatenate_lists(user_list, second_list)
            print("Concatenated List:", result)
        elif choice == '5':
            repetition_count = int(input("Enter the repetition count: "))
            result = repeat_list(user_list, repetition_count)
            print("Repeated List:", result)
        elif choice == '6':
            element_to_search = eval(input("Enter the element to search for: "))
            index = search_element(user_list, element_to_search)
            if index != -1:
                print(f"Element found at index {index}.")
            else:
                print("Element not found.")
        elif choice == '7':
            target_element = eval(input("Enter the element to find: "))
            indices = find_element_index(user_list, target_element)
            if indices:
                print(f"Element found at indices {indices}.")
            else:
                print(f"Element '{target_element}' not found.")
        elif choice == '8':
            result = is_numeric_list(user_list)
            if result:
                print("The list is numeric.")
            else:
                print("The list is not entirely numeric.")
        elif choice == '9':
            result = is_palindrome_list(user_list)
            if result:
                print("The list is a palindrome.")
            else:
                print("The list is not a palindrome.")
        elif choice == '10':
            old_element = eval(input("Enter the element to replace: "))
            new_element = eval(input("Enter the new element: "))
            result = replace_element(user_list, old_element, new_element)
            print("Modified List:", result)
        elif choice == '11':
            result = remove_duplicates(user_list)
            print("List with Duplicates Removed:", result)
        elif choice == '12':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
