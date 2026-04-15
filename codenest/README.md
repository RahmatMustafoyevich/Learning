# CodeNest (Django + Bootstrap)

CodeNest — dasturlashni o‘rganish platformasi uchun boshlang‘ich loyiha.

## Funksiyalar
- Kurslar va lessonlar (accordion ko‘rinishida)
- Lesson video, izoh va yulduzcha baholash
- Lessonga quiz modeli
- Blog sahifasi va like bosish
- Manbalar: kodlar va e-kitoblar
- Profil sahifasi: ism, familiya, username, email, avatar
- Rollar: admin, teacher, student
- Dark/Light mode
- To‘liq responsiv Bootstrap UI

## Ishga tushirish
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Admin panel: `/admin/`
