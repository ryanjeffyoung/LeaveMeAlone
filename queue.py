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

class Queue: 
      
    def __init__(self): 
        self.front = self.rear = None
  
    def isEmpty(self): 
        return self.front == None
      
    # Method to add an item to the queue 
    def EnQueue(self, start, end): 
        temp = Event(start, end) 
          
        if self.rear == None: 
            self.front = self.rear = temp 
            return
        self.rear.next = temp 
        self.rear = temp 
  
    # Method to remove an item from queue 
    def DeQueue(self): 
          
        if self.isEmpty(): 
            return
        temp = self.front 
        self.front = temp.next
  
        if(self.front == None): 
            self.rear = None

    def output_list(self):
        curr_node = self.front

        while curr_node is not None:
            print(curr_node.output())
            curr_node = curr_node.next 
        
        

