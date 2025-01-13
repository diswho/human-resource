# Report

## Department Info

- Get list of Department, tree structure, JSON format.
- Each node of tree include descendants id.

## Diagram

```mermaid
sequenceDiagram
  participant Alice
  participant Bob
  participant Charlie

  Alice->>Bob: Hello Bob, how are you?
  activate Bob
  Bob->>Alice: I am fine, thank you!
  deactivate Bob
  Alice-->>Charlie: Hello Charlie, how are you?
  activate Charlie
  Charlie-->>Alice: I am great, thanks!
  deactivate Charlie
```

# User

```bash
FIRST_SUPERUSER=admin@example.com
```

```bash
FIRST_SUPERUSER_PASSWORD=I536ib9E6HVxgc
```

```console
$ uvicorn backend.app.main:app --reload
```
