# Neo4j database snapshot

`neo4j.dump` is a snapshot of the application database, stored with Git LFS.
The `system` database, users, passwords, and server logs are not included.

- Created: 2026-10-14 (Asia/Seoul)
- Neo4j: `5.26-community`
- Source code commit before backup: `f9971ee65f7a78a88d06415feca0a3eb6e08152d`
- Verified by loading into a separate Docker volume.

Run these commands from the repository root in Linux/WSL with Docker and Git LFS installed.

## Download

```bash
git lfs install
git lfs pull
```

## Restore into a fresh installation

Stop Neo4j before loading. The load command below refuses to overwrite an
existing database. Keep a separate backup before replacing existing data.

```bash
docker compose stop backend neo4j
mkdir -p data/neo4j/data
docker run --rm --user 0 \
  --entrypoint /var/lib/neo4j/bin/neo4j-admin \
  -v "$PWD/data/neo4j/data:/data" \
  -v "$PWD/backups:/backups:ro" \
  neo4j:5.26-community database load neo4j --from-path=/backups
docker compose up -d
```

## Update the snapshot

The database must be stopped while dumping. Review the data before sharing it
through the repository. Every changed dump consumes additional LFS storage.

```bash
docker compose stop backend neo4j
docker run --rm --user 0 \
  --entrypoint /var/lib/neo4j/bin/neo4j-admin \
  -v "$PWD/data/neo4j/data:/data" \
  -v "$PWD/backups:/backups" \
  neo4j:5.26-community database dump neo4j --to-path=/backups --overwrite-destination=true
docker compose up -d
git add backups/neo4j.dump backups/README.md
git commit -m "chore: update Neo4j database snapshot"
git push
```

Update the snapshot date and source commit above when replacing the dump.
