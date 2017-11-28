
- run the container

	docker run --privileged -tid -v /sys/fs/cgroup:/sys/fs/cgroup:ro -p 2222:22 local/teamtalk_run_base

- interact with the container instance

	docker exec -it <THE-CONTAINER-INSTANCE-ID> /bin/bash

