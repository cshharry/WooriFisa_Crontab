from faker import Faker
import csv
import time
import os

# Faker 객체 생성
fake = Faker('ko_KR')  # 한국어 설정

# 데이터 생성 함수
def generate_fake_data(num_entries):
    data = []
    for _ in range(num_entries):
        name = fake.name()  # 가짜 한글 이름 생성
        likes = fake.random_int(min=0, max=1000)  # 0부터 1000 사이의 가짜 좋아요 수 생성
        data.append([name, likes])
    return data

# 파일에 데이터 추가 함수
def append_to_csv(file_name, data):
    file_exists = os.path.isfile(file_name)
    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Name', 'Likes'])  # 헤더 작성 (파일이 없을 때만)
        writer.writerows(data)  # 데이터 추가

# 데이터 생성 및 주기적 저장
if __name__ == "__main__":
    num_entries_per_cycle = 10  # 한 번에 생성할 데이터 수
    file_name = 'fake_data.csv'

    while True:
        fake_data = generate_fake_data(num_entries_per_cycle)
        append_to_csv(file_name, fake_data)
        print(f"{num_entries_per_cycle}개의 가짜 데이터가 '{file_name}' 파일에 추가되었습니다.")
        time.sleep(1)  # 1초 대기

