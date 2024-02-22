# Makefile for generating TLS certs for the Prometheus custom metrics API adapter

.PHONY: deploy
deploy:
	kubectl create -f ./k8s/monitoring-namespace.yaml
	kubectl create -f ./k8s/prometheus-deployment.yaml
	kubectl create -f ./k8s/prometheus-adapter-deployment.yaml
	kubectl create -f ./k8s/rabbitmq-deployment.yaml
	kubectl create -f ./k8s/hpa.yaml

start-simulation:
	kubectl apply -f ./k8s/producer-deployment.yaml
	echo " == Sleeping 20 to load up queue." > /dev/null
	sleep 20
	kubectl apply -f ./k8s/consumer-deployment.yaml
	echo " == Watch TARGET and REPLICAS for autoscaling action" > /dev/null
	echo " == Press CTRL+C to exit" > /dev/null
	kubectl get hpa consumer-deployment-hpa --watch