import logging

logging.basicConfig(
    filename="reports/logs/test_execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()
