from PySide6.QtCore import QMutex

from models.logger.log import Log
from models.logger.constants import MAX_BUFFER_SIZE


class LogBuffer:
    MAX_BUFFER_SIZE = MAX_BUFFER_SIZE

    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0
        self._lock = QMutex()

    def add(self, log: Log):
        """
            Add a log to the buffer.
            :param log: Log to add.
        """
        self._lock.lock()
        if self._length == self.MAX_BUFFER_SIZE:
            raise BufferError("Buffer is full")
        if self.head is None:
            self.head = log
            self.tail = log
        else:
            current = self.tail
            # find the correct position based on time created, head (oldest) -> tail (newest)
            while current is not None and current > log:
                if log == current:
                    self._lock.unlock()
                    return
                current = current.previous
            if current is None:
                # log is the oldest
                self.head.previous = log
                log.next = self.head
                self.head = log
                if self.head.next.next is None:
                    # only two logs in buffer -> update tail
                    self.tail = self.head.next
            else:
                # log is somewhere in the middle or the newest
                tmp = current.next
                current.next = log
                log.previous = current
                log.next = tmp
                if tmp is None:
                    # log is the newest -> update tail
                    self.tail = log
                else:
                    tmp.previous = log
        self._length += 1
        self._lock.unlock()

    def get(self):
        """
            Get the oldest log from the buffer.
        """
        self._lock.lock()
        if self.head is None:
            self._lock.unlock()
            return None
        log = self.head
        self.head = self.head.next
        self._length -= 1
        if self.head is not None:
            self.head.previous = None
        else:
            self.tail = None
        if self._length == 1:
            self.tail = self.head
        self._lock.unlock()
        return log

    def clear(self):
        """
            Clear the buffer.
        """
        self._lock.lock()
        self.head = None
        self.tail = None
        self._length = 0
        self._lock.unlock()

    def __len__(self):
        return self._length

    def __str__(self):
        self._lock.lock()
        current = self.head
        string = ""
        while current is not None:
            string += str(current) + "\n"
            current = current.next
        self._lock.unlock()
        return string

    def dump_to_file(self, file_path):
        """
            Dump the buffer to a file.
        """
        self._lock.lock()
        current = self.head
        log_text = ""
        while current is not None:
            log_text += str(current) + "\n"
            current = current.next
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(log_text)
        self.head = None
        self.tail = None
        self._lock.unlock()
