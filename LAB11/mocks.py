from unittest.mock import Mock

json = Mock()
json.loads('{"key": "value"}')
json.loads('{"key": "value"}')
json.loads('{"key": "value"}')
json.loads('{"key": "value"}')




json.loads.assert_called()
json.loads.assert_called_once()
json.loads.assert_called_with('{"key": "value"}')
json.loads.assert_called_once_with('{"key": "value"}')