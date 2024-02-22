# custom-metrics-hpa-demo

This project demonstrates how to use custom metrics for autoscaling deployments.

Components:

* kubernetes cluster
  * For running our containers
* prometheus
  * metric scraper and datastore
* rabbitmq cluster
  * message broker which we will scrape custom metrics for HPA
* producer & consumer app
  * python apps to generate and consumer messages
* grafana
  * for watching this in action

## Requirements

* docker (+25.0.3)
* kubectl (+v1.29.2)
* Python (+3.10)
* minikube (+1.32.0)

## Instructions

### Deploy the setup

1. Install docker and minikube.
2. Start the cluster.

    ```bash
    minikube start
    ```

3. Deploy the setup.

    ```bash
    make
    ```

> [!TIP]
> Useful commands
>
> ```bash
> make deploy # deploys the setup
> make clean # deletes the setup
> ```

### Monitoring

1. Launch grafana UI

    ```bash
    minikube --namespace=monitoring service grafana-service
    ```

2. Locate or search for dashboard `custom-metrics-hpa-demo`.
