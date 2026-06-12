from dagster import asset, Definitions

# Asset 1
@asset
def raw_data():
    data = [1, 2, 3, 4, 5]
    print(f"Raw Data: {data}")
    return data


# Asset 2
@asset
def doubled_data(raw_data):
    result = [x * 2 for x in raw_data]
    print(f"Doubled Data: {result}")
    return result


# Asset 3
@asset
def total_sum(doubled_data):
    total = sum(doubled_data)
    print(f"Total Sum: {total}")
    return total


