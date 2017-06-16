from elizabeth import Personal
import random
import datetime

person = Personal('zh')
data = open("data", "w", encoding='GB18030')
worker = 0


def employee():
    query = "insert into Workshop_employee" \
          "(eName, eSex, eAge, position, way, techGrading, dateOfAdmission, cNumber_id) " \
          "values" \
          "('{}', '{}', {}, '{}', '{}', '{}', '{}', {});\n"
    for i in range(1, 36):
        num = random.randint(60, 120)

        data.write(query.format(
            person.full_name(gender=random.choice(["male", "female"])),
            random.choice(["男", "女"]),
            random.randint(20, 50),
            '车间主任',
            '劳务工',
            random.choice(['无', '高级', '中级', '普通']),
            str(random.randint(2000, 2017)) + '-' + str(random.randint(1, 12)) + '-' + str(random.randint(1, 28)),
            i
        ))
        global worker
        worker = worker + 1

        for j in range(1, int(num / 20)):
            data.write(query.format(
                person.full_name(gender=random.choice(["male", "female"])),
                random.choice(["男", "女"]),
                random.randint(20, 50),
                '车间管理人员',
                '劳务工',
                random.choice(['无', '高级', '中级', '普通']),
                str(random.randint(2000, 2017)) + '-' + str(random.randint(1, 12)) + '-' + str(random.randint(1, 28)),
                i
            ))
            worker = worker + 1

        for j in range(1, int(num / 10)):
            data.write(query.format(
                person.full_name(gender=random.choice(["male", "female"])),
                random.choice(["男", "女"]),
                random.randint(20, 50),
                '班长',
                '劳务工',
                random.choice(['无', '高级', '中级', '普通']),
                str(random.randint(2000, 2017)) + '-' + str(random.randint(1, 12)) + '-' + str(random.randint(1, 28)),
                i
            ))
            worker = worker + 1

        for j in range(1, num):
            data.write(query.format(
                person.full_name(gender=random.choice(["male", "female"])),
                random.choice(["男", "女"]),
                random.randint(20, 50),
                '普通职工',
                random.choice(['劳务工', '小时工']),
                random.choice(['无', '高级', '中级', '普通']),
                str(random.randint(2000, 2017)) + '-' + str(random.randint(1, 12)) + '-' + str(random.randint(1, 28)),
                i
            ))
            worker = worker + 1


def work():
    query = "insert into Workshop_work" \
            "(wDate, wHours, wOvertime, eNumber_id)" \
            "values" \
            "('{}', {}, {}, {});\n"

    for i in range(1, worker):
        now = datetime.datetime.now()
        for j in range(1, 120):
            temp = now + datetime.timedelta(days=-j)

            if temp.isoweekday() == 5 or temp.isoweekday() == 6:
                continue

            wHours = 0
            wOvertime = 0

            if random.uniform(0, 1) > 0.95:
                wHours = random.randint(0, 8)
            else:
                wHours = 8

            if wHours == 8 and random.uniform(0, 1) > 0.8:
                wOvertime = random.randint(0, 4)

            data.write(query.format(
                str(temp.year) + '-' + str(temp.month) + '-' + str(temp.day),
                str(wHours),
                str(wOvertime),
                str(i)
            ))


def depot():
    query = "insert into Workshop_depot" \
            "(dType)" \
            "values" \
            "('{}');\n"
    for i in range(1, 100):
        data.write(query.format(
            random.choice(['产品仓库', '原料仓库'])
        ))


def provider():
    query = "insert into Workshop_provider" \
            "(pName)" \
            "values" \
            "('{}');\n"

    for i in range(1, 200):
        data.write(query.format(
            person.university()
        ))


def product():
    query = "insert into Workshop_product" \
            "(pName)" \
            "values" \
            "('{}');\n"

    for i in range(1, 100000):
        data.write(query.format(
            person.occupation()
        ))


def material():
    query = "insert into Workshop_material" \
            "(pNumber_id, dNumber_id, dName, dPrice)" \
            "values" \
            "({}, {}, '{}', {});\n"

    for i in range(1, 1000):
        data.write(query.format(
            str(random.randint(1, 199)),
            str(random.randint(1, 99)),
            person.favorite_movie(),
            str(random.randint(10, 50))
        ))


def usage():
    query = "insert into Workshop_usage" \
            "(cNumber_id, mNumber_id, uDate, uAmount)" \
            "values" \
            "({}, {}, '{}', {});\n"

    now = datetime.datetime.now()
    for k in range(1, 7):
        for i in range(1, 120):
            temp = now + datetime.timedelta(days=-i)

            if temp.isoweekday() == 5 or temp.isoweekday() == 6:
                continue

            for j in range(1, 1000):
                data.write(query.format(
                    str(k),
                    str(j),
                    str(temp.year) + '-' + str(temp.month) + '-' + str(temp.day),
                    str(random.randint(0, 100))
                ))


def produce():
    query = "insert into Workshop_produce" \
            "(cNumber_id, pNumber_id, dNumber_id, pDate, pWeight, pUsed)" \
            "values" \
            "({}, {}, {}, '{}', {}, {});\n"
    for i in range(1, 8):
        now = datetime.datetime.now()
        for j in range(1, 120):
            temp = now + datetime.timedelta(days=-j)

            if temp.isoweekday() == 5 or temp.isoweekday() == 6:
                continue

            data.write(query.format(
                str(i),
                str(random.randint(1, 99999)),
                str(random.randint(1, 99)),
                str(temp.year) + '-' + str(temp.month) + '-' + str(temp.day),
                str(random.randint(1, 10)),
                str(random.randint(10, 25))
            ))


employee()
data.write('\n')
work()
data.write('\n')
depot()
data.write('\n')
provider()
data.write('\n')
product()
data.write('\n')
material()
data.write('\n')
usage()
data.write('\n')
produce()
data.write('\n')
