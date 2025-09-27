def main():
    students = {}

    while True:
        name = input("введіть ім'я студента або 'stop': ")
        if name.lower() == 'stop':
            break

        try:
            grade = int(input(f"введіть оцінку для {name}: "))
            if grade < 1 or grade > 12:
                raise ValueError("Оцінка має бути від 1 до 12")
            students[name] = grade
        except ValueError as e:
            print(f"Помилка: {e}")
            continue

    print("Результати:")
    for name, grade in students.items():
        print(f"{name}: {grade}")

    if students:
        average = sum(students.values()) / len(students)
        print(f"\nСередній бал по групі: {average:.2f}")

        vidminnyky = [name for name, grade in students.items() if 10 <= grade <= 12]
        khoroshysty = [name for name, grade in students.items() if 7 <= grade <= 9]
        vidstayuchi = [name for name, grade in students.items() if 4 <= grade <= 6]
        nezdachi = [name for name, grade in students.items() if 1 <= grade <= 3]

        print(f"Відмінники (10-12): {len(vidminnyky)} → {vidminnyky}")
        print(f"Хорошисти (7-9): {len(khoroshysty)} → {khoroshysty}")
        print(f"Відстаючі (4-6): {len(vidstayuchi)} → {vidstayuchi}")
        print(f"Не здали (1-3): {len(nezdachi)} → {nezdachi}")
    else:
        print("Студентів не введено.")

if __name__ == "__main__":
    main()
