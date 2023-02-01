import psycopg
from src.settings import DB_DATABASE, DB_HOST, DB_PASSWORD, DB_PORT, DB_USER


CONN_INFO = f"dbname={DB_DATABASE} user={DB_USER} port={DB_PORT} host={DB_HOST} password={DB_PASSWORD}"


async def get_conn_async(query: str):
    async with await psycopg.AsyncConnection.connect(conninfo=CONN_INFO) as async_conn:
        async with async_conn.cursor() as async_cursor:
            records = await async_cursor.execute(query)
            column_names = list(map(lambda x: x.lower(), [
                d[0] for d in records.description]))
            rows = list(await records.fetchall())
            output = [dict(zip(column_names, row)) for row in rows]
            return output


async def insert_conn_async(query: str):
    async with await psycopg.AsyncConnection.connect(conninfo=CONN_INFO) as async_conn:
        async with async_conn.cursor() as async_cursor:
            await async_cursor.execute(query)
            return "QUERY SUCCESS"


def get_conn():
    connection = psycopg.connect(conninfo=CONN_INFO)
    return connection


connection = get_conn()


def get_data_db(query: str):
    cursor = connection.cursor()
    cursor.execute(query)
    column_names = list(map(lambda x: x.lower(), [
        d[0] for d in cursor.description]))
    rows = list(cursor.fetchall())
    output = [dict(zip(column_names, row)) for row in rows]
    return output
