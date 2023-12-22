from string import Template

import mindsdb_sdk
from mindsdb_sdk.server import Databases, Server
from pandas import DataFrame
from requests.exceptions import ConnectionError, HTTPError

MINDSDB_HOST = "https://cloud.mindsdb.com"

SQL_ASK_QUERY = Template(
    """
SELECT response
FROM mindsdb.gpt_model
WHERE text = "$text";
"""
)


def to_data(dataframe: DataFrame) -> str:
    """
    takes a pandas `DataFrame` and returns the first value from the first column
    Args:
        dataframe: the dataframe returned from MindsDB that stores the answer in the first cell of column

    Returns:
        first value of the first column of dataframe that MindsDB responses
    """
    return dataframe.iloc[:, 0].values[0]


class MindsDB:
    """
    MindsDB manager class
    """

    def __init__(self, email: str, password: str) -> None:
        """
        initializer class.
        Args:
            email: MindsDB account email address (that is stored as an env var)
            password: MindsDB account password
        """
        self.email = email
        self.password = password

        self.is_authenticated: bool = False
        self.database: Databases

    def authenticate(self) -> None:
        """
        authorizes the email and password with MindsDB's host
        """

        try:
            server = mindsdb_sdk.connect(
                MINDSDB_HOST,
                login=self.email,
                password=self.password,
            )
        except HTTPError:
            raise Exception(
                "Email or password is incorrect. Make sure to enter the right credentials."
            )
        except ConnectionError:
            raise Exception("Make sure you have access to the internet and try again.")

        self.is_authenticated = True
        self.database = self.collect_database(server)

    @staticmethod
    def collect_database(server: Server) -> Databases:
        return server.list_databases()[0]

    def answer(self, text: str) -> str:
        """
        takes the question and queries then converts the response into `rich.Markdown`
        Args:
            question: the value from `ask` positional argument

        Returns:
            response from MindsDB in Markdown format
        """

        return to_data(
            self.database.query(
                SQL_ASK_QUERY.substitute(
                    text=text,
                )
            ).fetch()
        )
