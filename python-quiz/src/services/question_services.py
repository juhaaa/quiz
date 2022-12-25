def question_service(connection):
    """Gets country data from database table Countries.

    Args:
        Connection: db connection
    Returns:
        List: Country, cca2, Capital
    """
    data = connection.execute(
        """SELECT *
        FROM Countries
        ORDER BY RANDOM()
        LIMIT 1"""
        ).fetchall()
    return data


def additional_answers(cca2, connection):
    """Provided with countrys cca2- code and db- connection,
    returns 3 random cities (if possible), located in that country.

    Args:
        str : Country code
        Connection: db connection
    Returns:
        List: cities
    """
    data = connection.execute(
        """SELECT Cities.name
        FROM Cities, Countries
        WHERE Cities.cca2=? AND Cities.cca2=Countries.cca2
        AND Countries.capital<>Cities.name
        ORDER BY RANDOM() LIMIT 3""",
        [cca2]).fetchall()
    return data

# provides more answers from random countries,
# amount depending how many was originally acquired
# (in case theres not enough cities in the country etc...)

def more_additional_answers(amount, connection):
    """Provides more answer cities from random countries,
    amount depending how many was originally acquired
    (in case theres not enough cities in the country etc...)

    Args:
        int: Amount of cities needed
        Connection: db connection
    Returns:
        List: cities
    """

    data = connection.execute(
        """SELECT Cities.name
        FROM Cities, Countries
        WHERE Countries.cca2=Cities.cca2 AND Countries.capital<>Cities.name
        ORDER BY RANDOM() LIMIT ?""",
        [amount]).fetchall()
    return data
