from bs4 import BeautifulSoup
import requests
import folium
import webbrowser
import os

def get_coords(client_location):
    # Funkcja pobiera współrzędne geograficzne (szerokość i długość) dla podanej lokalizacji z Wikipedii
    adres_url = f'https://pl.wikipedia.org/wiki/{client_location}'
    response = requests.get(adres_url)
    response_html = BeautifulSoup(response.text, 'html.parser')
    latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
    longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
    print([latitude, longitude])
    return [latitude, longitude]

def show_clients(clients):
    # Wyświetla listę klientów firmy
    company_name = input("Podaj nazwę firmy, której lista klientów ma zostać wyświetlona: ")
    company_found = False

    # Sprawdzenie, czy firma istnieje wśród klientów
    for client in clients:
        if client['client_company'] == company_name:
            company_found = True
            break

    # Wyświetlenie listy klientów, jeśli firma została znaleziona
    if company_found:
        print(f"Lista klientów firmy {company_name}:")
        for client in clients:
            if client['client_company'] == company_name:
                print(f" - {client['client_name']}")
    else:
        print(f"{company_name} nie znaleziono takiej firmy na liście.")

def add_client(clients, companies):
    # Dodaje nowego klienta do firmy
    company_name = input("Podaj nazwę firmy, do której chcesz dodać klienta: ")
    company_found = False
    for company in companies:
        if company["company_name"] == company_name:
            client_name = input(f"Podaj imię i nazwisko klienta do dodania do {company_name}: ")
            client_location = input(f"Podaj lokalizację klienta (miasto): ")
            company_name=input(f"Podaj firmę, której {client_name} jest klientem (klientką): ")
            clients.append({
                "client_name": client_name,
                "client_company": company_name,
                "client_location": client_location
            })
            print(f"{client_name} został(a) dodany(a) do listy klientów firmy {company_name}.")
            company_found = True
            break
    if not company_found:
        print(f"{company_name} nie znaleziono takiej firmy na liście.")

def remove_client(companies, clients):
    # Usuwa klienta z firmy
    company_name = input("Podaj nazwę firmy, z której chcesz usunąć klienta: ")
    company_found = False

    # Sprawdzenie, czy firma istnieje wśród firm
    for company in companies:
        if company['company_name'] == company_name:
            company_found = True
            client_name = input(f"Podaj imię i nazwisko klienta do usunięcia z {company_name}: ")
            client_found = False

            # Przeszukiwanie listy klientów, aby znaleźć i usunąć klienta
            for client in clients:
                if client['client_name'] == client_name and client['client_company'] == company_name:
                    clients.remove(client)
                    print(f"{client_name} został(a) usunięty(a) z listy klientów firmy {company_name}.")
                    client_found = True
                    break

            if not client_found:
                print(f"{client_name} nie znaleziono na liście klientów firmy {company_name}.")
            break

    if not company_found:
        print(f"{company_name} nie znaleziono takiej firmy na liście.")

def update_client(companies, clients):
    # Aktualizuje dane klienta
    company_name = input("Podaj nazwę firmy, w której chcesz zaktualizować dane klienta: ")
    company_found = False

    # Sprawdzenie, czy firma istnieje wśród firm
    for company in companies:
        if company['company_name'] == company_name:
            company_found = True
            old_client_name = input(f"Podaj imię i nazwisko klienta do zaktualizowania w {company_name}: ")
            client_found = False

            # Przeszukiwanie listy klientów, aby znaleźć i zaktualizować klienta
            for client in clients:
                if client['client_name'] == old_client_name and client['client_company'] == company_name:
                    new_client_name = input(
                        f"Podaj nowe imię i nazwisko dla {old_client_name} (pozostaw puste, aby nie zmieniać): ")
                    new_client_location = input(
                        f"Podaj nową lokalizację dla {old_client_name} (pozostaw puste, aby nie zmieniać): ")

                    # Aktualizacja imienia i nazwiska, jeśli zostało podane
                    if new_client_name:
                        client['client_name'] = new_client_name
                        print(f"Dane klienta zostały zmienione z {old_client_name} na {new_client_name}.")
                    # Aktualizacja lokalizacji, jeśli została podana
                    if new_client_location:
                        client['client_location'] = new_client_location
                        print(f"Lokalizacja klienta {old_client_name} została zmieniona na {new_client_location}.")

                    client_found = True
                    break

            if not client_found:
                print(f"{old_client_name} nie znaleziono na liście klientów firmy {company_name}.")
            break

    if not company_found:
        print(f"{company_name} nie znaleziono takiej firmy na liście.")

def dms_to_decimal(dms):
    # Konwertuje współrzędne geograficzne z formatu DMS (stopnie, minuty, sekundy) na format dziesiętny
    parts = dms.split('°')
    degrees = float(parts[0])
    parts = parts[1].split('′')
    minutes = float(parts[0])
    parts = parts[1].split('″')
    seconds = float(parts[0])
    direction = parts[1].strip()

    decimal_degrees = degrees + minutes / 60 + seconds / 3600

    if direction in ['S', 'W']:
        decimal_degrees *= -1

    return decimal_degrees

def clients_map(clients):
    # Tworzy mapę klientów, pobierając współrzędne z Wikipedii i dodając markery do mapy
    map = folium.Map(location=[52, 20], zoom_start=7)
    for client in clients:
        client_name = client['client_name']
        client_location = client['client_location']
        url = f"https://pl.wikipedia.org/wiki/{client_location}"

        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')

        latitude_tag = response_html.find('span', {'class': 'latitude'})
        longitude_tag = response_html.find('span', {'class': 'longitude'})

        if latitude_tag and longitude_tag:
            latitude = dms_to_decimal(latitude_tag.text)
            longitude = dms_to_decimal(longitude_tag.text)
            print(
                f"Klient: {client_name}, Lokalizacja: {client_location}, Szerokość geograficzna: {latitude}, Długość geograficzna: {longitude}")
            folium.Marker(
                location=[latitude, longitude],
                popup=f"{client_name},\n{client_location}",
                icon=folium.Icon(color='red', icon='male')
            ).add_to(map)
        else:
            print(f"Nie udało się znaleźć współrzędnych dla lokalizacji: {client_location}")

    # Zapisuje mapę do pliku HTML i otwiera ją w przeglądarce
    map_dir = 'models/maps'
    os.makedirs(map_dir, exist_ok=True)
    map_file = os.path.join(map_dir, 'map_clients.html')
    map.save(map_file)
    webbrowser.open(map_file)