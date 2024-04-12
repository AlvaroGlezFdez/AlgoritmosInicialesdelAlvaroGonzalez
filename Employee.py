from enum import Enum
class Employees():
    """Python class to implement a basic version of a hotel employee.

    This Python class implements the basic functionalities of a hotel employee in a 
    simple hotel management system.

    Syntax
    ------
    obj = Employee(emp_id, name, position, salary)

    Parameters
    ----------
    [in] emp_id : int
        Unique identifier for the employee.
    [in] name : str
        Name of the employee.
    [in] position : str
        The job position of the employee (e.g., 'Receptionist', 'Housekeeper', 'Manager').
    [in] salary : float
        The salary of the employee.

    Returns
    -------
    obj : Employee
        Python object output parameter that represents an instance of the class Employee.

    Attributes
    ----------
    """
    #Here you start your code.

    def __init__(self, id_empleado, nombre, posicion,salario):
        self._id_empleado = id_empleado
        self._nombre = nombre
        self._posicion = posicion
        self.salario = salario
      

    def get_id_empleado(self):
        return self._id_empleado

    def set_id_empleado(self, id_empleado):
        if not isinstance(id_empleado, int) or id_empleado <= 0:
            raise ValueError("El identificador de empleado debe ser un entero positivo.")
        self._id_empleado = id_empleado

    def get_nombre(self):
        return self._nombre


    def set_nombre(self, nombre):
        if not isinstance(nombre, str) or len(nombre.strip()) == 0:
            raise ValueError("El nombre del empleado no puede estar vacío.")
        self._nombre = nombre

    def get_posicion(self):
        return self._posicion

    def set_posicion(self, posicion):
        if not isinstance(posicion, str) or len(posicion.strip()) == 0:
            raise ValueError("La posición del empleado no puede estar vacía.")
        self._posicion = posicion

   

        
        





def main():
    #TESTING
    print("=================================================================")
    print("Test Case 1: Create an Employee.")
    print("=================================================================")
    employee1 = Employees(1, "John Doe", "Receptionist", 30000)

    if employee1.get_emp_id() == 1:
        print("Test PASS. The parameter emp_id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_name() == "John Doe":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_position() == "Receptionist":
        print("Test PASS. The parameter position has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_salary() == 30000:
        print("Test PASS. The parameter salary has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    # Position and Salary Update Test
    print("=================================================================")
    print("Test Case 2: Update Employee's Position and Salary.")
    print("=================================================================")
    employee1.set_position("Manager")
    employee1.set_salary(50000)

    if employee1.get_position() == "Manager":
        print("Test PASS. The employee's position has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_position().")

    if employee1.get_salary() == 50000:
        print("Test PASS. The employee's salary has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_salary().")

if __name__ == "__main__":
    main()
