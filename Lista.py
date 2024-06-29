# Lista firm sprzątających, każda firma jest reprezentowana przez słownik z nazwą i lokalizacją
companies: list[dict] = [
    {'company_name': 'CleanPol', 'company_location': 'Warszawa'},
    {'company_name': 'SanitClean', 'company_location': 'Kraków'},
    {'company_name': 'SprytnaKaśka - usługi sprzątające', 'company_location': 'Wrocław'},
    {'company_name': 'SyfBusters - pogromcy brudu', 'company_location': 'Gdańsk'},
    {'company_name': 'UltraPołysk - czyste okna i nie tylko', 'company_location': 'Bydgoszcz'}
]

# Lista klientów, każdy klient jest reprezentowany przez słownik z imieniem, firmą i lokalizacją
clients: list[dict] = [
    {'client_name': 'Andrzej Czysty', 'client_company': 'CleanPol', 'client_location': 'Warszawa'},
    {'client_name': 'Tomasz Brudny', 'client_company': 'CleanPol', 'client_location': 'Garwolin'},
    {'client_name': 'Janusz Miotła', 'client_company': 'CleanPol', 'client_location': 'Otwock'},
    {'client_name': 'Anna Podłoga', 'client_company': 'SanitClean', 'client_location': 'Kraków'},
    {'client_name': 'Kazimierz Niechlujny', 'client_company': 'SanitClean', 'client_location': 'Skawina'},
    {'client_name': 'Mariusz Mop', 'client_company': 'SanitClean', 'client_location': 'Myślenice'},
    {'client_name': 'Małgorzata Nieczysta', 'client_company': 'SprytnaKaśka - usługi sprzątające', 'client_location': 'Wrocław'},
    {'client_name': 'Krzysztof Leń', 'client_company': 'SprytnaKaśka - usługi sprzątające', 'client_location': 'Miłoszyce'},
    {'client_name': 'Czesław Detergent', 'client_company': 'SprytnaKaśka - usługi sprzątające', 'client_location': 'Oleśnica'},
    {'client_name': 'Wiktor Wektor', 'client_company': 'SyfBusters - pogromcy brudu', 'client_location': 'Gdańsk'},
    {'client_name': 'Bartosz Kurz', 'client_company': 'SyfBusters - pogromcy brudu', 'client_location': 'Gdynia'},
    {'client_name': 'Ingmar Rabarbar', 'client_company': 'SyfBusters - pogromcy brudu', 'client_location': 'Sopot'},
    {'client_name': 'Leszek Leser', 'client_company': 'UltraPołysk - czyste okna i nie tylko', 'client_location': 'Bydgoszcz'},
    {'client_name': 'Natan Nieład', 'client_company': 'UltraPołysk - czyste okna i nie tylko', 'client_location': 'Solec Kujawski'},
    {'client_name': 'Łukasz Łapciuch', 'client_company': 'UltraPołysk - czyste okna i nie tylko', 'client_location': 'Toruń'},
]

# Lista pracowników, każdy pracownik jest reprezentowany przez słownik z imieniem, firmą i lokalizacją
workers: list[dict] = [
    {'worker_name': 'Barbara Wiadro', 'worker_company': 'CleanPol', 'worker_location': 'Warszawa'},
    {'worker_name': 'Jadwiga Ścierka', 'worker_company': 'CleanPol', 'worker_location': 'Sulejówek'},
    {'worker_name': 'Mateusz Odkurzacz', 'worker_company': 'SanitClean', 'worker_location': 'Kraków'},
    {'worker_name': 'Stanisława Perfekcyjna', 'worker_company': 'SanitClean', 'worker_location': 'Wieliczka'},
    {'worker_name': 'Katarzyna Sprytna', 'worker_company': 'SprytnaKaśka - usługi sprzątające', 'worker_location': 'Wrocław'},
    {'worker_name': 'Monika Muchozol', 'worker_company': 'SprytnaKaśka - usługi sprzątające', 'worker_location': 'Jelcz-Laskowice'},
    {'worker_name': 'Aleksander Washingpowder', 'worker_company': 'SyfBusters - pogromcy brudu', 'worker_location': 'Gdańsk'},
    {'worker_name': 'Zbigniew Krochmal', 'worker_company': 'SyfBusters - pogromcy brudu', 'worker_location': 'Gdynia'},
    {'worker_name': 'Wiesława Gąbka', 'worker_company': 'UltraPołysk - czyste okna i nie tylko', 'worker_location': 'Bydgoszcz'},
    {'worker_name': 'Teresa Floresa', 'worker_company': 'UltraPołysk - czyste okna i nie tylko', 'worker_location': 'Solec Kujawski'},
]