import csv


def find_errors(path):
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file, skipinitialspace=True)

        header = next(reader)
        errors = []

        for line_number, row in enumerate(reader, start=2):
            if len(row) != len(header):
                errors.append(line_number)

        return errors


def calculate_average(path):
    with open(path, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file, skipinitialspace=True)

        header = next(reader)
        final_index = header.index("Final")

        grades = []

        for line_number, row in enumerate(reader, start=2):
            if len(row) != len(header):
                raise ValueError(
                    f"Ошибка в строке {line_number}: "
                    f"ожидалось {len(header)} столбцов, получено {len(row)}"
                )

            grades.append(float(row[final_index]))

        return sum(grades) / len(grades)


if __name__ == "__main__":
    errors = find_errors("data/grades_original.csv")

    print(f"Ошибки найдены в строках: {errors}")

    average = calculate_average("data/grades.csv")
    print(f"Среднее арифметическое Final: {average:.2f}")
