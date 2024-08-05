FROM thejmthon/jmbot:slim-buster

RUN git clone https://github.com/thejmthon/jmbot.git /root/Turbo_ismaz

WORKDIR /root/Turbo_ismax

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/jmrobot/bin:$PATH"

CMD ["python3","-m","Turbo_ismax"]
