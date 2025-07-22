import pytest
from unittest.mock import patch, MagicMock
from src.toot47.qa import GraphAgent

@patch('src.toot47.qa.settings')
@patch('src.toot47.qa.GraphCypherQAChain')
@patch('src.toot47.qa.ChatOpenAI')
@patch('src.toot47.qa.Neo4jGraph')
def test_graph_agent_ask(MockNeo4jGraph, MockChatOpenAI, MockGraphCypherQAChain, mock_settings):
    """Tests that GraphAgent.ask returns a string."""
    
    # Arrange
    mock_chain_instance = MagicMock()
    mock_chain_instance.invoke.return_value = {"result": "This is a test answer."}
    MockGraphCypherQAChain.from_llm.return_value = mock_chain_instance

    agent = GraphAgent()
    
    # Act
    question = "What is a test?"
    answer = agent.ask(question)
    
    # Assert
    assert isinstance(answer, str)
    assert answer == "This is a test answer."
    mock_chain_instance.invoke.assert_called_once_with({"query": question})

def test_placeholder():
    """ Placeholder test to ensure pytest runs. """
    assert True 