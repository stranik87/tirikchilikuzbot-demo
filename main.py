import time
from .handlers import (
    get_last_update,
)


def main():
    # get last update
    last_update = get_last_update()
    # get last update_id
    last_update_id = last_update['update_id']

    # infinite loop
    while True:
        # get new update
        new_update = get_last_update()

        # get new update_id
        new_update_id = new_update['update_id']

        # check if new update_id is not equal to last update_id
        if new_update_id != last_update_id:
            # do something
            pass

        # set last update_id to new update_id
        last_update_id = new_update_id

        # sleep for 1 second
        time.sleep(1)

main()
