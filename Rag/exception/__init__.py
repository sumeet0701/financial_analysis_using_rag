import sys

class RagException(Exception):
    """Custom exception class for raising and handling errors with detailed information."""

    def __init__(self, error_message: Exception):
        """Initialize the exception with the given error message."""
        self.error_message = self.get_detailed_error_message(error_message)

    @staticmethod
    def get_detailed_error_message(error_message: Exception) -> str:
        """
        Obtain a detailed error message, including file name, line numbers, and the original exception message.

        Args:
            error_message: The original exception object.

        Returns:
            A formatted string containing detailed error information.
        """

        _, _, exec_tb = sys.exc_info()
        file_name = exec_tb.tb_frame.f_code.co_filename
        try_block_line_number = exec_tb.tb_lineno
        exception_block_line_number = exec_tb.tb_frame.f_lineno

        return f"""
                Error occurred in script: [{file_name}] at
                try block line number: [{try_block_line_number}] exception block line number: [{exception_block_line_number}]
                Error message: [{error_message}]
            """

    def __str__(self) -> str:
        """Return the detailed error message as a string."""
        return self.error_message

    def __repr__(self) -> str:
        """Return a string representation of the exception class name."""
        return self.__class__.__name__