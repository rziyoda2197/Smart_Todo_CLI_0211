import json
import os

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\nVazifalar yo‘q.\n")
        return
    print("\nVazifalar:")
    for i, t in enumerate(tasks, 1):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {t['title']} {status}")
    print()

def add_task(tasks):
    title = input("Yangi vazifa: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)

def complete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Bajarilgan vazifa raqami: "))
        tasks[num-1]["done"] = True
        save_tasks(tasks)
    except:
        print("Xato raqam")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("O‘chirish raqami: "))
        tasks.pop(num-1)
        save_tasks(tasks)
    except:
        print("Xato raqam")

def main():
    tasks = load_tasks()

    while True:
        print("1. Ko‘rish")
        print("2. Qo‘shish")
        print("3. Bajarildi")
        print("4. O‘chirish")
        print("0. Chiqish")

        choice = input("Tanla: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "0":
            break
        else:
            print("Noto‘g‘ri tanlov")

if __name__ == "__main__":
    main()
