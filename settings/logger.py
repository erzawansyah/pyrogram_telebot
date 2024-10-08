import logging
import colorlog


class BotLogger:

    def __init__(
        self,
        name: str = "bot_logger",
        level: int = logging.INFO,
        format: str = "[%(log_color)s%(levelname)s%(reset)s] %(asctime)s %(log_color)s%(name)s:%(reset)s %(message)s",
    ):
        self.logger = logging.getLogger(name.upper())
        self.logger.setLevel(level)

        # Check if the logger already has handlers to prevent duplicate logs
        if not self.logger.hasHandlers():
            # Create a console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)

            # Create a color formatter and set it for the handler
            color_formatter = colorlog.ColoredFormatter(
                format,
                log_colors={
                    "DEBUG": "cyan",
                    "INFO": "green",
                    "WARNING": "yellow",
                    "ERROR": "red",
                    "CRITICAL": "bold_red",
                },
                secondary_log_colors={
                    "message": {
                        "DEBUG": "cyan",
                        "INFO": "green",
                        "WARNING": "yellow",
                        "ERROR": "red",
                        "CRITICAL": "bold_red",
                    }
                },
            )
            console_handler.setFormatter(color_formatter)

            # Add the handler to the logger
            self.logger.addHandler(console_handler)

    def info(self, message: str):
        """
        Log an informational message.

        Args:
            message (str): The message to log.
        """
        self.logger.info(message)

    def error(self, message: str):
        """
        Log an error message.

        Args:
            message (str): The message to log.
        """
        self.logger.error(message)

    def warning(self, message: str):
        """
        Log a warning message.

        Args:
            message (str): The message to log.
        """
        self.logger.warning(message)


# Example usage
if __name__ == "__main__":
    logger = BotLogger()
    logger.info("This is an info message.")
    logger.error("This is an error message.")
    logger.warning("This is a warning message.")
