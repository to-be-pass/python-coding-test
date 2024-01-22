FROM python:3.8

WORKDIR /

# COPY tests/ /tests
COPY src/ /src
COPY requirements.txt /requirements.txt
COPY pytest.ini /pytest.ini

RUN pip install -r requirements.txt

# main 의 테스트코드 가져오기
RUN git clone --single-branch --branch main https://github.com/to-be-pass/python-coding-test.git /tmp/repo && \
    mv /tmp/repo/tests /tests && \
    rm -rf /tmp/repo

ARG TEST_ID=""
ENV TEST_ID=${TEST_ID}

ARG TEST_NUM=""
ENV TEST_NUM=${TEST_NUM}

CMD sh -c "pytest --id=$TEST_ID -k '$TEST_NUM'"
