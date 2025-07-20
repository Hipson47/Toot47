import pytest
from unittest.mock import patch, MagicMock
from src.toot47.qa import GraphAgent

@patch('src.toot47.qa.GraphQAChain')
@patch('src.toot47.qa.ChatOpenAI')
@patch('src.toot47.qa.Neo4jGraph')
def test_graph_agent_ask(MockNeo4jGraph, MockChatOpenAI, MockGraphQAChain):
    """Tests that GraphAgent.ask returns a string."""
    
    # Arrange
    mock_chain_instance = MagicMock()
    mock_chain_instance.run.return_value = "This is a test answer."
    MockGraphQAChain.from_llm.return_value = mock_chain_instance

    agent = GraphAgent()
    
    # Act
    question = "What is a test?"
    answer = agent.ask(question)
    
    # Assert
    assert isinstance(answer, str)
    assert answer == "This is a test answer."
    mock_chain_instance.run.assert_called_once_with(question)

def test_placeholder():
    """ Placeholder test to ensure pytest runs. """
    assert True 