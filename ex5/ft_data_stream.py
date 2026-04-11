import typing
import random

name = [
    'bob',
    'alice',
    'dylan',
    'charlie'
]

action = [
    'run',
    'eat',
    'sleep',
    'grab',
    'move',
    'climb',
    'swim',
    'release'
]


def gen_counter() -> typing.Generator[int]:
    nb = 0
    while True:
        yield nb
        nb += 1


def gen_event() -> typing.Generator[tuple]:
    while True:
        yield (random.choice(name), random.choice(action))


def consume_event(event_list) -> typing.Generator[tuple, list]:
    new_event_list = [event for event in event_list]
    while (len(new_event_list) > 0):
        got_event = random.choice(new_event_list)
        new_event_list = [e for e in new_event_list if e != got_event]
        yield got_event, new_event_list


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    event = gen_event()
    event_nb = gen_counter()

    for nb in range(1000):
        p = next(event)
        print(f"Event {next(event_nb)}: Player {p[0]} did action {p[1]}")

    event_list = [next(event) for nb in range(10)]
    print(f"Build list of 10 events: {event_list}")

    pop_event_list = consume_event(event_list)
    for x in range(9):
        event, event_list = next(pop_event_list)
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")
