import csv


def read_wimbledon_data(filename):
    champions = {}
    countries = set()

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)

        # Skip the header row
        next(reader)

        for row in reader:
            if len(row) != 6:
                print(f"Skipped row with unexpected format: {row}")
                continue

            year, champion_country, champion, runnerup_country, runnerup, score = row

            if champion in champions:
                champions[champion] += 1
            else:
                champions[champion] = 1

            countries.add(champion_country)

    return champions, countries


def display_champions(champions):
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")


def display_countries(countries):
    sorted_countries = sorted(countries)
    country_str = ", ".join(sorted_countries)
    print("\nThese countries have won Wimbledon:", country_str)


def main():
    champions, countries = read_wimbledon_data("wimbledon.csv")
    display_champions(champions)
    display_countries(countries)


if __name__ == "__main__":
    main()
