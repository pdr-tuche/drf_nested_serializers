FROM python

COPY . /armazem

WORKDIR /armazem

EXPOSE 8000

RUN pip install -r requirements.txt

CMD [ "manage.py runserver" ]

ENTRYPOINT [ "python" ]
