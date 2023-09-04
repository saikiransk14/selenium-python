import logging


def log_detail():
    logging.basicConfig(
        filename="logdemo.py",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p'
    )
    return logging.getLogger()


logger = log_detail()
logger.info("program execution started")

a = 4
b = 3
if a > b:
    print("sai")
    logger.info("a is greater than b hence got printed in output")

logger.info("program execution ended")
2023-08-29 10:01:16 AM - INFO - program execution started
2023-08-29 10:01:16 AM - INFO - a is greater than b hence got printed in output
2023-08-29 10:01:16 AM - INFO - program execution ended
