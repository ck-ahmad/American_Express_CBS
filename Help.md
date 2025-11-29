
# 🚀 Docker Commands for **DB-Project-CBS**

---

## 🏗️ 1. Build Docker Image(First Install Docker)
```bash
# Build your image with a name and version tag
docker build -t ck714/db-project-cbs:0.0.1.RELEASE .
````

---

## 🏃‍♂️ 2. Run Container from the Image

```bash
# Run in detached mode and map host port 5000 to container port 5000
docker container run -d -p 5000:5000 ck714/db-project-cbs:0.0.1.RELEASE
```

---

## 📋 3. List Running Containers

```bash
docker container ls
```

---

## ✋ 4. Stop a Container

```bash
# Use CONTAINER ID (first few characters) or container NAME
docker container stop <container_id_or_name>

# Examples:
docker container stop cee51dad436c
docker container stop fervent_driscoll
```

---

## 🗑️ 5. Remove a Stopped Container

```bash
docker container rm <container_id_or_name>
```

---

## 🖼️ 6. List All Images

```bash
docker images
```

---

## ❌ 7. Remove an Image

```bash
docker rmi <image_name_or_id>
```

---

## ⚡ Quick Start Example

```bash
# Build, Run, and Open Container in One Go
docker build -t ck714/db-project-cbs:0.0.1.RELEASE . &&
docker container run -d -p 5000:5000 ck714/db-project-cbs:0.0.1.RELEASE &&
docker container ls
```

> Tip: Use `docker logs <container_id_or_name>` to check Flask app output.

```

