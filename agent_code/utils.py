import csv
import random
from dataclasses import dataclass
from typing import List


@dataclass
class Agent:
    email: str
    first: str
    last: str
    uid: str


def ingest(csv_file: str) -> List[Agent]:
    '''
    Ingest agents
    :param csv_file:
    :return:
    '''
    with open(csv_file) as csvfile:
        next(csvfile, None)  # skip header
        agentreader = csv.reader(csvfile)
        agents = [Agent(agent[0], agent[1], agent[2], agent[3]) for agent in agentreader]

    return agents


def domain_from_email(email: str) -> str:
    """
    parse the domain from the email
    :param email:
    :return:
    """
    name, domain = email.split("@")
    elements = domain.split(".")
    return elements[0]


def extract_random_letters(input_string):
    if len(input_string) < 3:
        return "Input string is too short"

    random_indices = random.sample(range(len(input_string)), 3)
    random_letters = [input_string[i] for i in random_indices]
    result = ''.join(random_letters)

    return result


def make_uid(domain: str) -> str:
    """
    make a UID i.e. AG-XYX from domain name
    :param domain:
    :return:
    """
    uid = extract_random_letters(domain)
    return f'AG-{uid.upper()}'


def domain_exists(email: str, csv_file: str) -> bool:
    """
    True if an email with a domain already exists for the given email
    :param email:
    :return:
    """
    domain = domain_from_email(email)
    agents = ingest(csv_file)
    emails = [agent.email for agent in agents]
    domains = list((domain_from_email(email) for email in emails))

    return domain in domains


def uid_from_email(email: str, csv_file: str) -> str:
    """
    create a uniqe uid from email
    :param email:
    :return:
    """

    # check if domain exists and exit if required
    print(f"EMAIL: {email}")

    domain = domain_from_email(email)
    print(f"DOMAIN: {domain}")
    if domain_exists(email, csv_file):
        print(f"emails exist for domain {domain}")
        agents = ingest(csv_file)
        matches = [agent.email for agent in agents if domain in agent.email]
        for match in matches:
            print(f"- {match}")
        user_input = input("Continue? (Y/n)").strip().lower()
        if user_input == 'n':
            print("Exiting")
            exit()


    agents = ingest(csv_file)
    uids = [agent.uid for agent in agents]
    is_unique = False
    while not is_unique:
        uid = make_uid(domain)
        is_unique = not (uid in uids)

    return uid
