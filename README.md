# interview_task
Aplikację można uruchomić za pomocą dockera
sudo docker build -t interview .
sudo docker run -p 8000:8000 -it --rm --name my-running-app interview
Lub skryptem run.sh
Architekura jest zwykłą MVC. Osobny program na crawlera i osobne api w django napisane. Plus testy w django.
Co do samego scrappera lepszym choć bardziej czasochłonnym podejściem byłby podajże Scrappy. Szczególnie, że wywoływanie i aktualizowanie skryptu mogło by być użyte dzięki crontab. Samo django także było zrobione w jak najszybszym okresie czasowym. Warto by było użyć innej bazy danych albo redisa.
