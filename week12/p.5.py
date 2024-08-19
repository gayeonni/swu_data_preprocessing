import agate

# csv into agate table
capture = agate.Table.from_csv("capture.csv")
boar = agate.Table.from_csv("boar.csv")

print(capture)
print(boar)

# join
# joined_table = capture.join(boar, 'key_people', 'key_boar', inner=True)  # inner join
# joined_table = capture.join(boar, 'key_people', 'key_boar')  # left outer join
# joined_table = capture.join(boar, 'key_people', 'key_boar', full_outer=True)  # full outer join

print(joined_table)
for r in joined_table.rows:
    print(r['key_people'], r['지역'], r['월'], r['지역2'], r['월2'], r['인원'], r['포획수'])
