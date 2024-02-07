class Cell:

    def __str__(self) -> str:
        return f"Cell: {self.value}. Column: {self.column_name}. Row: {self.row_number}"

    def __init__(self, column_name: str, value: int, row_number: int) -> None:
        self.column_name = column_name
        self.value = value
        self.row_number = row_number
        self.is_access = True


class Table:

    def _validate(self) -> None:
        if (
            self.columns * self.rows < 0 
        ) or (
            self.columns * self.rows > 3 * 10^5
        ):
            raise ValueError("Validateion error!")
        
        if self.conts < 1 or self.conts > 10^5:
            raise ValueError("Validation error!")

    def __init__(self, columns: int, rows: int, conts: int) -> None:
        self.columns = columns
        self.rows = rows
        self.conts = conts
        self._validate()

    def init_column_names(self, names: list[str]) -> None:
        if len(names) != self.columns:
            raise ValueError("Кол-во имён не совпадает с кол-во колонок!")
        self.column_names = names

    def init_cells(self, cell_values: list[list[int]]) -> None:
        self.cells = []
        for row_number in range(self.rows):
            for column_number in range(self.columns):
                self.cells.append(
                    Cell(
                        column_name=self.column_names[column_number],
                        value=cell_values[row_number][column_number],
                        row_number=row_number
                    )
                )

    def apply_constraint(self, constraint: str) -> None:
        column_name, operator, value = constraint.split()
        if operator not in {'<', '>'}:
            raise ValueError(f"Неподдерживаемый оператор: {operator}")

        for cell in self.cells:
            if cell.column_name == column_name:
                if operator == '<' and cell.value >= int(value):
                    cell.is_access = False
                elif operator == '>' and cell.value <= int(value):
                    cell.is_access = False

    @property
    def sum(self) -> int:
        total_sum = 0
        for total_index in range(0, len(self.cells), self.columns):
            is_accesseas = \
                [self.cells[total_index + index].is_access for index in range(self.columns)]
            if not False in is_accesseas:
                total_sum += \
                    sum([self.cells[total_index + index].value for index in range(self.columns)])
        return total_sum


try:
    N: int = int(input("Enter N: "))
    M: int = int(input("Enter M: "))
    Q: int = int(input("Enter Q: "))
except ValueError:
    raise ValueError("Неверный формат данных")

main_table = Table(columns=M, rows=N, conts=Q)
names = input("Enter name(name1 name2 name3 ... nameN): ").split(" ")
main_table.init_column_names(names=names)
rows_values: list[list[int]] = []
for number in range(N):
    row: list[str] = input(f"Enter {number + 1} row values(num1 num2 num3 ... numN): ").split(" ")
    if len(row) != M:
        raise ValueError("Неверное кол-во значений")
    try:
        rows_values.append([int(i) for i in row])
    except ValueError:
        raise ValueError("Вы ввели не число!")

main_table.init_cells(rows_values)
consts: list[str] = []
for num in range(Q):
    constraint = input(f"Enter {num} constraint (name{num} (<, >) NUMBER): ")
    main_table.apply_constraint(constraint)

print(f"Сумма во всех строках, удовлетворяющих всем ограничениям: {main_table.sum}")

