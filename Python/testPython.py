import sys
import time
import logging

# Create a logger
#logger = logging.getLogger('my_logger')
#logger.setLevel(logging.INFO)

# Create a stream handler
#class FlushStreamHandler(logging.StreamHandler):
#    def emit(self, record):
#        super().emit(record)
#        self.flush()

#buffering = 1 means line buffering, i.e console output is flushed after each line, i.e. it can be read externally
#sys.stdout = open(sys.stdout.fileno(), mode='w', buffering=1, encoding='cp1252', closefd=False)
#sys.stderr = open(sys.stderr.fileno(), mode='w', buffering=1, encoding='cp1252', closefd=False)

# Create a stream handler
#stream_handler = FlushStreamHandler(sys.stdout)
#stream_handler.setLevel(logging.INFO)

# Create a formatter and set it for the handler
#formatter = logging.Formatter('%(message)s')
#stream_handler.setFormatter(formatter)
#
# Add the handler to the logger
#logger.addHandler(stream_handler)

if __name__ == '__main__':
    print('Starting')
    sys.stdout.flush()
    time.sleep(5)
    print('After 1s : Test, args : ')
    sys.stdout.flush()
    for arg in sys.argv[1:]:
        time.sleep(1)
        print(arg)
        sys.stdout.flush()

