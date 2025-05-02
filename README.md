# CloudBlast API Python Wrapper

An unofficial Python wrapper for the CloudBlast API that provides an easy-to-use interface for interacting with CloudBlast's services.

## Documentation

For detailed API documentation, visit [CloudBlast API Documentation](https://docs.cloudblast.io/).

## Quick Start

```python
from cloudblast_py import CloudBlast

# Initialize client
client = CloudBlast(api_key="your_api_key")

# Create a server
server = client.create_server(
    plan_id=19, # VMA11: 1 Core ~ 3.00 GB ~ 20.00 GB
    location_id=1, # Amsterdam
    hostname="my-server",
    template_uuid="d954c4df-1f64-419c-94fe-91bea556e5ad" # Ubuntu 24.04
)
```

## API Overview

### Server Management
- `create_server()` - Create a new server
- `delete_server()` - Delete a server
- `get_server_details()` - Get server information
- `list_servers()` - List all servers

### Server Actions
- `send_action_server()` - Send actions (start/stop/restart) to a server

### IP Management
- `add_extra_ip()` - Add an extra IP to a server
- `remove_extra_ip()` - Remove an extra IP from a server

## Installation

```bash
pip install git+https://github.com/rlko/cloudblast-py.git
```

## Usage

### Server Management

#### Create a Server
```python
server = client.create_server(
    plan_id=1,                    # Plan ID         See: https://docs.cloudblast.io/id-lists/plans-list
    location_id=1,                # Location ID          https://docs.cloudblast.io/id-lists/locations-list
    hostname="my-server",         # Server hostname
    template_uuid="template-uuid" # Template UUID        https://docs.cloudblast.io/id-lists/os-list
)
```

#### Delete a Server
```python
client.delete_server(server_id=123)
```

#### Get Server Details
```python
server_details = client.get_server_details(server_id=123)
```

#### List All Servers
```python
servers = client.list_servers()
```

### Server Actions

#### Send Action to Server
```python
# Available actions: 'start', 'stop', 'restart'
client.send_action_server(server_id=123, action="restart")
```

### IP Management

#### Add Extra IP
```python
client.add_extra_ip(server_id=123)
```

#### Remove Extra IP
```python
client.remove_extra_ip(server_id=123, ip_address="1.2.3.4")
```

## Configuration

Set your API key using environment variables:

```bash
export CLOUDBLAST_API_KEY="your_api_key"
```

Or pass it directly when initializing the client:

```python
client = CloudBlast(api_key="your_api_key")
```

## Development

For development, clone the repository and install in editable mode:

```bash
git clone https://github.com/rlko/cloudblast-py.git
cd cloudblast-py
pip install -e .
```

## License

MIT
