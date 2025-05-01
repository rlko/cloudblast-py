# CloudBlast API Python Wrapper

An unofficial Python wrapper for the CloudBlast API that provides an easy-to-use interface for interacting with CloudBlast's services.

## Documentation

For detailed API documentation, visit [CloudBlast API Documentation](https://docs.cloudblast.io/).

## Installation

```bash
pip install cloudblast-py
```

## Usage

```python
from cloudblast_py import CloudBlast

# Initialize the client with your API key
client = CloudBlast(api_key="your_api_key")

# Create a new server
server = client.create_server(
    plan_id=1,
    location_id=1,
    hostname="my-server",
    template_uuid="your-template-uuid"
)

print(f"Created server with ID: {server['id']}")
```

## Features

- Create new servers
- Manage server actions
- Delete servers
- Add/remove extra IPs
- Get server details
- List all servers

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