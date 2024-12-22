# Tork Sentiment Analysis demo

Download the latest [Tork binary](https://github.com/runabol/tork/releases/tag/v0.1.109) and untar it.

```bash
tar xvzf tork_0.1.109_darwin_arm64.tgz
```

Start Tork in `standalone` mode:

```bash
./tork run standalone
```

If all goes well, you should something like this:

```bash
...
10:36PM INF Coordinator listening on http://localhost:8000
...
```

Build the docker image that contains the sentiment analysis model

```bash
docker build -t sentiment-analysis .
```

Submit the job. Tork jobs execute asynchronously. Once a job is submitted you get back a job ID to track its progress:

```bash
JOB_ID=$(curl -s -X POST -H "content-type:text/yaml" --data-binary @sentiment.yaml http://localhost:8000/jobs | jq -r .id)
```

Wait for the job to complete:

```bash
while true; do state=$(curl -s http://localhost:8000/jobs/$JOB_ID | jq -r .state); echo "Status: $state"; if [ "$state" = "COMPLETED" ]; then; break; fi; sleep 1; done
```

Inspect the job results:

```bash
curl -s http://localhost:8000/jobs/$JOB_ID | jq -r .result
```

```
Positive
```