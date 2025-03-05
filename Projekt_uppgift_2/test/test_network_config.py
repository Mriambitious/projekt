
#Inshallah ramadan mubarak
# tests/test_network_config.py

import pytest
from network_config_manager import NetworkConfigManager

# Fixture skapar en instans för att kunna komincera i NetworkConfigManager och ansluta till servern
@pytest.fixture
def network_config_manager():
    manager = NetworkConfigManager()
    manager.connect()
    # Återställer konfigurationsvärden till utgångsläge
    manager.update_hostname("1")
    manager.update_interface_state("down")
    manager.update_response_prefix("Standard Response")
    yield manager
    # Stänger SSH-anslutningen efter varje test
    manager.disconnect()

# Testar o verifiera standardvärden efter grund start walla är rätt.
def test_show_host_name(network_config_manager):
    """Testar att show_host_name returnerar rätt värde efter grund start walla."""
    assert network_config_manager.show_host_name() == "hostname: 1"

def test_show_interface_state(network_config_manager):
    """Testar att show_interface_state returnerar rätt värde efter setup."""
    assert network_config_manager.show_interface_state() == "interface_state: down"

def test_show_response_prefix(network_config_manager):
    """Testar att show_response_prefix returnerar rätt värde efter grund start walla."""
    assert network_config_manager.show_response_prefix() == "response_prefix: Standard Response"

# Test om man man vill verifiera o uppdatering av inställningar så som hostnam o ikande
def test_update_hostname(network_config_manager):
    """Testar att uppdatera hostname overifierar att ändringen har slagit igenom."""
    network_config_manager.update_hostname("new_hostname")
    assert network_config_manager.show_host_name() == "hostname: new_hostname"

def test_update_interface_state(network_config_manager):
    """Testar att uppdatera interface_state och verifierar att ändringen har gått igenom."""
    network_config_manager.update_interface_state("up")
    assert network_config_manager.show_interface_state() == "interface_state: up"

def test_update_response_prefix(network_config_manager):
    """Testar att uppdatera response_prefix och verifierar att ändringen har gått igenom."""
    network_config_manager.update_response_prefix("New Response")
    assert network_config_manager.show_response_prefix() == "response_prefix: New Response"

# Test för att verifiera att ett ogiltigt värde för interface_state kastar ett exception
def test_invalid_interface_state(network_config_manager):
    """Testar att ett ogiltigt värde för interface_state kastar ett exception."""
    with pytest.raises(ValueError):
        network_config_manager.update_interface_state("invalid_state")

#mashallah pliz run program