"""
Merge k sorted lists



"""


def merge_k_lists(lists):
    """Merge k lists."""
    start = None

    if not lists:
        return start

    lists = [
        pair[1]
        for pair in sorted(
            [(list_.val, list_) for list_ in lists if list_], key=lambda pair: pair[0]
        )
    ]
    if not lists:
        return start

    def insert_into_lists(list_):
        """Insert pair into list values."""
        if list_ is None:
            return

        if not lists:
            lists.append(list_)
            return

        if lists[0].val >= list_.val:
            lists.insert(0, list_)
            return

        if lists[-1].val <= list_.val:
            lists.append(list_)
            return

        a: int = 0
        b: int = len(lists)
        while b - a > 1:
            guess = int((a + b) // 2)
            if lists[guess].val == list_.val:
                lists.insert(guess + 1, list_)
                return
            if list_.val > lists[guess].val:
                a = guess
            else:
                b = guess

        lists.insert(b, list_)

    start = current = lists.pop(0)
    insert_into_lists(current.next)

    while lists:
        print(current)
        current.next = lists.pop(0)
        current = current.next
        insert_into_lists(current.next)

    return start
