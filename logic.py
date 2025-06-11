def reverse_number(numbers):
    """
    反轉數字列表中的每個數字。
    """
    reversed_numbers = [int(str(num)[::-1]) for num in numbers]
    return reversed_numbers

def count_letter(text):
    """
    計算文本中每個字母的出現次數。
    """
    letter_count = {}
    for char in text:
        if char.isalpha(): 
            char = char.lower()  
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count


def pop_people(n):    
    """
    從1到n的人中，每次跳過兩個人，直到只剩下一個人。
    """

    people = list(range(1, n + 1))  
    index = 0  

    while len(people) > 1:
        index = (index + 2) % len(people)  
        people.pop(index)  

    return people[0]  
    

# Example usage
if __name__ == "__main__":
    input_numbers = [35, 46, 57, 91, 29]
    output_numbers = reverse_number(input_numbers)
    print("輸入:", input_numbers)
    print("輸出:", output_numbers)

    input_text = "Hello welcome to Cathay 60th year anniversary"
    output_count = count_letter(input_text)
    print("輸入:", input_text)
    print("輸出:", output_count)

    n = 50
    last_person = pop_people(n)
    print(f"從1到{n}的人中，最後剩下的人是: {last_person}")