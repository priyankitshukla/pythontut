name={
    "name":"Priyankit",
    "organization":"30",
    "age":40
}

for resource in name:
    print(resource)


records= [
    {
        "name":"Priyankit",
        "organization":"30",
        "age":40
    },
    {
        "name":"HCL",
        "organization":"HCL",
        "age":42
    }
    ]

for record in records:
    print(record)
    print(record.get('name'))