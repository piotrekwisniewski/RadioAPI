# RestHits –

Aplikacja REST API do zarządzania hitami radiowymi, oparta o Django, PostgreSQL i Docker.

## Funkcje

- Przeglądanie, dodawanie, edycja i usuwanie rekordów utworów radiowych przez API.
- Dokumentacja Swagger/Redoc.
- Seedowanie bazy przykładowymi danymi.
- Gotowa do uruchomienia w kontenerach Docker.

## Wymagania

- Docker + Docker Compose
- Python 3.12 (jeśli uruchamiane poza Dockerem)

## Szybki start (Docker)

1. **Sklonuj repozytorium [BASH]:**

git clone https://github.com/piotrekwisniewski/RadioAPI

2. **Utwórz plik `.env` w katalogu głównym projektu** (na tym samym poziomie co `docker-compose.yml`) i wpisz wartości zmiennych środowiskowych uzupełniając nazwę użytkownika i hasło:


>POSTGRES_USER={user}  
>POSTGRES_PASSWORD={SilneHaslo}  
>POSTGRES_DB=radiodb  
>POSTGRES_HOST=db  
>POSTGRES_PORT=5432  

 **Uwaga:** Plik `.env` powinien być wykluczony z repozytorium (`.gitignore`).

3. **Zbuduj i uruchom kontenery [BASH]:**

> docker-compose up -d

 4. **Wykonaj migracje bazy danych [BASH]:**

>docker-compose run web python manage.py migrate

5. **Wypełnij bazę przykładowymi danymi [BASH]:**

>docker-compose run web python manage.py db_populate

6. **Otwórz aplikację:**

- API: [http://localhost:8000/api/v1/hits](http://localhost:8000/api/v1/hits)
- Dokumentacja Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- Dokumentacja Redoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)



## Najważniejsze komendy [BASH]

- **Budowanie i uruchamianie kontenerów:**  
  `docker-compose up -d`
- **Zatrzymanie i usunięcie kontenerów oraz danych bazy:**  
  `docker-compose down --volumes --remove-orphans`
- **Wykonanie migracji:**  
  `docker-compose run web python manage.py migrate`
- **Seedowanie bazy:**  
  `docker-compose run web python manage.py db_populate`