import argparse
import os
import random
from pathvalidate import sanitize_filename

def assign(participants):
    while True:
        unchosen = list(participants)
        matches = {}
        try:
            for participant in participants:
                valid = [candidate for candidate in unchosen if candidate != participant]
                if not valid:
                    raise ValueError("No candidates left")
                chosen = random.choice(valid)
                matches[participant] = chosen
                unchosen.remove(chosen)
            return matches
        except ValueError:
            continue  # restart if hungry assignment results in error

def write_matches_to_file(matches, output_directory_name):
    try:
        os.mkdir(output_directory_name)
        print(f"Directory '{output_directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{output_directory_name}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{output_directory_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    for participant in matches:
        filename = sanitize_filename(participant.replace(" ", "_") + ".txt")
        filename = output_directory_name + "/" + filename

        with open(filename, "w") as f:
            f.write(matches[participant])

def main():
    parser = argparse.ArgumentParser(description="Secret Santa participant matcher")

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        "participants",
        nargs="?",
        type=str,
        help="Comma-separated list of participants."
    )

    group.add_argument(
        "-f", "--file",
        type=str,
        help="Read participant list from file. One participant per line."
    )

    group.add_argument(
        "-o", "--output",
        action="store_true",
        help="Directory to output files."
    )
    
    args = parser.parse_args()

    participants = set()

    if args.file:
        with open(args.file, "r") as f:
            for name in f:
                participants.add(name.strip())
    else:
        names = args.participants.split(',')
        for name in names:
            participants.add(name)

    if len(participants) <=1:
        print("More than one participant is required.")
        exit(1)
       

    matches = assign(participants=participants)

    if args.output:
        write_matches_to_file(matches=matches,output_directory_name=args.output)
    else:
        for participant in matches:
            print(f'{participant}:\t{matches[participant]}')
    


if __name__ == "__main__":
    main()