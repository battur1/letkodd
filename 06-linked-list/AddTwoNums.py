from LinkedList import LinkedList


class AddTwoNums(object):
    def addTwoNumbers(self, l1, l2):
        dum = LinkedList(0)
        cur = dum
        car = 0

        while l1 or l2 or car:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + car

            car = total // 10
            digit = total % 10

            cur.next = LinkedList(digit)
            cur = cur.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dum.next

if __name__ == "__main__":
    l1 = LinkedList(2, LinkedList(4, LinkedList(3)))
    l2 = LinkedList(5, LinkedList(6, LinkedList(4)))
    result = AddTwoNums().addTwoNumbers(l1, l2)

    values = []
    while result:
        values.append(result.val)
        result = result.next

    print(values)