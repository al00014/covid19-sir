#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from pathlib import Path
from covsirphy import Population


def main():
    # Create output directory in example directory
    code_path = Path(__file__)
    output_dir = code_path.with_name("output").joinpath(code_path.stem)
    output_dir.mkdir(exist_ok=True, parents=True)
    # Read population dataset
    pop_file = "input/locations_population.csv"
    pop = Population(pop_file)
    # Show the cleaned data as a CSV file
    pop_df = pop.cleaned()
    pop_df.to_csv(output_dir.joinpath("cleaned.csv"), index=False)
    # Show as a dictionary in country level
    pop_dict = pop.to_dict()
    with output_dir.joinpath("dictionary_country.json").open("w") as fh:
        json.dump(pop_dict, fh, indent=4)
    # Show as a dictionary in province level
    pop_province_dict = pop.to_dict(country_level=False)
    with output_dir.joinpath("dictionary_province.json").open("w") as fh:
        json.dump(pop_province_dict, fh, indent=4)


if __name__ == "__main__":
    main()
