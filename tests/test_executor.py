from unittest.mock import patch, MagicMock
import pytest
import sqlite3
from src.sql_execution import SQL_Executor

@pytest.fixture
def mock_executor():
    with patch.object(SQL_Executor, '__init__', lambda self: None):
        executor = SQL_Executor()
        executor.conn = MagicMock()
        return executor

@patch('sqlite3.connect')
def test_connection_success(mock_connect):
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn
    executor = SQL_Executor()
    assert executor.conn == mock_conn
    mock_connect.assert_called_once()

@patch('sqlite3.connect', side_effect=sqlite3.Error("Connection failed"))
def test_connection_failure(_):
    with pytest.raises(sqlite3.Error, match="Connection failed"):
        SQL_Executor()

@patch('pandas.read_sql_query')
def test_execute_query(mock_read_sql, mock_executor):
    mock_df = MagicMock()
    mock_read_sql.return_value = mock_df

    result = mock_executor.execute_query("SELECT 1")

    mock_read_sql.assert_called_with("SELECT 1", mock_executor.conn)

    assert result == mock_df


def test_cleanup(mock_executor):
    assert mock_executor.cleanup() is True