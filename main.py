# Importowanie niezbędnych funkcji i danych z innych modułów
from FunkcjeFirmy import show_companies, add_company, remove_company, update_company, companies_map
from FunkcjeKlienci import show_clients, add_client, remove_client, update_client, clients_map
from FunkcjePracownicy import show_workers, add_worker, remove_worker, update_worker, workers_map
from Lista import companies, clients, workers

def logowanie():
    # Ustawienie poprawnych danych logowania
    correct_login = "123"
    correct_password = "123"
    logowanie = False

    # Pętla logowania, dopóki użytkownik nie wprowadzi poprawnych danych
    while not logowanie:
        login = input("Wprowadź login: ")
        password = input("Wprowadź hasło: ")

        # Sprawdzenie, czy wprowadzone dane są poprawne
        if not (login == correct_login and password == correct_password):

            print("Niepoprawny login lub hasło.")
            logowanie = False

        else:
            print("Pomyślnie zalogowano.")
            logowanie = True

            print("Witaj w systemie zarządzania firmami sprzątającymi.")
            while True:
                # Wyświetlanie głównego menu
                print("Menu:")
                print("0. Zakończ pracę")
                print("1. Firmy sprzątające")
                print("2. Klienci")
                print("3. Pracownicy")
                menu_option = input("Wybierz opcję: ")
                if menu_option == '0':
                    break
                elif menu_option == '1':
                    while True:
                        # Wyświetlanie menu zarządzania firmami sprzątającymi
                        print("0. Powrót do menu głównego")
                        print("1. Wyświetl listę firm sprzątających")
                        print("2. Dodaj firmę do listy")
                        print("3. Usuń firmę z listy")
                        print("4. Aktualizuj dane firmy")
                        print("5. Wyświetl lokalizację wszystkich firm na mapie")
                        opcja = input("Wybierz opcję: ")
                        if opcja == '0':
                            break
                        elif opcja == '1':
                            show_companies(companies)
                        elif opcja == '2':
                            add_company(companies)
                            show_companies(companies)
                        elif opcja == '3':
                            remove_company(companies)
                            show_companies(companies)
                        elif opcja == '4':
                            update_company(companies)
                            show_companies(companies)
                        elif opcja == '5':
                            companies_map(companies)
                        else:
                            print("Niewłaściwa opcja. Wybierz z dostępnych powyżej.")
                elif menu_option == '2':
                    while True:
                        # Wyświetlanie menu zarządzania klientami
                        print("0. Powrót do menu głównego")
                        print("1. Wyświetl listę klientów danej firmy")
                        print("2. Dodaj klienta do firmy")
                        print("3. Usuń klienta z firmy")
                        print("4. Aktualizuj dane klienta")
                        print("5. Wyświetl lokalizację wszystkich klientów na mapie")
                        opcja = input("Wybierz opcję: ")
                        if opcja == '0':
                            break
                        elif opcja == '1':
                            show_clients(clients)
                        elif opcja == '2':
                            add_client(clients, companies)
                        elif opcja == '3':
                            remove_client(clients, companies)
                        elif opcja == '4':
                            update_client(clients, companies)
                        elif opcja == '5':
                            clients_map(clients)
                        else:
                            print("Niewłaściwa opcja. Wybierz z dostępnych powyżej.")
                elif menu_option == '3':
                    while True:
                        # Wyświetlanie menu zarządzania pracownikami
                        print("0. Powrót do menu głównego")
                        print("1. Wyświetl listę pracowników danej firmy")
                        print("2. Dodaj pracownika do firmy")
                        print("3. Usuń pracownika z firmy")
                        print("4. Aktualizuj dane pracownika")
                        print("5. Wyświetl lokalizację wszystkich pracowników na mapie")
                        opcja = input("Wybierz opcję: ")
                        if opcja == '0':
                            break
                        elif opcja == '1':
                            show_workers(workers)
                        elif opcja == '2':
                            add_worker(workers, companies)
                        elif opcja == '3':
                            remove_worker(workers, companies)
                        elif opcja == '4':
                            update_worker(workers, companies)
                        elif opcja == '5':
                            workers_map(workers)
                        else:
                            print("Niewłaściwa opcja. Wybierz z dostępnych powyżej.")
                print("Dziękujemy za skorzystanie z systemu. Do widzenia!")

logowanie()
