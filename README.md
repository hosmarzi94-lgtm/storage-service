# Storage Service

## Overview

Storage Service is a lightweight abstraction layer for storing and retrieving application assets across multiple storage backends. It provides a unified interface that allows the application to switch between different storage implementations without changing business logic.

## Supported Backends

* Local filesystem storage
* Cloud object storage
* Hybrid storage (experimental)

## Design

The storage layer is designed around a backend adapter interface. Client code interacts with a single storage API while backend-specific implementations handle the underlying storage operations.

## Production Notes

The hybrid backend was introduced to support future scalability and improved reliability. However, deployment environments may use different storage configurations depending on operational requirements and migration status.

## Development

Run tests with:

```bash
pytest
```

The default backend is determined by the application configuration and should remain consistent with the deployment environment.
