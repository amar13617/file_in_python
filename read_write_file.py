my_file = open('data.txt', 'r')
file_content = my_file.read()
my_file.close()
print(file_content)

user_name = input("Enter your name")
my_file_writing = open('data.txt', 'w')
my_file_writing.write(user_name)
my_file_writing.close()

with open("hello_world.txt", "w") as f:
    f.write("Hello, World!")

with open("hello_world.txt", "a") as f:
    f.write("\nHow are you?")
    
    print(f)

    