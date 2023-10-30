class ToDoList:
    todo = {}

    def __init__(self):
        pass

    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere

    def finalizare_task(self, nume):
        self.todo.pop(nume)

    def afiseaza_todo_list(self):
        for task in self.todo.keys():
            print(f'{task}')

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task not in self.todo.keys():
            raspuns = input(f'taskul {nume_task} nu e in todo list, doresti sa il adaugi? Y/N ')
            if raspuns == 'Y':
                descriere_task = input(f'dati o descriere pentru taskul {nume_task}:')
                self.adauga_task(nume_task, descriere_task)
            else:
                print('la revedere')



lista = ToDoList()
lista.adauga_task("mancare", "de pus mancarea in frigider")
lista.adauga_task("tema", "tema trebuie facuta pana vineri")
lista.afiseaza_todo_list()
lista.afiseaza_detalii_suplimentare("tema")
lista.afiseaza_detalii_suplimentare("pastile")
lista.afiseaza_todo_list()
print('*'*100)
lista.finalizare_task("mancare")
lista.afiseaza_todo_list()




