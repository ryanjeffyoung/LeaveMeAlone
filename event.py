
class Event:
    def __init__(self, start, end):
        """
        initializes event node with start and end time stored as Data
        """
        self.data = {
            'start': start,
            'end': end,
        }
        self.next = None
        return
    
    def output(self):
        """
        formats and returns start and end time
        """
        start_str = 'Start: ' + str(self.data['start'])
        end_str = 'End: ' + str(self.data['end'])
        both = start_str + ' | ' + end_str
        return(both)

class SLL:
    def __init__(self):
        """
        instantiation of object
        """
        self.head = None
        self.tail = None
        return

    def add(self, start, end):
        """
        creates new event & adds to end of list

        start -- start of event
        end -- end of event
        """
        new_event = Event(start, end)

        if self.head is None:
            self.head = new_event
            return
        
        h = self.head
        while h.next is not None:
            h = h.next
        h.next = new_event

    def del_head(self):
        curr = self.head
        if curr is not None:
            self.head = curr.next
        else:
            self.head = None
        return

    def get_head(self):
        return self.head
        
    def add_head(self, item):
        """
        adds item to front of list

        item -- item to be added
        """
        item.next = self.head
        self.head = item

    def add_tail(self, start, end):
        """
        adds item to end of list

        item -- item to be added
        """
        new_event = Event(start, end)

        if self.head is None:
            self.head = new_event
        else:
            self.tail.next = new_event

        self.tail = new_event

        return
    
        
    def list_length(self):
        count = 0
        curr_node = self.head

        while curr_node is not None:
            count = count + 1

            curr_node = curr_node.next
        
        return count

    def output_list(self):
        curr_node = self.head

        while curr_node is not None:
            print(curr_node.output())
            curr_node = curr_node.next 
        
        return


