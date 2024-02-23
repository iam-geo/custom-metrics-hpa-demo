# Variables. Configure these for your environment
KUBE_CONTEXT:=minikube
KUBE_CLUSTER:=minikube

ARGS:=--context="$(KUBE_CONTEXT)" --cluster="$(KUBE_CLUSTER)"

all: deploy

.PHONY: deploy
deploy:
# Monitoring tools
	kubectl apply -f ./k8s/kube-state-metrics/ $(ARGS)
	kubectl apply -f ./k8s/monitoring-namespace.yaml $(ARGS)
	kubectl apply -f ./k8s/prometheus-deployment.yaml $(ARGS)
	kubectl apply -f ./k8s/prometheus-adapter-deployment.yaml $(ARGS)
	kubectl apply -f ./k8s/grafana/ $(ARGS)
# Apps
	kubectl apply -f ./k8s/rabbitmq-deployment.yaml $(ARGS)
	kubectl apply -f ./k8s/hpa.yaml $(ARGS)
	kubectl apply -f ./k8s/producer-deployment.yaml $(ARGS)
	kubectl apply -f ./k8s/consumer-deployment.yaml $(ARGS)

.PHONY: clean
clean:
# Apps
	-kubectl delete -f ./k8s/consumer-deployment.yaml --context="$(KUBE_CONTEXT)"
	-kubectl delete -f ./k8s/producer-deployment.yaml --context="$(KUBE_CONTEXT)"
	-kubectl delete -f ./k8s/hpa.yaml --context="$(KUBE_CONTEXT)"
	-kubectl delete -f ./k8s/rabbitmq-deployment.yaml --context="$(KUBE_CONTEXT)"
# Mnitoring tools
	-kubectl delete -f ./k8s/prometheus-deployment.yaml $(ARGS)
	-kubectl delete -f ./k8s/prometheus-adapter-deployment.yaml $(ARGS)
	-kubectl delete -f ./k8s/grafana/ $(ARGS)
	-kubectl delete -f ./k8s/monitoring-namespace.yaml $(ARGS)
	-kubectl delete -f ./k8s/kube-state-metrics/ $(ARGS)

.PHONY: tests
tests:
	docker-compose -f docker-compose-test.yml run black
	docker-compose -f docker-compose-test.yml run flake8
